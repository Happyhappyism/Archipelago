
from typing import TYPE_CHECKING, Set, Optional, Dict, Any
import logging
from NetUtils import ClientStatus
#Test comment
from base64 import b64encode
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

import time
import random

from .Items import item_recv_text
logger = logging.getLogger("Client")

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

RECV_IDX = 0x2FFF
DEX_SIZE = 0x96
RECV_PORT = 0x1AF0

class PokePinballClient(BizHawkClient):
    game = "Pokemon Pinball"
    system = "GBC"
    patch_suffix = ".apkpinball"
    local_checked_locations: Set[int]
    rom_slot_name: Optional[str]

    death_link: bool = False
    sending_death_link: bool = True
    pending_death_link: bool = False
    score_goal = False
    all_needed_mons = False
    dex_complete = False

    notes_used = 0
    dex_need = 151
    score_need = 1000000000


    #needed_mons = b''

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.rom_slot_name = None
        self.game_state = False
        self.research_command = None

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger
        from .Rom import ROM_NAME_ADR, PLAYER_NAME_ADR, OPTION_ADR
        rom_data = await bizhawk.read(
            ctx.bizhawk_ctx,
            [
            (0x134, 0xB, "ROM"), # 0 Rom Name
            (OPTION_ADR, 0x10, "ROM"), # 1 Options
            (PLAYER_NAME_ADR, 0x32, "ROM"), # 2 Player Name
            (ROM_NAME_ADR, 0x20, "ROM"), # 3 Slot Data
            (0xDD400, DEX_SIZE, "ROM"), # 4 Needed Mons
            #(0x1962, DEX_SIZE, "WRAM"), # 5 Dex State
            ]
        )
        try:
            rom_name = rom_data[0].decode("ascii")
            if rom_name != "POKEPINBALL":
                return False
            try:
                slot_name_bytes = rom_data[2]
                self.rom_slot_name = bytes([byte for byte in slot_name_bytes if byte != 0]).decode("utf-8")
            except UnicodeDecodeError:
                logger.info("Could not read slot name from ROM. Are you sure this ROM matches this client version?")
                return False
        except bizhawk.RequestFailedError:
            return False  # Not able to get a response, say no for now
        
        gameoptions = rom_data[1]
        deathlink = gameoptions[2]
        self.needed_mons = rom_data[4]
        # = needed_mon_raw
        if deathlink:
            self.death_link = True
        #self.notes_used = 0
        self.dex_need = gameoptions[0]
        self.score_need = int.from_bytes((rom_data[0x8:0x0C]), byteorder='little', signed=False)
        ctx.game = self.game
        ctx.items_handling = 0b111
        self.player_name = rom_data[2].decode("ascii")
        ctx.command_processor.commands["research"] = cmd_notes
        ctx.slot = chr(rom_data[3][7])
        ctx.want_slot_data = True
        #self.dex_state = rom_data[5]
        return True
    
    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: Dict[str, Any]) -> None:
        if cmd == "Bounced":
            if "tags" in args:
                assert ctx.slot is not None
                if "DeathLink" in args["tags"] and args["data"]["source"] != ctx.slot_info[ctx.slot].name:
                    self.on_deathlink(ctx)

    async def send_deathlink(self, ctx: "BizHawkClientContext") -> None:
        self.sending_death_link = True
        ctx.last_death_link = time.time()
        await ctx.send_death("Pinballs were lost.")

    def on_deathlink(self, ctx: "BizHawkClientContext") -> None:
        ctx.last_death_link = time.time()
        self.pending_death_link = True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        ctx.auth = self.rom_slot_name

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger
        def send_banner_msg(text:str,writes:list, item_timer:int):
                if item_timer == 0:
                    while len(text) < 0x20:
                        text += " "
                    writes.append((0x500, text.encode("ascii") , "WRAM"))
                    
                    writes.append((0x15CA, bytearray([0x01,0x01,0x01,0x02,0x05,0x54,0x10,0x14]) , "WRAM"))
                    writes.append((0x1AF4, (0xFF).to_bytes(1, "little") , "WRAM"))
                return writes
        
        if ctx.slot is None:
            await ctx.send_connect(name=ctx.auth)

        try:
            ram_data = await bizhawk.read(
                ctx.bizhawk_ctx,
                [
                    (0x1400, 0x100, "WRAM"), # 0 Game RAM
                    (0x1962, DEX_SIZE, "WRAM"), # 1 Pokedex Data
                    (0x18F1, 0x1, "WRAM"), # 2 Game State
                    (RECV_IDX, 0x1, "WRAM"), # 3 Recv Index
                    (0x1616, 0x1, "WRAM"), # 4 Death State
                    (0x1AF0, 0x20, "WRAM"), # 5 AP RAM
                    (0x19FB, 0x01, "WRAM"), # 6 Pokeon Owned
                    (0x1540, 0x10, "WRAM"), # 7 Current Map
                ]
            )
            outbound_writes = []
            game_data = ram_data[0]
            pokedex_data = ram_data[1]
            #self.dex_state = pokedex_data
            game_screen = ram_data[2][0]
            recv_index = ram_data[3][0]
            mon_owned = 0
            death_state = game_data[0xC9]
            game_over = ram_data[0x4][0]
            ap_ram = ram_data[5]
            item_timer = ap_ram[0x4]
            bonus_clear = game_data[0x9A]
            stage_cur = game_data[0xAC]
            #meowth_score = ram_data[7][0]
            #seel_score = ram_data[0xA][0]
            #diglett_score = ram_data[8][0]
            #gastly_score = ram_data[9][0]
            #mewtwo_clears = ram_data[0xB][0]


            if game_screen != 0x04:
                # Make sure you are in a pinball game
                return
            self.game_state = True
            
            if self.death_link:
                await ctx.update_death_link(self.death_link)

            if self.pending_death_link:
                ## Handle deathlink
                outbound_writes.append((0x14B3, bytearray([0xF8, 0x44, 0x55, 0xA9]), "WRAM"))
                self.pending_death_link = False
                self.sending_death_link = True

            if "DeathLink" in ctx.tags  and ctx.last_death_link + 10 < time.time():
                if game_over == 0x01 and not self.sending_death_link:
                    await self.send_deathlink(ctx)
                else:
                    self.sending_death_link = False

            locs_to_send = set()
            # Handle Locations
                # Pokedex
            mon_idx = 0
            for val in pokedex_data:
                mon_idx += 1
                if val & 2:
                    loc_id = 0x1C2000 + mon_idx
                    if loc_id not in self.local_checked_locations:
                        locs_to_send.add(loc_id)
                # Map Events
            if ap_ram[0x1] and 0x1C2098 not in self.local_checked_locations:
                locs_to_send.add(0x1C2098)
            if ap_ram[0x2] and 0x1C2099 not in self.local_checked_locations:
                locs_to_send.add(0x1C2099)

            if bonus_clear == 0x1:
                if stage_cur == 0xD and 0x1C209A not in self.local_checked_locations:
                    locs_to_send.add(0x1C209A)
                if stage_cur == 0xB and 0x1C209B not in self.local_checked_locations:
                    locs_to_send.add(0x1C209B)
                if stage_cur == 0x7 and 0x1C209C not in self.local_checked_locations:
                    locs_to_send.add(0x1C209C)
                if stage_cur == 0xF and 0x1C209D not in self.local_checked_locations:
                    locs_to_send.add(0x1C209D)
                if stage_cur == 0x9 and 0x1C209E not in self.local_checked_locations:
                    locs_to_send.add(0x1C209E)
                #outbound_writes.append((0x149A,bytearray([0x00]), "WRAM"))

                # Score
            cur_score = 0
            for x in range(6):
                offset = 0x6A + x
                score_digits = game_data[offset]
                lower_digit = score_digits & 0xF
                upper_digit = ((score_digits & 0xF0) >> 4) * 10
                dec_score = upper_digit + lower_digit
                added_score = (dec_score * (10**(x*2))) * 10
                cur_score = cur_score + added_score
                #logger.warning(f"score: {cur_score}, H: {upper_digit}, L: {lower_digit}, DS: {dec_score}, SD: {score_digits}, AS{added_score}")
            #score10k = game_data[0x6D]
            
            if cur_score >= 20000000 and 0x1C20A0 not in self.local_checked_locations:
                locs_to_send.add(0x1C20A0)
            if cur_score >= 50000000 and 0x1C20A1 not in self.local_checked_locations:
                locs_to_send.add(0x1C20A1)
            if cur_score >= 100000000 and 0x1C20A2 not in self.local_checked_locations:
                locs_to_send.add(0x1C20A2)
            if cur_score >= 250000000 and 0x1C20A3 not in self.local_checked_locations:
                locs_to_send.add(0x1C20A3)
            if cur_score >= 500000000 and 0x1C20A4 not in self.local_checked_locations:
                locs_to_send.add(0x1C20A4)
            
            if locs_to_send != self.local_checked_locations:
                self.local_checked_locations = locs_to_send
                if locs_to_send is not None:
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": list(locs_to_send)}])

            # Handle Items
                # Permanent Items
            notes_have = 0
            red_stages = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
                         0x00,0x00]
            blue_stages = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
                         0x00,0x00]
            
            for item in range(len(ctx.items_received)):
                raw_item = ctx.items_received[item].item
                match raw_item:
                    #case 0x1C2000:
                    #    pokeball_level += 1
                    #    if pokeball_level > 3:
                    #        pokeball_level = 3
                    case 0x1C2002: # Viridian Forest
                        red_stages[0x2] = 0x01
                        blue_stages[0x2] = 0x01
                    case 0x1C2003: # Pewter City
                        red_stages[0x3] = 0x01
                    case 0x1C2004: # Mt Moon
                        blue_stages[0x4] = 0x01
                    case 0x1C2005: # Cerulean City
                        red_stages[0x5] = 0x01
                        blue_stages[0x5] = 0x01
                    case 0x1C2006: # Vermilion City Seaside
                        red_stages[0x6] = 0x01
                    case 0x1C2007: # Vermilion City Streets
                        blue_stages[0x7] = 0x01
                    case 0x1C2008: # Rock Mountain
                        red_stages[0x8] = 0x01
                        blue_stages[0x8] = 0x01
                    case 0x1C2009: # Lavender Town
                        red_stages[0x9] = 0x01
                    case 0x1C200A: # Celadon City
                        blue_stages[0xA] = 0x01
                    case 0x1C200B: # Cycling Road
                        red_stages[0xB] = 0x01
                    case 0x1C200C: # Safari Zone
                        red_stages[0xC] = 0x01
                        blue_stages[0xC] = 0x01
                    case 0x1C200D: # Fuchsia City
                        blue_stages[0xD] = 0x01
                    case 0x1C200E: # Saffron City
                        blue_stages[0xE] = 0x01
                    case 0x1C200F: # Seafoam Islands
                        red_stages[0xF] = 0x01
                    case 0x1C2010: # Cinnabar Island
                        red_stages[0x10] = 0x01
                        blue_stages[0x10] = 0x01
                    case 0x1C2011: # Indigo Plateau
                        red_stages[0x11] = 0x01
                        blue_stages[0x11] = 0x01
                    case 0x1C2020:
                        notes_have += 1

            
            #balltypes = [0x00, 0x02, 0x03, 0x05]
            #outbound_writes.append((0x147E,bytearray(balltypes[pokeball_level]), "WRAM"))
            outbound_writes.append((0x1AB0,bytearray(red_stages), "WRAM"))
            outbound_writes.append((0x1AD0,bytearray(blue_stages), "WRAM"))

                # Temp Items
            if (len(ctx.items_received) > recv_index) and (ap_ram[0] == 0x00) and (stage_cur == 0x01 or stage_cur == 0x5):
                raw_item = ctx.items_received[recv_index].item
                #item_name = ctx.items_received[recv_index].player
                #logger.warning(f"{ctx.items_received[recv_index]}")
                match raw_item:
                    case 0x1C2030:   # Extra Ball
                        #lives_cur = game_data[0x9B]
                        #if lives_cur == 9:
                        #    lives = 9
                        #else:
                        #    lives = lives_cur + 1
                        outbound_writes.append((RECV_PORT, bytearray([0x07]), "WRAM"))
                    case 0x1C2031:   # Pika Power
                        outbound_writes.append((RECV_PORT, bytearray([0x03]), "WRAM"))
                    case 0x1C2032:   # Ball Saver
                        outbound_writes.append((RECV_PORT, bytearray([0x06]), "WRAM"))
                    case 0x1C2033:   # Slots
                        outbound_writes.append((0x1513, bytearray([0x01]), "WRAM"))
                        outbound_writes.append((RECV_PORT, bytearray([0x02]), "WRAM"))
                    case 0x1C2034:  # Catchem Mode
                        outbound_writes.append((RECV_PORT, bytearray([0x01]), "WRAM"))
                        
                    case 0x1C2035:  # Evolution Mode
                        outbound_writes.append((0x1543, bytearray([0x03]), "WRAM"))
                        outbound_writes.append((RECV_PORT, bytearray([0x02]), "WRAM"))

                        if stage_cur == 0x04 or stage_cur == 0x05:
                            # Blue Field
                            outbound_writes.append((0x14AC, bytearray([0x04]), "WRAM"))
                            outbound_writes.append((0x14B3, bytearray([0x00, 0x2E, 0x00, 0x77]), "WRAM"))
                        elif stage_cur == 0x01 or stage_cur == 0x00:
                            # Red Field
                            outbound_writes.append((0x14AC, bytearray([0x00]), "WRAM"))
                            outbound_writes.append((0x14B3, bytearray([0x00, 0x11, 0x00, 0x23]), "WRAM"))
                        #
                        #outbound_writes.append((RECV_PORT, bytearray([0x01]), "WRAM"))
                        #outbound_writes.append((0x1608, bytearray([0x01]), "WRAM"))
                    case 0x1C2036: # Bonus Multiplier
                        outbound_writes.append((RECV_PORT, bytearray([0x04]), "WRAM"))
                    case 0x1C2038: # Ball Upgrade
                        outbound_writes.append((RECV_PORT, bytearray([0x08]), "WRAM"))
                if raw_item in item_recv_text:
                    #logger.warning(f"Billboard Msg: {item_recv_text[raw_item]}")
                    #send_banner_msg(item_recv_text[raw_item].upper(), outbound_writes, item_timer)
                    pass
                outbound_writes.append((RECV_IDX, (recv_index +1).to_bytes(1, "little") , "WRAM"))
                

            # Handle notes command
            if self.research_command:
                dex_offset = self.research_command
                if (notes_have > self.notes_used) and pokedex_data[dex_offset] != 0x03:
                    outbound_writes.append((0x1962+dex_offset, bytearray([0x03]), "WRAM"))
                    self.notes_used += 1
                else:
                    self.research_command = None
            # Handle Goal
            goalclear = False
            #all_needed_mons = False
            #score_clear = False

            counted_mons = 0
            mon_owned = 0

            for offset in range(DEX_SIZE):
                if (pokedex_data[offset] | self.needed_mons[offset]) & 0x02 == 0x2:
                    counted_mons += 1
                else:
                    #counted_mons = 0
                    break
            for offset in range(DEX_SIZE):
                if (pokedex_data[offset] & 0x2):
                    mon_owned += 1

            #logger.warning(f"Counted Mons: {counted_mons}, Needed Mons: {self.dex_need}, Mons_Owned: {mon_owned}")
            if counted_mons >= DEX_SIZE and self.all_needed_mons == False:
                self.all_needed_mons = True
                logger.warning(f"RESEARCH COMPLETE!")
                send_banner_msg("RESEARCH COMPLETE!", outbound_writes, item_timer)
                
            if (cur_score >= self.score_need) and (self.score_goal == False):
                self.score_goal = True
                if self.score_need:
                    logger.warning(f"GOAL SCORE COMPLETE!")
                    send_banner_msg("GOAL SCORE COMPLETE!", outbound_writes, item_timer)

            if (mon_owned >= self.dex_need) and self.dex_complete == False:
                self.dex_complete = True
                if self.dex_need:
                    logger.warning(f"POKEDEX COMPLETE!")
                    send_banner_msg("POKEDEX COMPLETE!", outbound_writes, item_timer)


            if (self.dex_complete) and (self.all_needed_mons) and (self.score_goal):
                goalclear = True
                

            if not ctx.finished_game and goalclear:
                send_banner_msg("CONGRADULATIONS YOU WIN!", outbound_writes, item_timer)
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])
                ctx.finished_game = True
            await bizhawk.write(ctx.bizhawk_ctx, outbound_writes)

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass

def cmd_notes(self, sub: str = ""):
    from .Locations import pokemon_names
    """Allows you to research a dex entry for a pokemon you have access to.
    example: /research Blastoise"""
    if self.ctx.game != "Pokemon Pinball":
        logger.warning(f"This command can only be used while playing Pokemon Pinball")
        return
    if (not self.ctx.server) or self.ctx.server.socket.closed or not self.ctx.client_handler.game_state:
        logger.warning(f"Must be connected to server and in game.")
        return
    elif not sub:
        logger.warning(f"A Pokemon must be named")
    elif sub not in pokemon_names:
        logger.warning(f"Pokemon not found")
    else:
        self.ctx.client_handler.research_command = pokemon_names.index(sub)
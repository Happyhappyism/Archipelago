
from typing import TYPE_CHECKING, Set, Optional, Dict, Any
import logging
from NetUtils import ClientStatus
#Test comment
from base64 import b64encode
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

import time
import random

from .Items import item_WRAM_address, item_stackable
from .Locations import overworld_flags, monster_flags, sythesis_flags

logger = logging.getLogger("Client")

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

RECV_IDX = 0xEB0
RECV_PORT = 0xEB1

class BombQuestClient(BizHawkClient):
    game = "Bomberman Quest"
    system = "GBC"
    patch_suffix = ".apbombquest"
    local_checked_locations: Set[int]
    rom_slot_name: Optional[str]

    death_link: bool = False
    game_goal = 0
    sending_death_link: bool = True
    pending_death_link: bool = False


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
            (ROM_NAME_ADR, 0x3, "ROM"), # 0 Rom Name
            (OPTION_ADR, 0x10, "ROM"), # 1 Options
            (PLAYER_NAME_ADR, 0x32, "ROM"), # 2 Player Name
            (ROM_NAME_ADR, 0x20, "ROM"), # 3 Slot Data
            (0x134, 0xB, "ROM"), # 4 Game Title
            ]
        )
        try:
            rom_name = (rom_data[4]).decode("ascii")
            ap_string = (rom_data[0]).decode("ascii")
            if rom_name != "BOMBERQUEST":
                logger.info(f"Wrong Name {rom_name} for this client")
                return False
            elif ap_string != "BQU":
                logger.info(f"Please use the Archipelago patched rom for this client")
                return False
            try:
                slot_name_bytes = rom_data[2]
                self.rom_slot_name = bytes([byte for byte in slot_name_bytes if byte != 0]).decode("utf-8")
            except UnicodeDecodeError:
                logger.info("Could not read slot name from ROM. Are you sure this ROM matches this client version?")
                return False
        except bizhawk.RequestFailedError:
            logger.info(f"Request Failed")
            return False  # Not able to get a response, say no for now
        
        gameoptions = rom_data[1]
        self.game_goal = gameoptions[0]
        deathlink = gameoptions[1]
        
        if deathlink:
            self.death_link = True
        ctx.game = self.game
        ctx.items_handling = 0b101
        self.player_name = rom_data[2].decode("ascii")
        ctx.slot = chr(rom_data[3][7])
        ctx.want_slot_data = True

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
        await ctx.send_death("Bomberman Died.")

    def on_deathlink(self, ctx: "BizHawkClientContext") -> None:
        ctx.last_death_link = time.time()
        self.pending_death_link = True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        ctx.auth = self.rom_slot_name

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger
        
        if ctx.slot is None:
            await ctx.send_connect(name=ctx.auth)

        try:
            ram_data = await bizhawk.read(
                ctx.bizhawk_ctx,
                [
                    (RECV_IDX, 0x2, "WRAM"), # 0 Recv Index
                    (0xEA1, 0x6, "WRAM"), # 1 Overworld Item Flags
                    (0xEB2, 0x38, "WRAM"), # 2 Monster Flags
                    (0xF24, 0x40, "WRAM"), # 3 Inventory
                    (0xE93, 0x8, "WRAM"), # 4 Game Start flag
                    (0xE81, 0x2, "WRAM"), # 5 Health
                    (0x1000, 0x20,"WRAM" )  # 6 AP Flags
                    
                ]
            )
            outbound_writes = []
            recv_index = ram_data[0][0]
            ap_port = ram_data[0][1]
            #game_flags = ram_data[2]
            overworld_data = ram_data[1]
            monster_data = ram_data[2]
            inventory_data = ram_data[3]
            ap_data = ram_data[6]
            game_flags = ram_data[4]
            health = ram_data[5][1]
            event_flags = ram_data[4][5]


            if game_flags[0] != 0x58 or game_flags[1] != 0x4C:
                # Make sure ram has been initialized
                return
            
            self.game_state = True
            if recv_index == 0xFF:
                outbound_writes.append((RECV_IDX, bytearray([0x00]), "WRAM"))
            
            if self.death_link:
                await ctx.update_death_link(self.death_link)

            if self.pending_death_link:
                ## Handle deathlink
                # Code to kill the player
                outbound_writes.append((0x390, bytearray([0x00]), "WRAM"))
                outbound_writes.append((0xE82, bytearray([0x00]), "WRAM"))
                outbound_writes.append((0xEB1, bytearray([(ap_port | 0x1)]), "WRAM"))
                self.pending_death_link = False
                self.sending_death_link = True

            if "DeathLink" in ctx.tags  and ctx.last_death_link + 10 < time.time():
                # Code to check if you are dead
                if health == 0 and ((ap_port & 0xFE) == 0):
                    outbound_writes.append((0xEB1, bytearray([(ap_port & 0xFE)]), "WRAM"))
                    await self.send_deathlink(ctx)
                else:
                    self.sending_death_link = False

            locs_to_send = set()
            # Handle Locations

            for loc_id, raw_offset in monster_flags.items():
                if loc_id not in self.local_checked_locations:
                    offset = raw_offset - 0xEB2
                    flags = monster_data[offset]
                    if flags & 0x1:
                        locs_to_send.add(loc_id)

            for loc_id, data in overworld_flags.items():
                if loc_id not in self.local_checked_locations:
                    raw_offset = data[0]
                    flag_mask = data[1]
                    offset = raw_offset - 0xEA1
                    flags = overworld_data[offset]
                    if flags & flag_mask:
                        locs_to_send.add(loc_id)

            for loc_id, flag_mask in sythesis_flags.items():
                if loc_id not in self.local_checked_locations:
                    flags = overworld_data[2]
                    if flags & flag_mask:
                        locs_to_send.add(loc_id)

            if event_flags & 0x01:
                trade_id = 0x1C3078
                if trade_id not in self.local_checked_locations:
                    locs_to_send.add(trade_id)
            # for val in game_flags:
            #     flag_idx = 0
            #     if val != 0x00:
            #         loc_id = 0x40001 + flag_idx
            #         if loc_id not in self.local_checked_locations:
            #             locs_to_send.add(loc_id)
            #     flag_idx += 1
            #     # Score

            if locs_to_send != self.local_checked_locations:
                self.local_checked_locations = locs_to_send
                if locs_to_send is not None:
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": list(locs_to_send)}])

            # Handle Items
            # item_WRAM_address
            if (len(ctx.items_received) > recv_index):
                raw_item = ctx.items_received[recv_index].item
                write_offset = item_WRAM_address[raw_item]
                if raw_item in item_stackable:
                    starting_count = inventory_data[write_offset- 0xF24] & 0xF
                    count = starting_count + 1
                    item_value = count + 0x10
                    outbound_writes.append((write_offset, bytearray([item_value]) , "WRAM"))
                else:
                    outbound_writes.append((write_offset, bytearray([0x10]) , "WRAM"))
                outbound_writes.append((RECV_IDX, (recv_index +1).to_bytes(1, "little") , "WRAM"))


            # Handle Goal
            goalclear = False
            if self.game_goal == 0 and (
                0x1C300D in self.local_checked_locations and \
                0x1C301D in self.local_checked_locations and \
                0x1C302D in self.local_checked_locations and \
                0x1C303D in self.local_checked_locations
            ):
                goalclear = True
            elif self.game_goal == 1 and (monster_data[0x34] & 0x40): # Chaos Bomber
                goalclear = True
            elif self.game_goal == 2 and (event_flags & 0x01) == 1: # Card Trade
                goalclear = True
            if not ctx.finished_game and goalclear == True:

                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

            await bizhawk.write(ctx.bizhawk_ctx, outbound_writes)

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass

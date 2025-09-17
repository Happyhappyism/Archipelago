from typing import TYPE_CHECKING, Set, Optional, Dict, Any
import logging

from NetUtils import ClientStatus
from .Items import id_to_string
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

import time
import random

#from .com_ap_methods import randomize_table_with_exclude, split_into_xbit_chunks

logger = logging.getLogger("Client")

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

ARCADE_MAP = {
    0x1E: 0x1C2700, # B Valley  30
    0x28: 0x1C2701, # S Forest  40
    0x32: 0x1C2702, # Upsilon   50
    0x3C: 0x1C2703, # Volcano   60
}


# def split_into_xbit_chunks(byte_array,size):
#    #Splits a byte array into chunks of 32 bits (4 bytes).

#     chunks = []
#     for i in range(0, len(byte_array), size):
#         chunk = byte_array[i:i + size]
#         # If the last chunk is less than 4 bytes, pad it with zeros
#         if len(chunk) < size:
#             chunk += b'\x00' * (size - len(chunk)) 
#         chunks.append(chunk)
#     return chunks

# def ramdomize_table_with_exclude(tbl,entrysize,excepts):
#     split_table = split_into_xbit_chunks(tbl,entrysize)
#     idxshuffle = []
#     new_table = []
#     for x in range(len(split_table)):
#         idxshuffle.append(x)
#         new_table.append(b'/x00/x00/x00/x00')
#     random.shuffle(idxshuffle)
#     for idx in range(len(split_table)):
#         if idx in excepts:
#             new_table[idx] = split_table[idx]
#             continue
#         randidx = idxshuffle.pop(0)
#         while randidx in excepts:
#             randidx = idxshuffle.pop(0)
#         new_table[idx] = split_table[randidx]
#     result = b''.join(new_table)
#     return result

# Client Code mirrored from Yugioh 2006 apworld
#item_name_to_id = {name: data for name, data in item_data_table}

class BomberTClient(BizHawkClient):
    game = "Bomberman Tournament"
    system = "GBA"
    patch_suffix = ".apbombt"
    local_checked_locations: Set[int]
    rom_slot_name: Optional[str]

    death_link: bool = False
    sending_death_link: bool = True
    pending_death_link: bool = False

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.rom_slot_name = None


    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger
        try:
            # Check ROM name/patch version
            rom_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(0xA0, 11, "ROM")]))[0]).decode("ascii")
            if rom_name != "BOMSTORYUSA":
                return False  # Not a Bomberman Tournament ROM
            try:
                slot_name_bytes = (await bizhawk.read(ctx.bizhawk_ctx, [(0x30, 32, "ROM")]))[0]
                self.rom_slot_name = bytes([byte for byte in slot_name_bytes if byte != 0]).decode("utf-8")
            except UnicodeDecodeError:
                logger.info("Could not read slot name from ROM. Are you sure this ROM matches this client version?")
                return False
        except bizhawk.RequestFailedError:
            return False  # Not able to get a response, say no for now

        # This is a Bomberman Tournament ROM
        ctx.game = self.game
        ctx.items_handling = 0b111

        deathlink = (await bizhawk.read(ctx.bizhawk_ctx, [(0x3C2800, 1, "ROM")]))[0][0]
        if deathlink:
            self.death_link = True

        ctx.want_slot_data = True
        #bizhawk.set_message_interval(ctx.bizhawk_ctx,5)
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
        await ctx.send_death("Bomberman is dead.")

    def on_deathlink(self, ctx: "BizHawkClientContext") -> None:
        ctx.last_death_link = time.time()
        self.pending_death_link = True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        ctx.auth = self.rom_slot_name

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        try:
            # Read save data
            ram_data = await bizhawk.read(
                ctx.bizhawk_ctx,
                [
                (0x35194, 0x7,  "EWRAM"),# 0 Stats
                (0x35278, 0x90, "EWRAM"), # 1 Flags
                (0x3525C, 0x1, "EWRAM"), # 2 Temp location, uses MarinGon's loss record
                (0x34980, 0x4, "EWRAM"), # 3 Arcade
                ]
            )
            outbound_writes = []
            bomber_stats = ram_data[0]
            flag_data = ram_data[1]
            recv_index = ram_data[2][0]
            game_start = flag_data[0x29] & 0x1
            game_win = flag_data[0x19] & 0x4
            arcade_needed_score = ram_data[3][0]
            arcade_current_score = ram_data[3][2]

            if game_start == 0:
                return

            #Deathlink
            if self.death_link:
                await ctx.update_death_link(self.death_link)
            if self.pending_death_link:
                outbound_writes.append((0x2594, bytearray([0xC5, 0x84]), "IWRAM"))
                outbound_writes.append((0x259C, bytearray([0x0B, 0xD0]), "IWRAM"))
                outbound_writes.append((0x60A1, bytearray([0x11]), "IWRAM"))
                self.pending_death_link = False
                self.sending_death_link = True
            if "DeathLink" in ctx.tags  and ctx.last_death_link + 1 < time.time():
                if bomber_stats[0] == 0 and not self.sending_death_link:
                    await self.send_deathlink(ctx)
                elif bomber_stats[0] != 0:
                    self.sending_death_link = False

            # Check locations
            locs_to_send = set()
            offset = 0
            for val in flag_data:
                for bit in range(8):
                    loc_id = 0x1C2780 + (offset * 0x10) + bit
                    mask = 1 << bit
                    flag = val & mask
                    if flag and loc_id in ctx.server_locations:
                        locs_to_send.add(loc_id)
                offset += 1
            
            # Arcade
            if arcade_needed_score in ARCADE_MAP:
                loc_id = ARCADE_MAP[arcade_needed_score]
                if (arcade_current_score >= arcade_needed_score) and ( loc_id in ctx.server_locations):
                    locs_to_send.add(loc_id)

            if locs_to_send != self.local_checked_locations:
                self.local_checked_locations = locs_to_send

                if locs_to_send is not None:
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": list(locs_to_send)}])

            # Process Items 
            if len(ctx.items_received) > recv_index:
                raw_item = ctx.items_received[recv_index].item
                item_index = int(((raw_item & 0xFFFFF0)/0x10)- 0x1C278)
                item_adr = item_index + 0x35278
                bit = int(raw_item & 0xF)
                if bit > 7:
                    match bit:
                        case 0x8: # Money
                            oldval = bomber_stats[4] + (bomber_stats[5] << 8)
                            if raw_item == 0x1C2958:
                                amount = 50
                            elif raw_item == 0x1C29A8:
                                amount = 100
                            else:
                                amount = 25
                            newval = (oldval + amount)
                            #highval = (oldval + amount) & 0xF00
                            item_adr = 0x35198
                            outbound_writes.append((item_adr, newval.to_bytes(2, "little"), "EWRAM"))
                        case 0xA: # Max Health
                            oldval = bomber_stats[1]
                            newval = oldval + 2
                            item_adr = 0x35195
                        case 0xB: # Bomb Up
                            oldval = bomber_stats[2]
                            newval = oldval + 1
                            item_adr = 0x35196
                        case 0xC: # Fire up
                            oldval = bomber_stats[3]
                            newval = oldval + 1
                            item_adr = 0x35197
                        case 0xD: #Boots
                            oldval = flag_data[0]
                            if oldval & 0x2:
                                newval = oldval | 0x8
                            else:
                                newval = oldval | 0x2
                        case 0xE: #Armor
                            oldval = flag_data[0]
                            if oldval & 0x4:
                                newval = oldval | 0x10
                            else:
                                newval = oldval | 0x4
                        case 0xF: # Other
                            match raw_item:
                                case 0x1C298F: # Zone Key
                                    zonekeys = sum(itemid.item == 0x1C298F for itemid in ctx.items_received)
                                    if zonekeys > 3:
                                        zonekeys = 3
                                    zoneindex = zonekeys - 1 
                                    keyoffsets = [0x20,0x20,0x25]
                                    keymasks = [0x4,0x20,0x2]
                                    oldval = flag_data[keyoffsets[zoneindex]]
                                    newval = oldval | keymasks[zoneindex]
                                    item_adr = 0x35278 + keyoffsets[zoneindex]
                                    #logger.warning(f"{zoneindex}, {hex(item_adr)}: {hex(oldval)} -> {hex(newval)}; {ctx.items_received}")
                                case _: #Don't know what happened, take a medicine
                                    item_adr = 0x3527B
                                    oldval = flag_data[3]
                                    newval = oldval | 0x8
                        case _: #Don't know what happened, take a medicine
                            item_adr = 0x3527B
                            oldval = flag_data[3]
                            newval = oldval | 0x8
                elif raw_item == 0x1C27B3 or raw_item == 0x1C27B4:
                    oldhp = bomber_stats[0]
                    maxhp = bomber_stats[1]
                    if   raw_item == 0x1C27B3: # Small Medicine
                        have_med = flag_data[3] & 0x8
                        if have_med and (oldhp == maxhp):
                            pass
                        elif have_med:
                            newhp = oldhp + 2
                            if newhp > maxhp:
                                newhp = maxhp
                            outbound_writes.append((0x35194, newhp.to_bytes(1, "little"), "EWRAM"))
                            item_adr = 0x352F8

                    elif raw_item == 0x1C27B4: # Large Medicine
                        have_med = flag_data[3] & 0x10
                        if have_med and (oldhp == maxhp):
                            pass
                        elif have_med:
                            newhp = maxhp
                            outbound_writes.append((0x35194, newhp.to_bytes(1, "little"), "EWRAM"))
                            item_adr = 0x352F8
                    oldval = flag_data[item_index]
                    newval = oldval | (1 << bit)
                else:
                    oldval = flag_data[item_index]
                    newval = oldval | (1 << bit)
                if raw_item == 0x1C2958 or raw_item == 0x1C29A8:
                    pass
                else:
                    outbound_writes.append((item_adr, newval.to_bytes(1, "little"), "EWRAM"))

                outbound_writes.append((0x3525C, (recv_index +1).to_bytes(1, "little") , "EWRAM"))
                if raw_item in id_to_string:
                    itemtext = id_to_string[raw_item]
                    while len(itemtext) < 22:
                        itemtext = itemtext + " "
                    outstr = b'\xE0\x12\x0CReceived\xfa' + itemtext.encode('ascii') + b'\xfd'
                    linkflag = flag_data[0x27] | 0x80
                    
                    outbound_writes.append((0x215AE0, outstr, "ROM"))
                    outbound_writes.append((0x3529F, bytearray([linkflag]) , "EWRAM"))

            # Send Theta Access
            if flag_data[26] & 0x80 == 0:
                brave_medal = flag_data[1] & 0x80
                other_medal = flag_data[2] & 0xA4
                if brave_medal == 0x80 and  other_medal == 0xA4:
                    new_flag = flag_data[26] | 0x80
                    outbound_writes.append((0x3529E, new_flag.to_bytes(1, "little") , "EWRAM"))

            # Send game clear
            if not ctx.finished_game and game_win:
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

            await bizhawk.write(ctx.bizhawk_ctx, outbound_writes)

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass
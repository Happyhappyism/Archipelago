import logging
import time
import asyncio

from NetUtils import ClientStatus, color
from worlds.AutoSNIClient import SNIClient

snes_logger = logging.getLogger("SNES")

# FXPAK Pro protocol memory mapping used by SNI
ROM_START = 0x000000
WRAM_START = 0xF50000
WRAM_SIZE = 0x20000
SRAM_START = 0xE00000

ACTR_ROMNAME_START = 0x00FFC0
ACTR_ROMHASH_START = 0x7FC0
ROMNAME_SIZE = 0x15
ROMHASH_SIZE = 0x15

GAMEMODE = WRAM_START + 0x18
#DEATH_FLAG = WRAM_START + 0x766
ACTR_DEATH_STATES = {0x1}
DEATH_SEND = WRAM_START + 0x1A0A
DEATH_LOCAL = WRAM_START + 0x1A0D
DEATH_TIME = WRAM_START + 0x1A0C

MAX_HP = WRAM_START + 0x293
MAX_MP = WRAM_START + 0x296

OFFER_FILLMORE =WRAM_START + 0x24C
OFFER_BLOOD =   WRAM_START + 0x255
OFFER_KASA = WRAM_START + 0x25E
OFFER_AITOS = WRAM_START + 0x267
OFFER_MARAHNA = WRAM_START + 0x270
OFFER_NORTH = WRAM_START + 0x279

OFFERCNT_FILLMORE = WRAM_START + 0x23A
OFFERCNT_BLOOD = WRAM_START + 0x23C
OFFERCNT_KASA = WRAM_START + 0x23E
OFFERCNT_AITOS = WRAM_START + 0x240
OFFERCNT_MARAHNA = WRAM_START + 0x242
OFFERCNT_NORTH = WRAM_START + 0x244

ACTPROGRESS = WRAM_START + 0x16B18
REGIONPOP = WRAM_START + 0x21C
ORBADR = WRAM_START + 0x1A20
EVENTADR = WRAM_START + 0x19190
APRAM = WRAM_START + 0x1A00

MAGIC_INV = WRAM_START + 0x299
OFF_INV = WRAM_START + 0x2A2
LIVES = WRAM_START + 0x2AB
ARWADR =  WRAM_START + 0x1A45

ACTR_RECV_PROGRESS_ADDR = WRAM_START + 0x1A00
ACTR_SEND_ADDR = WRAM_START + 0x1A08
ACTR_FILE_NAME_ADDR = WRAM_START + 0x288
DEATH_LINK_ACTIVE_ADDR = ROM_START + 0xF8002     

GAME_CLEAR = WRAM_START + 0x347 #If 7 then game cleared

#item_queue = []

class ActraiserSNIClient(SNIClient):
    game = "Actraiser"
    patch_suffix = ".apactr"
    

    async def deathlink_kill_player(self, ctx):
        from SNIClient import DeathState, snes_buffered_write, snes_flush_writes
        
        snes_buffered_write(ctx, DEATH_SEND , bytes([0x02]))
        await snes_flush_writes(ctx)
        ctx.death_state = DeathState.dead
        ctx.last_death_link = time.time()


    async def validate_rom(self, ctx):
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read

        rom_name = await snes_read(ctx, ACTR_ROMHASH_START, ROMHASH_SIZE)
        
        #snes_logger.info(f"{rom_name}")
        if rom_name is None or rom_name == bytes([0] * ROMHASH_SIZE) or rom_name[:2] != b"AR":
            return False

        #Make sure a file is made
        
        
        ctx.game = self.game
        ctx.items_handling = 0b111  # remote items

        death_link = await snes_read(ctx, DEATH_LINK_ACTIVE_ADDR, 1)
        if death_link:
            #ctx.allow_collect = True
            await ctx.update_death_link(bool(death_link[0] & 0b1))

        ctx.rom = rom_name

        return True


    async def game_watcher(self, ctx):
        from SNIClient import DeathState, snes_buffered_write, snes_flush_writes, snes_read
        item_port = await snes_read(ctx, ACTR_SEND_ADDR, 0x1)
        death_status = await snes_read(ctx, DEATH_LOCAL , 0x1)
        #death_timer = await snes_read(ctx, DEATH_TIME , 0x1)
        goal_flag = await snes_read(ctx, GAME_CLEAR, 0x1 )
        #ctx.death_state = DeathState.alive
        actscleared = await snes_read(ctx, ACTPROGRESS, 0x12)
        regionpopulation = await snes_read(ctx, REGIONPOP, 0x12)
        apcheckram = await snes_read(ctx, APRAM + 0x10, 0x20)
        orbram = await snes_read(ctx, ORBADR, 0x6)
        eventram = await snes_read(ctx, EVENTADR, 0x40)
        arwram = await snes_read(ctx, ARWADR, 0x1)
        if ctx.server is None or ctx.slot is None:
            return
        char_name = await snes_read(ctx, ACTR_FILE_NAME_ADDR, 0x1)
        
        if char_name[0] == 0x20: 
            return

        if "DeathLink" in ctx.tags and death_status and ctx.last_death_link + 1 < time.time():

            currently_dead = death_status[0] in ACTR_DEATH_STATES
            await ctx.handle_deathlink_state(currently_dead)

        def check_locations(rom_table,location_ram_data,offset):
            checks = []
            for loc_id, loc_data in rom_table.items():
                if loc_id not in ctx.locations_checked:
                    data = location_ram_data[loc_data[0] - offset]
                    masked_data = data & (1 << loc_data[1])
                    bit_set = (masked_data != 0)
                    invert_bit = ((len(loc_data) >= 3) and loc_data[2])
                    if bit_set != invert_bit:
                        checks.append(loc_id)
            return checks
        
        def action_stage_checks(orbs, ram_data):
            checks = []
            for loc_id, loc_vals in orbs.items():
                if loc_id not in ctx.locations_checked:
                    y = 0
                    for x in range(6):
                        if ram_data[x] == loc_vals[x]:
                            y = y + 1
                        elif loc_id == 0x1C10C3 and ram_data[x] == 0x7:
                            y = y + 1
                        else:
                            break
                    if y == 6:
                        checks.append(loc_id)
                        return checks
            return checks

        # Handle Victory
        if not ctx.finished_game and goal_flag[0] == 0x7:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True

        new_checks = []
        from .rom_data import location_rom_data, item_rom_data, act_clear_rom_data, region_pop_rom_data, orb_location_data, event_flag_rom_data
        new_checks.extend(check_locations(act_clear_rom_data, actscleared, 0x16B18))
        new_checks.extend(check_locations(region_pop_rom_data, regionpopulation, 0x21C))
        new_checks.extend(check_locations(event_flag_rom_data, eventram, 0x19190))
        new_checks.extend(check_locations(location_rom_data, apcheckram, 0x1A10))
        if orbram[0] != 0:
            new_checks.extend(action_stage_checks(orb_location_data, orbram))
            snes_buffered_write(ctx, ORBADR, bytes([0x00]))
            await snes_flush_writes(ctx)

        rom = await snes_read(ctx, ACTR_ROMHASH_START, ROMHASH_SIZE)
        if rom != ctx.rom:
            ctx.rom = None
            # We have somehow loaded a different ROM
            return

        for new_check_id in new_checks:
            ctx.locations_checked.add(new_check_id)

            location = ctx.location_names.lookup_in_game(new_check_id)
            snes_logger.info(
                f'New Check: {location} ({len(ctx.locations_checked)}/{len(ctx.missing_locations) + len(ctx.checked_locations)})')
            await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [new_check_id]}])


        recv_count = await snes_read(ctx, ACTR_RECV_PROGRESS_ADDR, 1)
        recv_index = recv_count[0]

        if recv_index < len(ctx.items_received) and item_port[0] == 0:
            item = ctx.items_received[recv_index]
            recv_index += 1
            logging.info('Received %s from %s (%s) (%d/%d in list)' % (
                color(ctx.item_names.lookup_in_game(item.item), 'red', 'bold'),
                color(ctx.player_names[item.player], 'yellow'),
                ctx.location_names.lookup_in_slot(item.location, item.player), recv_index, len(ctx.items_received)))
            if recv_index > recv_count[0]:
                snes_buffered_write(ctx, ACTR_RECV_PROGRESS_ADDR, bytes([recv_index]))
            
            if item.item in item_rom_data:
                rawitem = item.item - 0x1C1000
                snes_buffered_write(ctx, ACTR_SEND_ADDR, bytes([rawitem]))


            await snes_flush_writes(ctx)

        # Arrow hotfix
        arwcnt = 1
        for item in range(len(ctx.items_received)):
            raw_item = ctx.items_received[item].item
            
            if raw_item ==0x1C101E:
                arwcnt += 1
        if arwcnt > arwram[0]:
            snes_buffered_write(ctx, ARWADR, bytes([arwcnt]))
            await snes_flush_writes(ctx)

        # Handle Collected Locations #loc_id = item code value
        for loc_id in ctx.checked_locations:
            if loc_id not in ctx.locations_checked:
                ctx.locations_checked.add(loc_id)
                #if loc_id in location_rom_data:
                 #   loc_data = location_rom_data[loc_id]
               # elif loc_id in act_clear_rom_data:
                   # loc_data = act_clear_rom_data[loc_id]
                #else:
                #ctx.locations_checked.add(loc_id)
                    #pass
                #data = await snes_read(ctx, WRAM_START + loc_data[0], 1)
                #invert_bit = ((len(loc_data) >= 3) and loc_data[2])
                #if not invert_bit:
                    #masked_data = data[0] | (1 << loc_data[1])
                    #snes_buffered_write(ctx, WRAM_START + loc_data[0], bytes([masked_data]))


                    #await snes_flush_writes(ctx)
                #else:
                    #masked_data = data[0] & ~(1 << loc_data[1])
                    #snes_buffered_write(ctx, WRAM_START + loc_data[0], bytes([masked_data]))
                    #await snes_flush_writes(ctx)
                #ctx.locations_checked.add(loc_id)

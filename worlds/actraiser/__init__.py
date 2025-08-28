from typing import List
from typing import Dict

import dataclasses
import os
import typing
import math
import threading

from .Client import ActraiserSNIClient
from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
import Utils
import Patch
import settings

from .Items import ActraiserItem, item_data_table, item_table
from .Locations import ActraiserLocation, location_data_table, location_table, locked_locations
from .Options import ActraiserOptions
from .Regions import region_data_table, get_exit
from .Rules import *
from .Rom import LocalRom, patch_rom, get_base_rom_path, ActraiserDeltaPatch, ActraiserProcedurePatch

POOLSIZE = 171

class ActraiserSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Actraiser US rom"""
        copy_to = "Actraiser.sfc"
        description = "Actraiser (US) ROM File"
        md5s = [ActraiserDeltaPatch.hash]

    rom_file: RomFile = RomFile(RomFile.copy_to)

class ActraiserWebWorld(WebWorld):
    theme = "partyTime"
    
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Actraiser.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["Happyhappyism"]
    )
    
    tutorials = [setup_en]

class ActraiserWorld(World):
    """Actraiser whose apworld code had a lot of it's base code mirrored from 
    the Majoras Mask and Donkey Kong Country 3 Apworlds."""

    game = "Actraiser"
    data_version = 1
    web = ActraiserWebWorld()
    options_dataclass = ActraiserOptions
    settings: typing.ClassVar[ActraiserSettings]
    topology_present = False
    options: ActraiserOptions
    location_name_to_id = location_table
    item_name_to_id = item_table
    act_levels = [0,1,3,5,7,9]

    def __init__(self, world: MultiWorld, player: int):
        self.rom_name_available_event = threading.Event()
        super().__init__(world, player)
        
    def generate_early(self):
        pass
    
    def create_item(self, name: str) -> ActraiserItem:
        return ActraiserItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        mw = self.multiworld
        #pool_size = POOLSIZE
        item_pool: List[ActraiserItem] = []
        item_pool_count: Dict[str, int] = {}
        
        for name, item in item_data_table.items():
            item_pool_count[name] = 0
            if item.code and item.can_create(mw, self.player):
                while item_pool_count[name] < item.num_exist:
                    item_pool.append(self.create_item(name))
                    item_pool_count[name] += 1

        if self.options.crystal_goal: 
            if self.options.max_crystal.value >= self.options.crystal_count.value:
                total_crystals = self.options.max_crystal.value
            else:
                total_crystals = self.options.crystal_count.value
            if self.options.boss_crystal:
                total_crystals = total_crystals - 6
            for x in range(total_crystals):
                item_pool.append(self.create_item("Dheim Crystal"))
                #pool_size -= 1
        if self.options.fire_sword:
            item_pool.append(self.create_item("Flame Sword"))
            #pool_size -= 1
        if self.options.arrow_count.value > 0:
            for x in range(self.options.arrow_count.value):
                item_pool.append(self.create_item("Progressive Arrow"))
                #pool_size -= 1
        for x in range(self.options.level_count.value):
            item_pool.append(self.create_item("Level Up"))
            #pool_size -= 1
        #if self.options.boss_crystal == False and self.options.goal == "death_heim":
            #pool_size -= 6
        #Deal with this later to add more filler
        unfilled_items = len(self.multiworld.get_unfilled_locations(self.player)) - len(item_pool)
        item_pool += [self.create_item(self.get_filler_item_name()) for _ in range(unfilled_items)]
        #for x in range(unfilled_items):
        #    filler_item = random.choices(filler_items, filler_weights)
        #    item_pool.append(self.create_item(filler_item[0]))

        mw.itempool += item_pool

    def create_regions(self) -> None:
        player = self.player
        mw = self.multiworld

        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, player, mw)
            mw.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = mw.get_region(region_name, player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self.options)
            }, ActraiserLocation)
            region.add_exits(region_data.connecting_regions)

        #if self.options.crystal_goal:
        #    region = mw.get_region("Sky", player)
        #    region.add_locations({"Crystal Goal":0x1C100C})
        #if self.options.population_goal:
        #    region = mw.get_region("Sky", player)
        #    region.add_locations({"Population Goal":0x1C100D})
        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self.options):
                continue

            locked_item = self.create_item(location_data_table[location_name].locked_item)
            mw.get_location(location_name, player).place_locked_item(locked_item)
        
        if self.options.boss_crystal and self.options.crystal_goal:
            mw.get_location("FMC - Minotaurus", player).place_locked_item(self.create_item("Dheim Crystal"))
            mw.get_location("BPC - Zeppelin Wolf", player).place_locked_item(self.create_item("Dheim Crystal"))
            mw.get_location("KDP - Pharaoh", player).place_locked_item(self.create_item("Dheim Crystal"))
            mw.get_location("ATV - Fire Wheel", player).place_locked_item(self.create_item("Dheim Crystal"))
            mw.get_location("MHT - Kalia", player).place_locked_item(self.create_item("Dheim Crystal"))
            mw.get_location("NWT - Arctic Wyvern", player).place_locked_item(self.create_item("Dheim Crystal"))

    def generate_output(self, output_directory: str):
        try:
            patch = ActraiserProcedurePatch(player=self.player, player_name=self.player_name)
            patch_rom(self, patch)
            self.rom_name = patch.name
            patch.write(os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}{patch.patch_file_ending}"))
        except Exception:
            raise
        finally:
            self.rom_name_available_event.set()  # make sure threading continues and errors are collected
        # try:
        #     #rom = LocalRom(get_base_rom_path())
        #     #patch_rom(self, rom, self.act_levels)


        #     rompath = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.sfc")
        #     #rom.write_to_file(rompath)
        #     #self.rom_name = rom.name

        #     #patch = ActraiserDeltaPatch(os.path.splitext(rompath)[0]+ActraiserDeltaPatch.patch_file_ending, player=self.player,
        #                            #player_name=self.multiworld.player_name[self.player], patched_path=rompath)
        #     #patch.write()
        #     #outfilepname = f"_P{self.player}"
        #     #outfilepname += f"_{self.multiworld.get_file_safe_player_name(self.player).replace(' ', '_')}"
        #     from Main import __version__
        #     self.rom_name_text = f'AR{__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}\0'
        #     self.romName = bytearray(self.rom_name_text, "utf8")[:0x20]
        #     self.romName.extend([0] * (0x20 - len(self.romName)))
            
        #     self.playerName = bytearray(self.multiworld.player_name[self.player], "utf8")[:0x20]
        #     self.playerName.extend([0] * (0x20 - len(self.playerName)))
        #     patch = ActraiserProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
        #     procedure = [("apply_tokens", ["token_data.bin"])]
        #     patch.procedure = procedure
        #     patch_rom(self, patch)
        #     self.rom_name = self.romName
        #     out_file_name = self.multiworld.get_out_file_name_base(self.player)
        #     patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))
        # except:
        #     raise
        # finally:
        #     self.rom_name_available_event.set()  # make sure threading continues and errors are collected
        #     if os.path.exists(rompath):
        #         os.unlink(rompath)

    def get_filler_item_name(self) -> str:
        filler_items = ["Apple","1UP","1000 Points","Magic", "Bomb","Fertility"]
        filler_weights =[0.8, 0.35, 0.45, 0.7, 0.15, 0.15]
        if self.options.include_traps:
            filler_items.extend(["Skull Trap","Redirect Trap"])
            filler_weights.extend([0.3, 0.4])
        junk_item = self.random.choices(filler_items,filler_weights)[0]
        return junk_item

    def modify_multidata(self, multidata: dict):
        import base64
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]
            
    def set_rules(self) -> None:
        player = self.player
        mw = self.multiworld

        #if self.options.goal == "death_heim":
        #        dh_entrance = mw.get_entrance("Sky -> Death Heim", player)
        #        dh_entrance.access_rule = lambda state: state.has("Dheim Crystal", player, self.options.crystal_count.value)
        if self.options.random_level:
            upperlevel = self.options.max_level.value - 1
            #town_index = random.shuffle([0,1,2,3,4,5])
            for x in range(1,6):
                self.act_levels[x] = random.randint(1, upperlevel)
        
        region_rules = get_region_rules(player, self.act_levels)
        for entrance_name, rule in region_rules.items():
            entrance = mw.get_entrance(entrance_name, player)
            entrance.access_rule = rule

        location_rules = get_location_rules(player, self.options.crystal_count.value)
        for location in mw.get_locations(player):
            name = location.name
            if name in location_rules and location_data_table[name].can_create(self.options):
                location.access_rule = location_rules[name]

        # Completion condition.
        if self.options.crystal_goal and self.options.population_goal:
            mw.completion_condition[player] = lambda state: state.has("Savior", player) and state.has("Prosperity", player)
        elif self.options.population_goal:
            mw.completion_condition[player] = lambda state: state.has("Prosperity", player)
        elif self.options.crystal_goal:
            mw.completion_condition[player] = lambda state: state.has("Savior", player)

    def fill_slot_data(self) -> dict:
        return {
            "lvlfillmore": self.act_levels[0],
            "lvlbloodpool": self.act_levels[1],
            "lvlkassandora": self.act_levels[2],
            "lvlaitos": self.act_levels[3],
            "lvlmarahna": self.act_levels[4],
            "lvlnorthwall": self.act_levels[5],
            "DeathLink": self.options.death_link.value
        }

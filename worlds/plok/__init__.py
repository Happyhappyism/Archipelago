from typing import List, Dict, Any

import dataclasses
import os
import typing
import math
import threading
import random

from .Client import PlokSNIClient
from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
import Patch
import settings

from .Items import PlokItem, item_data_table, item_table
from .Locations import PlokLocation, location_data_table, location_table, locked_locations, location_flea_data_table, flea_location_table
from .Options import PlokOptions
from .Regions import region_data_table, get_exit
from .Rules import *
from .Rom import LocalRom, patch_rom, get_base_rom_path, PlokDeltaPatch

class PlokSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Plok US rom"""
        copy_to = "Plok.sfc"
        description = "Plok (US) ROM File"
        md5s = [PlokDeltaPatch.hash]

    rom_file: RomFile = RomFile(RomFile.copy_to)

class PlokWebWorld(WebWorld):
    theme = "partyTime"
    
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Plok.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["Cultist"]
    )
    
    tutorials = [setup_en]

class PlokWorld(World):
    """Plok whose apworld code is completely stolen from Majoras Masks apworld."""

    game = "Plok"
    data_version = 1
    web = PlokWebWorld()
    options_dataclass = PlokOptions
    settings: typing.ClassVar[PlokSettings]
    topology_present = False
    options: PlokOptions
    location_name_to_id = location_table
    location_name_to_id.update(flea_location_table)
    item_name_to_id = item_table

    def __init__(self, world: MultiWorld, player: int):
        self.rom_name_available_event = threading.Event()
        super().__init__(world, player)
        
    def generate_early(self):
        pass
    
    def create_item(self, name: str) -> PlokItem:
        return PlokItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        mw = self.multiworld

        item_pool: List[PlokItem] = []
        item_pool_count: Dict[str, int] = {}
        for name, item in item_data_table.items():
            item_pool_count[name] = 0
            if item.code and item.can_create(mw, self.player):
                while item_pool_count[name] < item.num_exist:
                    item_pool.append(self.create_item(name))
                    item_pool_count[name] += 1

        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(item_pool)
        item_pool += [self.create_item(self.get_filler_item_name()) for _ in range(junk)]
        mw.itempool += item_pool

        #mw.push_precollected(self.create_item("Ocarina of Time"))
        #mw.push_precollected(self.create_item("Song of Time"))
        #mw.push_precollected(self.create_item("Progressive Sword"))

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
                if location_data.region == region_name and location_data.can_create(mw, player)
            }, PlokLocation)
            

            if self.options.fleasanity:
                region.add_locations({
                location_name: location_data.address for location_name, location_data in location_flea_data_table.items()
                if location_data.region == region_name and location_data.can_create(mw, player)
            }, PlokLocation)
                
            region.add_exits(region_data.connecting_regions)

        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(mw, player):
                continue

            locked_item = self.create_item(location_data_table[location_name].locked_item)
            mw.get_location(location_name, player).place_locked_item(locked_item)

    

    def generate_output(self, output_directory: str):
        try:
            rom = LocalRom(get_base_rom_path())
            patch_rom(self, rom)

            #self.active_level_list.append(LocationName.rocket_rush_region)

            rompath = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.sfc")
            rom.write_to_file(rompath)
            self.rom_name = rom.name

            patch = PlokDeltaPatch(os.path.splitext(rompath)[0]+PlokDeltaPatch.patch_file_ending, player=self.player,
                                   player_name=self.multiworld.player_name[self.player], patched_path=rompath)
            patch.write()
        except:
            raise
        finally:
            self.rom_name_available_event.set()  # make sure threading continues and errors are collected
            if os.path.exists(rompath):
                os.unlink(rompath)

    def get_filler_item_name(self) -> str:
        filler_items = ["Shells","Extra Plife","Fruit","Force Field","Rage",
                        #"Unicycle Rental", "Car Rental", "Jet Rental", "Motorcycle Rental",
                        #"Helicopter Rental", "Tank Rental", "UFO Rental", "Springs Rental",
                        "Boxing Glove Rental", "Rocket Rental", "Musket Rental",
                        "Flamethrower Rental","Sheriff Badge Rental"]
        filler_weights = [0.3,0.2,0.3,0.5,0.3,
                          #0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,
                          0.2,0.2,0.2,0.2,0.2]
        #if self.options.include_traps:
        #    filler_items.extend(["Stun Trap","Panic Bomb Trap","Fire Trap","Reverse Trap"])
        #    filler_weights.extend([0.3,0.4,0.3,0.4])
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

        region_rules = get_region_rules(player)
        for entrance_name, rule in region_rules.items():
            entrance = mw.get_entrance(entrance_name, player)
            entrance.access_rule = rule

        queen_item_cnt = self.options.queen_items.value
        location_rules = get_location_rules(player, queen_item_cnt)
        for location in mw.get_locations(player):
            name = location.name
            if name in location_rules and location_data_table[name].can_create(mw, player):
                location.access_rule = location_rules[name]

        # Completion condition.
        mw.completion_condition[player] = lambda state: state.has("Flea Queen Dead", player)

    def fill_slot_data(self) -> dict:
        return {
            "DeathLink": self.options.death_link.value
        }
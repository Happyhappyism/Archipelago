from typing import List, Dict, Any, ClassVar

from BaseClasses import Region, Tutorial, MultiWorld, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import BomberTItem, item_data_table, item_table
from .Locations import BomberTLocation, location_data_table, location_table, locked_locations, rock_location_data_table, rock_location_table
from .mapsanity import *
from .Options import BomberTOptions
from .Regions import region_data_table
from .Rules import *
from .Rom import MD5Hash, BomberTProcedurePatch, write_tokens
from .Rom import get_base_rom_path as get_base_rom_path
from .Client import BomberTClient

import Utils
import dataclasses
import typing
import random
import os
import pkgutil
import Patch
import settings

class BomberTSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Tournament US rom"""
        copy_to = "BombermanTournament.gba"
        description = "Bomberman Tournament (US) ROM File"
        md5s = [MD5Hash]

    rom_file: RomFile = RomFile(RomFile.copy_to)

class BomberTWebWorld(WebWorld):
    theme = "partyTime"
    
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Bomberman Tournament.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["Happyhappyism"]
    )
    
    tutorials = [setup_en]


class BomberTWorld(World):
    """The greatest game of all time."""

    game = "Bomberman Tournament"
    data_version = 1
    web = BomberTWebWorld()
    options: BomberTOptions
    settings: ClassVar[BomberTSettings]
    topology_present = False
    options_dataclass = BomberTOptions
    settings_key = "bombermantournament_settings"
    location_name_to_id = location_table
    location_name_to_id.update(rock_location_table)
    location_name_to_id.update(map_location_table)
    item_name_to_id = item_table

    fusion_dict = {}

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)

    def create_item(self, name: str) -> BomberTItem:
        return BomberTItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[BomberTItem] = []
        
        if self.options.random_fuse.value:
            from .Items import kara_hints
            karalist = kara_hints
            self.random.shuffle(karalist)
            fuse_items = ["Beta - Fuse Fangs", "Beta - Fuse Sea", "Beta - Fuse Dragon", "Beta - Fuse SeaWing"]
            for x in range(4):
                kara1 = karalist.pop()
                kara2 = karalist.pop()
                self.fusion_dict.update({fuse_items[x]: [kara1, kara2]})
        else:
            self.fusion_dict = {
                "Beta - Fuse Fangs": ["Pommy", "Elifan"],
                "Beta - Fuse Sea": ["Kai-man", "P Nucklz"],
                "Beta - Fuse Dragon": ["P Beast", "Dorako"],
                "Beta - Fuse SeaWing": ["Youni", "Youno"]
            }

        for name, item in item_data_table.items():
            if item.code and item.can_create(self):
                for x in range(item.num_exist):
                    item_pool.append(self.create_item(name))

        if self.options.pool_medals:
            item_pool.append(self.create_item("Medal of Bravery"))
            item_pool.append(self.create_item("Medal of Justice"))
            item_pool.append(self.create_item("Medal of Love"))
            item_pool.append(self.create_item("Medal of Friendship"))
        if self.options.zone_navigation == 1:
            item_pool.append(self.create_item("Zone Key"))
            item_pool.append(self.create_item("Zone Key"))
            item_pool.append(self.create_item("Zone Key"))
        elif self.options.zone_navigation == 2:
            self.multiworld.push_precollected(self.create_item("Magnet Door Key"))
            self.multiworld.push_precollected(self.create_item("Boat Key"))
            self.multiworld.push_precollected(self.create_item("Desert Key"))
        if self.options.random_fuse.value == 2:
            item_pool.append(self.create_item("P Fangs"))
            item_pool.append(self.create_item("P Sea"))
            item_pool.append(self.create_item("P Dragon"))
            item_pool.append(self.create_item("SeaWing"))

        self.multiworld.push_precollected(self.create_item("Pommy"))
        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(item_pool)
        item_pool += [self.create_item(self.get_filler_item_name()) for _ in range(junk)]
        
        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.code for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, BomberTLocation)
            
            if self.options.rocksanity:
                region.add_locations({
                location_name: location_data.code for location_name, location_data in rock_location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, BomberTLocation)
                
            if self.options.mapsanity:
                region.add_locations({
                location_name: location_data.code for location_name, location_data in loc_map_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
                }, BomberTLocation)
                
            region.add_exits(region_data.connecting_regions)

        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self):
                continue
            #if location_data.type == "map" and self.options.mapsanity == False:
            #    continue
            #if location_data.type == "rock" and self.options.rocksanity == False:
            #    continue
            locked_item = self.create_item(location_data_table[location_name].locked_item)
            self.get_location(location_name).place_locked_item(locked_item)
        powerup_names = ["Health", "BombUp","FireUp"]
        self.get_location("Colosseum Streak").place_locked_item(self.create_item(self.random.choice(powerup_names)))
        if self.options.pool_medals == False:
            self.get_location("Magnet - Magnet Bomber Defeated").place_locked_item(self.create_item("Medal of Bravery"))
            self.get_location("Pretty - Pretty Bomber Defeated").place_locked_item(self.create_item("Medal of Justice"))
            self.get_location("Plasma - Plasma Bomber Defeated").place_locked_item(self.create_item("Medal of Love"))
            self.get_location("Golem - Golem Bomber Defeated").place_locked_item(self.create_item("Medal of Friendship"))
        if self.options.zone_navigation == 0:
            self.get_location("Magnet - Magnet Clear").place_locked_item(self.create_item("Magnet Door Key"))
            self.get_location("Pretty - Pretty Clear").place_locked_item(self.create_item("Boat Key"))
            self.get_location("Plasma - Plasma Clear").place_locked_item(self.create_item("Desert Key"))
        if self.options.random_fuse.value != 2:
            self.get_location("Beta - Fuse Fangs").place_locked_item(self.create_item("P Fangs"))
            self.get_location("Beta - Fuse Sea").place_locked_item(self.create_item("P Sea"))
            self.get_location("Beta - Fuse Dragon").place_locked_item(self.create_item("P Dragon"))
            self.get_location("Beta - Fuse SeaWing").place_locked_item(self.create_item("SeaWing"))
        # Set priority location for the Big Red Button!
        #self.options.priority_locations.value.add("The Big Red Button")

        #unfilled = self.get_unfilled_locations(world.player)
    def get_filler_item_name(self) -> str:
        filler_items = ["Small Medicine","Large Medicine","50 Gold","100 Gold"]
        filler_weights = [0.9, 0.2, 0.7,0.4]
        junk_item = self.random.choices(filler_items,filler_weights)[0]
        return junk_item

    #def modify_multidata(self, multidata: dict):
    #    import base64
    #    # wait for self.rom_name to be available.
    #    self.rom_name_available_event.wait()
    #    rom_name = getattr(self, "rom_name", None)
    #    # we skip in case of error, so that the original error in the output thread is the one that gets raised
    #    if rom_name:
    #        new_name = base64.b64encode(bytes(self.rom_name)).decode()
    #        multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    def set_rules(self) -> None:
        player = self.player
        region_rules = get_region_rules(player)

        for entrance_name, rule in region_rules.items():
            entrance = self.multiworld.get_entrance(entrance_name, player)
            entrance.access_rule = rule

        location_rules = get_location_rules(player)
        for location in self.multiworld.get_locations(player):
            name = location.name
            #if name in location_rules and location_data_table[name].can_create(self.multiworld, player):
            if name in location_rules:
                location.access_rule = location_rules[name]
        location_rules = fusion_rules(player,self.fusion_dict)
        for location in self.multiworld.get_locations(player):
            name = location.name
            if name in location_rules:
                location.access_rule = location_rules[name]
        # Completion condition.
        self.multiworld.completion_condition[self.player] = lambda state: state.has("MAX", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "DeathLink": self.options.death_link.value
        }

    def generate_output(self, output_directory: str):
        outfilepname = f"_P{self.player}"
        outfilepname += f"_{self.multiworld.get_file_safe_player_name(self.player).replace(' ', '_')}"
        self.rom_name_text = f'BombT{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}\0'
        self.romName = bytearray(self.rom_name_text, "utf8")[:0x20]
        self.romName.extend([0] * (0x20 - len(self.romName)))
        self.rom_name = self.romName
        self.playerName = bytearray(self.multiworld.player_name[self.player], "utf8")[:0x20]
        self.playerName.extend([0] * (0x20 - len(self.playerName)))
        patch = BomberTProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
        patch.write_file("base_patch.bsdiff4", pkgutil.get_data(__name__, "bombt.bsdiff4"))
        procedure = [("apply_bsdiff4", ["base_patch.bsdiff4"]), ("apply_tokens", ["token_data.bin"])]
        patch.procedure = procedure
        write_tokens(self, patch, self.fusion_dict)
        out_file_name = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))
        
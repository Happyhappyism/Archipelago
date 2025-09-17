from typing import List, Dict, Any, ClassVar

from BaseClasses import Region, Tutorial, MultiWorld, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import HamGamesItem, item_data_table, item_table, item_filler, item_filler_weight
from .Locations import HamGamesLocation, location_data_table, location_table, locked_locations
from .talksanity import talk_location_table, loc_talk_data_table
from .seedsanity import seed_location_table, loc_seed_data_table
from .costumesanity import costume_location_table, loc_costume_data_table
from .Options import HamGamesOptions
from .Regions import region_data_table
from .Rules import *
from .Rom import MD5Hash, HamGamesProcedurePatch, write_tokens
from .Rom import get_base_rom_path as get_base_rom_path
from .Client import HamGamesClient

import Utils
import dataclasses
import typing
import random
import os
import pkgutil
import Patch
import settings
import math

class HamGamesSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Hamtaro Hamham Games US rom"""
        copy_to = "hamtaro_hamhamgames.gba"
        description = "Hamtaro Ham-Ham Games (US) ROM File"
        md5s = MD5Hash

    rom_file: RomFile = RomFile(RomFile.copy_to)

class HamGamesWebWorld(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Hamtaro Hamham Games.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["Happymhappyism"]
    )

    tutorials = [setup_en]

class HamGamesWorld(World):
    """The GBA version of Hamtaro Hamham Games."""

    game = "Hamtaro Hamham Games"
    data_version = 1
    web = HamGamesWebWorld()
    options_dataclass = HamGamesOptions
    settings: ClassVar[HamGamesSettings]
    topology_present = False
    settings_key = "hamgames_settings"
    options: HamGamesOptions
    location_name_to_id = location_table
    location_name_to_id.update(talk_location_table)
    location_name_to_id.update(seed_location_table)
    location_name_to_id.update(costume_location_table)
    item_name_to_id = item_table
    fortune_area = random.randint(0xAB,0xB7)


    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)

    def create_item(self, name: str) -> HamGamesItem:
        return HamGamesItem(name, item_data_table[name].type, item_data_table[name].code, self.player)
    
    def create_items(self) -> None:
        item_pool: List[HamGamesItem] = []
        max_nomination = self.options.max_nomination.value
        for x in range(max_nomination):
            item_pool.append(self.create_item("Marathon Nomination"))
        for name, item in item_data_table.items():
                if item.code and item.can_create(self):
                    for x in range(item.num_exist):
                        item_pool.append(self.create_item(name))
        self.get_location("Day 7 Stadium - Marathon").place_locked_item(self.create_item("Hamham Games Trophy"))

        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(item_pool)
        item_pool += [self.create_item(self.get_filler_item_name()) for _ in range(junk)]
        
        self.multiworld.push_precollected(self.create_item("Stadium Pass"))
        if self.options.starthamigo:
            self.multiworld.push_precollected(self.create_item("Hamigo File"))
        
        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, region_data in region_data_table.items():
            
            #if region_name in self.included_stages or region_name in fixed_regions:
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, HamGamesLocation)
            
            #if self.options.talksanity:
            #    region.add_locations({
            #    location_name: location_data.address for location_name, location_data in loc_talk_data_table.items()
            #    if location_data.region == region_name and location_data.can_create(self)
            #}, HamGamesLocation)
                
            if self.options.seedsanity:
                region.add_locations({
                location_name: location_data.address for location_name, location_data in loc_seed_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, HamGamesLocation)
                
            if self.options.costumesanity:
                region.add_locations({
                location_name: location_data.address for location_name, location_data in loc_costume_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, HamGamesLocation)
                
            region.add_exits(region_data_table[region_name].connecting_regions)

    
    def get_filler_item_name(self) -> str:
        junk_item = self.random.choices(item_filler,item_filler_weight)[0]
        return junk_item
    
    def set_rules(self) -> None:
        #area_pick = random.randint(0)
        player = self.player
        region_rules = get_region_rules(player,self.fortune_area)

        for entrance_name, rule in region_rules.items():
            entrance = self.multiworld.get_entrance(entrance_name, player)
            entrance.access_rule = rule

        location_rules = get_location_rules(player)

        for location in self.multiworld.get_locations(player):
            name = location.name
            #if name in location_rules and location_data_table[name].can_create(self.multiworld, player):
            if name in location_rules:
                location.access_rule = location_rules[name]

            if self.options.game_goal.value == 1:
                self.multiworld.completion_condition[self.player] = (
                    lambda state: state.has("Hamham Games Trophy", self.player) and state.has("Marathon Nomination",self.player, self.options.needed_nomination.value)
                )
            elif self.options.game_goal.value == 2:
                 self.multiworld.completion_condition[self.player] = (
                    lambda state: state.can_reach_location("Hamigo 7 - Prince Bo", self.player)
                )

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "DeathLink": self.options.death_link.value
        }
    
    def generate_output(self, output_directory: str):
        outfilepname = f"_P{self.player}"
        outfilepname += f"_{self.multiworld.get_file_safe_player_name(self.player).replace(' ', '_')}"
        self.rom_name_text = f'HHG{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}\0'
        self.romName = bytearray(self.rom_name_text, "utf8")[:0x20]
        self.romName.extend([0] * (0x20 - len(self.romName)))
        self.rom_name = self.romName
        self.playerName = bytearray(self.multiworld.player_name[self.player], "utf8")[:0x20]
        self.playerName.extend([0] * (0x20 - len(self.playerName)))
        patch = HamGamesProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
        #patch.write_file("base_patch.bsdiff4", pkgutil.get_data(__name__, "bombt.bsdiff4"))
        #procedure = [("apply_bsdiff4", ["base_patch.bsdiff4"]), ("apply_tokens", ["token_data.bin"])]
        procedure = [("apply_tokens", ["token_data.bin"])]
        patch.procedure = procedure
        write_tokens(self, patch)
        out_file_name = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))
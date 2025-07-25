from typing import List, Dict, Any, ClassVar

from BaseClasses import Region, Tutorial, MultiWorld, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import PokePinballItem, item_data_table, item_table, item_filler, item_filler_weight
from .Locations import PokePinballLocation, location_data_table, location_table, locked_locations, pokemon_names
from .Options import PokePinballOptions
from .Regions import region_data_table
from .Rules import *
from .Rom import MD5Hash, PokePinballProcedurePatch, write_tokens
from .Rom import get_base_rom_path as get_base_rom_path
from .Client import PokePinballClient

import Utils
import dataclasses
import typing
import random
import os
import pkgutil
import Patch
import settings
import math

class PokePinballSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Pokemon Pinball Color US rom"""
        copy_to = "PokemonPinball.gbc"
        description = "Pokemon Pinball (US) ROM File"
        md5s = [MD5Hash]

    rom_file: RomFile = RomFile(RomFile.copy_to)

class PokePinballWebWorld(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Pokemon Pinball.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["Cultist"]
    )

    tutorials = [setup_en]

class PokePinballWorld(World):
    """The Gameboy Color version of Pokemon Pinball."""

    game = "Pokemon Pinball"
    data_version = 1
    web = PokePinballWebWorld()
    options_dataclass = PokePinballOptions
    settings: ClassVar[PokePinballSettings]
    topology_present = False
    settings_key = "pokepinball_settings"
    options: PokePinballOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)

    def create_item(self, name: str) -> PokePinballItem:
        return PokePinballItem(name, item_data_table[name].type, item_data_table[name].code, self.player)
    
    def create_items(self) -> None:
        item_pool: List[PokePinballItem] = []

        for name, item in item_data_table.items():
                if item.code and item.can_create(self):# and (name in self.included_stages):
                    for x in range(item.num_exist):
                        item_pool.append(self.create_item(name))
        if self.options.extra_start_route:
            from .Items import route_list
            routes = route_list
            random.shuffle(routes)
            self.multiworld.push_precollected(self.create_item(routes[0]))
        if self.options.include_notes:
            note_count = math.ceil(self.options.dex_needed.value/10)
            for x in range(note_count):
                item_pool.append(self.create_item("Oaks Notes"))
        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(item_pool)
        item_pool += [self.create_item(self.get_filler_item_name()) for _ in range(junk)]
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
                if location_data.region == region_name and location_data.can_create(self)# and (region_name in self.included_stages or region_name in fixed_regions)
            }, PokePinballLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

    
    def get_filler_item_name(self) -> str:
        junk_item = random.choices(item_filler,item_filler_weight)[0]
        return junk_item
    
    def set_rules(self) -> None:
        player = self.player
        region_rules = get_region_rules(player, self.options)

        for entrance_name, rule in region_rules.items():
            entrance = self.multiworld.get_entrance(entrance_name, player)
            entrance.access_rule = rule

        location_rules = get_location_rules(player, self.options.dex_needed.value)

        for location in self.multiworld.get_locations(player):
            name = location.name
            #if name in location_rules and location_data_table[name].can_create(self.multiworld, player):
            if name in location_rules:
                location.access_rule = location_rules[name]

        #for location_name, location_data in locked_locations.items():
        #    # Ignore locations we never created.
        #    if not location_data.can_create(self):
        #        continue
        #    
        #    locked_item = self.create_item(location_data_table[location_name].locked_item)
        #    self.get_location(location_name).place_locked_item(locked_item)
        #self.get_location("Pokedex Completed").place_locked_item(self.create_item("Victory"))

        #if self.options.required_mons.value:
        #self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location("Pokedex Completed", player) and [state.can_reach_region(x, player) for x in self.options.required_mons.value]
        if self.options.required_mons.value:
            self.multiworld.completion_condition[self.player] = (
                lambda state: 
                (sum([state.can_reach_location(x, player) for x in pokemon_names]) >= self.options.dex_needed.value) 
                and 
                (sum([state.can_reach_location(x, player) for x in self.options.required_mons.value]) >= len(self.options.required_mons.value))
            )
        else:
            self.multiworld.completion_condition[self.player] = (
            lambda state: (sum([state.can_reach_location(x, player) for x in pokemon_names]) >= self.options.dex_needed.value) )

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "DeathLink": self.options.death_link.value
        }
    
    def generate_output(self, output_directory: str):
        outfilepname = f"_P{self.player}"
        outfilepname += f"_{self.multiworld.get_file_safe_player_name(self.player).replace(' ', '_')}"
        self.rom_name_text = f'B64{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}\0'
        self.romName = bytearray(self.rom_name_text, "utf8")[:0x20]
        self.romName.extend([0] * (0x20 - len(self.romName)))
        self.rom_name = self.romName
        self.playerName = bytearray(self.multiworld.player_name[self.player], "utf8")[:0x20]
        self.playerName.extend([0] * (0x20 - len(self.playerName)))
        patch = PokePinballProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
        #patch.write_file("base_patch.bsdiff4", pkgutil.get_data(__name__, "bombt.bsdiff4"))
        #procedure = [("apply_bsdiff4", ["base_patch.bsdiff4"]), ("apply_tokens", ["token_data.bin"])]
        procedure = [("apply_tokens", ["token_data.bin"])]
        patch.procedure = procedure
        write_tokens(self, patch)
        out_file_name = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))
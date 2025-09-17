from typing import Callable, Dict

from worlds.AutoWorld import LogicMixin, World
from BaseClasses import CollectionState, MultiWorld

def has_key_miracles(state, player):
    return state.has("Lightning", player) and state.has("Sun", player) and state.has("Rain",player) and state.has("Wind",player)

def has_all_key_items(state, player):
    return state.has("Loaf of Bread", player) and state.has("Wheat", player) and state.has("Herb", player) and state.has("Bridge", player) and state.has("Music", player) and state.has("Magic Skull", player) and state.has("Fleece", player)

def can_use_quake(state, player):
    return state.has("Earthquake", player) and state.has("Level Up", player, 7)

def can_reach_region_count(state, player, regcount):
    return (sum(
        (state.can_reach_region("Fillmore Forest", player),
        state.can_reach_region("Bloodpool Bridge", player),
        state.can_reach_region("Kasandora Desert", player),
        state.can_reach_region("Aitos Mountain", player),
        state.can_reach_region("Marahna Swamp", player),
        state.can_reach_region("Northwall Cave", player),)
    ) >= regcount)


def has_max_civ(state, player):
    return state.has("Fillmore Advancement", player ,2) and state.has("Bloodpool Advancement", player,2) and state.has("Kasandora Advancement", player,2) and state.has("Aitos Advancement", player,2) and state.has("Marahna Advancement", player,2) and state.has("Northwall Advancement", player,2) 

def get_region_rules(player, act_levels):
    return {
        "Sky -> Fillmore Forest":
            lambda state: state.has("Level Up", player, act_levels[0]),
        "Fillmore -> Fillmore Chasm":
            lambda state: state.has("Lightning", player),

        "Sky -> Bloodpool Bridge":
            lambda state: state.has("Level Up", player, act_levels[1]),
        "Bloodpool Bridge -> Bloodpool":
            lambda state: state.has("Loaf of Bread", player),
        "Bloodpool -> Bloodpool Castle":
            lambda state: state.has("Lightning", player) and state.has("Bridge", player) and state.has("Magic Skull", player) and state.has("Sun", player),
        

        "Sky -> Kasandora Desert":
            lambda state: state.has("Level Up", player, act_levels[2]),
        "Kasandora Desert -> Kasandora":
            lambda state: state.has("Rain", player),
        #"Kasandora -> Kasandora Pyramid":
        #    lambda state: state.has("Rain", player),
        

        "Sky -> Aitos Mountain":
            lambda state: state.has("Level Up", player, act_levels[3]),
        "Aitos Mountain -> Aitos":
            lambda state: state.has("Lightning", player) and state.has("Wind", player), 
        # Wind so that you don't softlock from building a windmill too early.
        #"Aitos -> Aitos Volcano":
        #    lambda state: state.has("Lightning", player),
        

        "Sky -> Marahna Swamp":
            lambda state: state.has("Level Up", player, act_levels[4]),
        "Marahna Swamp -> Marahna":
            lambda state: state.has("Lightning", player),
        "Marahna -> Marahna Temple":
            lambda state: can_use_quake(state, player) and state.has("Sun", player),

        "Sky -> Northwall Cave":
            lambda state: state.has("Level Up", player, act_levels[5]),
        "Northwall Cave -> Northwall":
            lambda state: state.has("Sun", player) and state.has("Fleece", player),
        #"Northwall -> Northwall Tree":
        #    lambda state: state.has("Fleece", player),
        #"Sky -> Death Heim":
        #    lambda state: state.has("Dheim Crystal", player, 6)
        #Sky -> Death Heim":
        #    lambda state: state.has("Dheim Crystal", player, world.options.crystal_count)
        
    }

def get_location_rules(player, crystal_needed):
    return {
        #The level up logic could use some looseing up but this is to keep too many progression items from spawning in the level up pool, logic for it is too complex right now
        "SK - Level 3":
            lambda state: state.has("Lightning", player) or state.has("Level Up", player),
        "SK - Level 4":
            lambda state: state.has("Lightning", player) and state.has("Level Up", player) ,
        "SK - Level 5":
            lambda state: state.has("Lightning", player) and state.has("Bridge", player) and can_reach_region_count(state, player, 2),
        "SK - Level 6":
            lambda state: has_key_miracles(state, player) and state.has("Bridge", player) and can_reach_region_count(state, player, 3),
        "SK - Level 7":
            lambda state: has_key_miracles(state, player) and state.has("Bridge", player) and can_reach_region_count(state, player, 3),
        "SK - Level 8":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 4),
        "SK - Level 9":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 4),
        "SK - Level 10":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 5),
        "SK - Level 11":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 5),
        "SK - Level 12":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 6),
        "SK - Level 13":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 6),
        "SK - Level 14":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 6) and has_max_civ(state, player) and state.has("Earthquake",player),
        "SK - Level 15":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 6) and has_max_civ(state, player) and state.has("Earthquake",player),
        "SK - Level 16":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 6) and has_max_civ(state, player) and state.has("Earthquake",player),
        "SK - Level 17":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 6) and has_max_civ(state, player) and state.has("Earthquake",player),
            
        #"FM - Act 2 Clear":
        #    lambda state: state.has("Lightning", player),
        "FM - Population 256":
            lambda state: state.has("Lightning", player),
        "FM - Population 512":
            lambda state: state.has("Lightning", player) and state.has("Fillmore Advancement", player),
        "FM - Max Population":
            lambda state: state.has("Lightning", player) and state.has("Fillmore Advancement", player, 2) and state.has("Wheat", player),
        "FM - Bridge":
            lambda state: state.has("Lightning", player),
        "FM - Magical Fire":
            lambda state: state.has("Lightning", player),
        "FM - Strength of Angel":
            lambda state: state.has("Lightning", player),
        "FM - Source of Magic":
            lambda state: state.has("Lightning", player),
        "FM - Source of Life":
            lambda state: state.has("Compass", player) and state.has("Lightning", player),
        "FM - Advancement 2":
            lambda state: state.has("Lightning", player),
        
        "BP - Population 256":
            lambda state: state.has("Sun", player) and state.has("Bridge",player),
        "BP - Population 512":
            lambda state: state.has("Bloodpool Advancement", player) and state.has("Music", player)  and state.has("Sun", player) and state.has("Magic Skull", player)  and state.has("Lightning",player) and state.has("Bridge",player),
        "BP - Max Population":
            lambda state: state.has("Bloodpool Advancement", player, 2) and state.has("Music", player)  and state.has("Sun", player) and state.has("Magic Skull", player) and state.has("Wheat", player) and state.has("Lightning",player) and state.has("Bridge",player),
        "BP - Magic Skull":
            lambda state: state.has("Bridge", player) and state.has("Sun", player),
        "BP - Magical Stardust":
            lambda state: state.has("Lightning",player) and state.has("Magic Skull", player),
        "BP - Advancement 1":
            lambda state: state.has("Lightning",player) or state.has("Sun", player) and state.has("Bridge", player),
        "BP - Bomb":
            lambda state: state.has("Sun", player) and state.has("Bridge", player),
        "BP - Source of Magic":
            lambda state: state.has("Magic Skull", player) and state.has("Sun", player) and state.has("Bridge", player),
        "BP - Source of Life":
            lambda state: state.has("Rain", player),
        "BP - Compass":
            lambda state: state.has("Lightning",player) and state.has("Music", player) and state.has("Magic Skull", player)  and state.has("Sun", player) and state.has("Bridge", player),
        "BP - Advancement 2":
            lambda state: state.has("Sun", player) and state.has("Bridge", player) and state.has("Lightning",player),
        "BP - Bread":
            lambda state: state.has("Lightning",player) and state.has("Bridge", player) and state.has("Sun", player),
        "BP - Wheat":
            lambda state: state.has("Lightning",player),
        "BP - Calmed Citizens":
            lambda state: state.has("Lightning", player) and state.has("Bridge", player) and state.has("Magic Skull", player) and state.has("Sun", player) and state.has("Bloodpool Advancement", player, 2) and state.has("Music"),


        "KD - Population 512":
            lambda state: state.has("Herb", player) and state.has("Kasandora Advancement", player),
        "KD - Max Population":
            lambda state: state.has("Herb", player) and state.has("Kasandora Advancement", player, 2) and state.has("Wheat", player),
        "KD - Source of Life":
            lambda state: can_use_quake(state, player),
        "KD - Ancient Tablet":
            lambda state: state.has("Herb", player) and state.has("Kasandora Advancement", player, 2),
        "KD - Cured Plague":
            lambda state: state.has("Herb", player),

        "AT - Population 512":
            lambda state: state.has("Aitos Advancement", player),
        "AT - Max Population":
            lambda state: state.has("Aitos Advancement", player, 2),
        #"AT - Fleece":
        #    lambda state: state.has("Wind", player),
        #"AT - Source of Magic":
        #    lambda state: state.has("Wind", player),



        #"MH - Act 2 Clear":
        #    lambda state: state.has("Ancient Tablet", player), 
        "MH - Herb":
            lambda state: can_use_quake(state, player) and state.has("Sun", player),
        "MH - Bomb":
            lambda state: state.has("Sun", player),
        "MH - Source of Magic":
            lambda state: state.has("Compass", player),
        "MH - Advancement 1":
            lambda state: can_use_quake(state, player) or  state.has("Sun", player),
        "MH - Advancement 2":
            lambda state: can_use_quake(state, player) and  state.has("Sun", player),
        "MH - Magical Aura":
            lambda state: state.has("Ancient Tablet", player) and can_use_quake(state, player) and state.has("Sun", player),
        "MH - Population 256":
            lambda state: state.has("Sun", player) and (can_use_quake(state, player) or state.has ("Marahna Advancement", player)), 
        "MH - Max Population":
            lambda state: state.has("Marahna Advancement", player, 2) and state.has("Sun", player) and can_use_quake(state, player) and state.has("Wheat", player),

        #"NW - Bomb":
        #    lambda state: state.has("Fleece", player),
        #"NW - Population 64":
        #    lambda state: state.has("Fleece", player),
        #"NW - Population 128":
        #    lambda state: state.has("Fleece", player),
        #"NW - Population 256":
        #    lambda state: state.has("Fleece", player),
        "NW - Population 512":
            lambda state: state.has("Northwall Advancement", player, 2),
        "NW - Max Population":
            lambda state: state.has("Northwall Advancement", player,2) and state.has("Wheat", player),
        #"NW - Warm Clothes":
        #    lambda state: state.has("Fleece", player),
        #"NW - Advancement 1":
        #    lambda state: state.has("Fleece", player),
        #"NW - Advancement 2":
        #    lambda state: state.has("Fleece", player),
        #"NW - Bomb":
        #    lambda state: state.has("Fleece", player),
        #"NW - Strength of Angel":
        #    lambda state: state.has("Fleece", player),
        "NW - Source of Life":
            lambda state: state.has("Lightning", player),

        "Crystal Goal":
            lambda state: state.has("Dheim Crystal", player, crystal_needed),
        "Population Goal":
            lambda state: has_key_miracles(state, player) and has_all_key_items(state, player) and can_reach_region_count(state, player, 6) and has_max_civ(state, player),

    }
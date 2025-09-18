from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState

from .Items import kara_hints

import logging
logger = logging.getLogger("Bomberman Tournament")

if TYPE_CHECKING:
    from . import BomberTWorld

# FUSE_KARAS = [
#     "Pommy",
#     "Ceedrun",
#     "Elifan",
#     #"Fangs",
#     "Sharkun",
#     "Th Liger",
#     "Kai-man",
#     "TwinDrag",
#     "P Nucklz",
#     #"P Sea",
#     "ToughGuy",
#     "P Beast",
#     "Pteradon",
#     "Dorako",
#     #"P Dragon",
#     "Youno",
#     "Sibaloon",
#     "P Animal",
#     "Unagi",
#     "Elekong",
#     "Youni",
#     #"Seawing",
#     "KameKing",
#     "MarinGon",
#     "Firekong",
# ]

def plasma_clear_rules(state, player):
    return state.has("Dorako", player) and state.has("Sharkun", player) and state.has("Elifan", player) and  state.has("ToughGuy", player)

def fantasy_clear_rules(state, player):
    return state.has("ToughGuy", player) and state.has("Elifan", player) and state.has("Sibaloon", player),

def general_sid_rules(state,player):
    return (
        (state.has("Pommy", player) and state.has("Elifan", player)) or
        (state.has("Kai-man", player) and state.has("P Nucklz", player)) and (state.has("RC Bomb", player) or state.has("ToughGuy", player) or (state.has("TwinDrag", player) or state.has("FireUp",player, 2))) or
        (plasma_clear_rules(state, player) and state.has("P Beast", player)) or
        (state.has("Youno", player) and state.has("Youni", player))
    )

# def fusion_rules(player, fusedict):
#     return {
#         # Fusions
#         }

def get_region_rules(player):
    
    return{
        "Alpha -> Plains":
            lambda state: state.has("Pommy", player),
        "ShuraRd -> Beta":
            lambda state: state.has("Ceedrun", player),

        #"B Valley -> ToPlain":
        #    lambda state: (state.has("Elifan", player) and state.has("P Fangs", player)) or state.has("Magnet Door Key", player),
        "B Valley -> ToPlain":
            lambda state: state.has("Magnet Door Key", player) or state.has("Zone Key", player),
        "Gamma -> Delta":
            lambda state: state.has("Sharkun", player),
        "HighMt -> LiteCave":
            lambda state: state.has("Sharkun", player) and state.has("Elifan", player),
        "S Forest -> BigOcean":
            lambda state: state.has("Kai-man", player),
        "Beluga -> PttyBase":
            lambda state: state.has("Kai-man", player),
        "Beluga -> BigOcean":
            lambda state: state.has("Kai-man", player),

        #"Delta -> Jetty":
        #    lambda state: (state.has("P Nucklz", player) and state.has("P Sea", player) and (state.has("TwinDrag", player) or state.has("RC Bomb", player) or state.has("Firepower",player, 2)))
        #    or state.has("Boat Key", player),
        "Delta -> Jetty":
            lambda state: state.has("Boat Key", player) or state.has("Zone Key", player, 2),
        "SnowFld -> Blizzard":
            lambda state: state.has("ToughGuy", player),
        "Epsilon -> FPalace":
            lambda state: state.has("P Beast", player),
        #"Upsilon -> MtRoad":
        #    lambda state: plasma_clear_rules(state, player)
        #    or (state.has("Desert Key", player)), 
        "Upsilon -> MtRoad":
            lambda state: state.has("Desert Key", player) or state.has("Zone Key", player, 3),

        "MtRoad -> Zeta":
            lambda state: state.has("Youno", player),
        "Desert -> LavaPool":
            lambda state: state.has("Sibaloon", player),
        "Desert -> Omega":
            lambda state: state.has("Sibaloon", player),
        "LavaPool -> Volcano":
            lambda state: state.has("Sibaloon", player),
        "Volcano -> GlmBase":
            lambda state: state.has("Unagi", player),
        "Desert -> Theta":
            lambda state: state.has("Medal of Bravery", player) and state.has("Medal of Justice", player) and state.has("Medal of Love", player) and state.has("Medal of Friendship", player),

        "AccessPt -> Fantasy":
            lambda state: state.has("KameKing", player) and state.has("Youni", player),

        # Dungeon Advancment
        "MagBase -> MagBase Elifan":
            lambda state: state.has("Elifan", player),

        # Starting Teleports
        #"Menu -> Beta":
        #    lambda state: state.has("Beta Teleport", player) and state.has("Pommy", player),
        #"Menu -> Gamma":
        #    lambda state: state.has("Gamma Teleport", player) and state.has("Pommy", player),
        #"Menu -> Delta":
        #    lambda state: state.has("Delta Teleport", player) and state.has("Pommy", player),
        #"Menu -> Epsilon":
        #    lambda state: state.has("Epsilon Teleport", player) and state.has("Pommy", player),
        #"Menu -> Upsilon":
        #    lambda state: state.has("Upsilon Teleport", player) and state.has("Pommy", player),
        #"Menu -> Zeta":
        #    lambda state: state.has("Zeta Teleport", player) and state.has("Pommy", player),
        #"Menu -> Ita":
        #    lambda state: state.has("Ita Teleport", player) and state.has("Pommy", player),

        # Backward Connections
        "ToPlain -> B Valley":
            lambda state: state.has("Magnet Door Key", player) or state.has("Zone Key", player),
    }

def get_location_rules(player, fusedict):
    logger.warning(f"{fusedict["Beta - Fuse Fangs"][0]}, {fusedict["Beta - Fuse Fangs"][1]}")
    return {
        "Alpha - Return Ring":
            lambda state: state.has("Ring", player),
        "Alpha - Turn in Louie Photo":
            lambda state: state.has("Camera", player),
        #"Capture Louie Photo":
         #   lambda state: state.has("Camera", player),
        "L Forest - Basement Heart":
            lambda state: state.has("Elifan", player),
        "Alpha - Kid Challenge":
            lambda state: state.has("Pommy", player),
        "Omega - Feed Morg":
            lambda state: state.has("Teriyaki Beef", player),
        "ToPlain - Sampei Return Fishhook":
            lambda state: state.has("Fish Hook", player),
        "Wetwood - Heart":
            lambda state: state.has("Elifan", player),
        #"Baked Bread":
        #    lambda state: state.has("Flour", player),
        #"Delivered Bread":
        #    lambda state: state.has("Bread", player),
        "FPalace - Balloon":
            lambda state: plasma_clear_rules(state, player),
        "Finish Step Counter":
            lambda state: state.has("Stepcounter", player),
        "Colosseum Streak":
            lambda state: state.has_from_list(kara_hints, player,5),


        # Karabons
        "HighMt - Kai-man":
            lambda state: state.has("Disinfectant", player) and state.has("Aqua Bomb", player),
        "LiteCave - Th Liger":
           lambda state: state.has("Dorako", player),
        "HighMt - TwinDrag":
            lambda state: state.has("ToughGuy", player) or (state.has("Kai-man", player)),
        "HtSpring - P Beast":
            lambda state: state.has("Egg", player),
        #"IValley - Pteradon":
        #    lambda state: state.has("IceFlwrs", player),
        "Plasma - Dorako":
            lambda state: state.has("Elifan", player),
        "FPalace - Youno":
            lambda state: plasma_clear_rules(state, player),
        "Zeta - Sibaloon":
            lambda state: state.has("Stepcounter", player),
        "Omega - Unagi":
            lambda state: state.has("Teriyaki Beef", player),
        "Desert - Elekong":
            lambda state: state.has("P Animal", player),
        "ColdSea - Firekong":
            lambda state: state.has("Sibaloon", player),

        # Bomb Sythesis
        "Bomb Synthesis - Hold Bomb":
            lambda state: state.has("Balloon", player),
        "Bomb Synthesis - Aqua Bomb":
            lambda state: state.has("RainDrop", player),
        "Bomb Synthesis - Power Bomb":
            lambda state: state.has("Hammer", player),
        "Bomb Synthesis - RC Bomb":
            lambda state: state.has("Transistor", player),
        "Bomb Synthesis - Landmine":
            lambda state: state.has("Sensor", player),

        # Arcade
        "S Forest - Arcade":
            lambda state: state.has("FireUp", player),
        "Upsilon - Arcade":
            lambda state: state.has("FireUp", player),
        "Volcano - Arcade":
            lambda state: state.has("FireUp", player, 2),

        # Chests
        "Magnet - Fireup Chest":
            lambda state: state.has("Elifan", player),
        "Magnet - Medicine Chest":
            lambda state: state.has("Elifan", player),
        "Magnet - Silver Shoe Chest":
            lambda state: state.has("Elifan", player),
        
        "Pretty - Medicine Chest":
            lambda state: state.has("RC Bomb", player) or state.has("ToughGuy", player) or (state.has("P Nucklz", player) and (state.has("TwinDrag", player) or state.has("FireUp",player, 2))),
        "Pretty - Silver Armor Chest":
            lambda state: state.has("P Nucklz", player) or state.has("RC Bomb", player) or state.has("ToughGuy", player),
        "Pretty - Bombup Chest": 
            lambda state: state.has("P Nucklz", player) or state.has("RC Bomb", player) or state.has("ToughGuy", player),
        
        "Plasma - Medicine Chest":
            lambda state: state.has("Elifan", player),
        "Plasma - Crystal Chest":
            lambda state: state.has("Elifan", player) and state.has("Dorako", player) and state.has("ToughGuy", player),
        "Plasma - Fireup Chest":
            lambda state: state.has("Elifan", player) and state.has("Dorako", player) and state.has("ToughGuy", player),
        "Plasma - Gold Shoes Chest":
            lambda state: plasma_clear_rules(state, player),

        "Fantasy - Final Small Medicine Chest": 
            lambda state: fantasy_clear_rules(state, player),
        "Fantasy - Crystal Chest": 
            lambda state: fantasy_clear_rules(state, player),
        "Fantasy - Final Large Medicine Chest": 
            lambda state: fantasy_clear_rules(state, player),
        "Fantasy - First Small Medicine Chest":
            lambda state: state.has("ToughGuy", player) or state.has("P Nucklz", player),
        "Fantasy - First Large Medicine Chest":
            lambda state: state.has("ToughGuy", player) or state.has("P Nucklz", player),

        "Fantasy - Fireup Chest":
            lambda state: fantasy_clear_rules(state, player),
        "Fantasy - Bombup Chest":
            lambda state: fantasy_clear_rules(state, player),
        
        "Magnet - SID":
            #lambda state: general_sid_rules(state,player),
            lambda state: state.has("Elifan", player),
        "Pretty - SID":
            #lambda state: general_sid_rules(state,player),
            lambda state: state.has("P Nucklz", player) and (state.has("RC Bomb", player) or state.has("ToughGuy", player) or (state.has("TwinDrag", player) or state.has("FireUp",player, 2))),
        "Plasma - SID":
            #lambda state: general_sid_rules(state,player),
            lambda state: plasma_clear_rules(state, player) and state.has("P Beast", player),
            #lambda state: general_sid_rules(state,player),

        # Dungeon Clears 
        "Magnet - Magnet Bomber Defeated":
            lambda state: state.has("Elifan", player) and state.has("P Fangs", player),
        "Magnet - Magnet Clear":
            lambda state: state.has("Elifan", player) and state.has("P Fangs", player),
        "Pretty - Pretty Bomber Defeated":
            lambda state: state.has("P Sea", player),
        "Pretty - Pretty Clear":
            lambda state: state.has("P Sea", player),
        "Plasma - Plasma Bomber Defeated":
            lambda state: plasma_clear_rules(state, player),
        "Plasma - Plasma Clear":
            lambda state: plasma_clear_rules(state, player),
        "Golem - Golem Bomber Defeated":
            lambda state: state.has("SeaWing",player) and state.has("Sharkun", player),
        "Golem - Golem Clear":
            lambda state: state.has("SeaWing",player) and state.has("Sharkun", player),
        "Fantasy - Brain Bomber Defeated":
            lambda state: fantasy_clear_rules(state, player),

        # Fusions
        "Beta - Fuse Fangs": 
            lambda state: state.has(fusedict["Beta - Fuse Fangs"][0], player) and state.has(fusedict["Beta - Fuse Fangs"][1], player),
        "Beta - Fuse Sea":
            lambda state: state.has(fusedict["Beta - Fuse Sea"][0], player) and state.has(fusedict["Beta - Fuse Sea"][1], player),
        "Beta - Fuse Dragon":
            lambda state: state.has(fusedict["Beta - Fuse Dragon"][0], player) and state.has(fusedict["Beta - Fuse Dragon"][1], player),
        "Beta - Fuse SeaWing":
            #lambda state: state.has("Th Liger", player) and state.has("TwinDrag", player),
            lambda state: state.has(fusedict["Beta - Fuse SeaWing"][0], player) and state.has(fusedict["Beta - Fuse SeaWing"][1], player),

        
        #Rocks
        "L Forest - Side Rock":
            lambda state: state.has("Elifan", player),
        "L Forest - Main Rock":
            lambda state: state.has("Elifan", player),
        "Plains - Rock":
            lambda state: state.has("Elifan", player),
        "ColdSea - Entrance Rock":
            lambda state: state.has("Elifan", player),
        "ColdSea - Wall Rock":
            lambda state: state.has("Elifan", player),
        "ColdSea - Tree Rock":
            lambda state: state.has("Elifan", player),
        "Magbase - Outside Rock":
            lambda state: state.has("Elifan", player),
        "Wetwood - Rock":
            lambda state: state.has("Elifan", player),
        "S Forest - North Rock":
            lambda state: state.has("Elifan", player),
        "S Forest - South Rock":
            lambda state: state.has("Elifan", player),
        "SleetSt - Rock":
            lambda state: state.has("Elifan", player),
        "I Valley - Rock":
            lambda state: state.has("Elifan", player),
        "Blizzard - Rock":
            lambda state: state.has("Elifan", player),
        "SnowFld - Rock":
            lambda state: state.has("Elifan", player),
        "Jetty - Rock":
            lambda state: state.has("Elifan", player),
        "Arctic - Rock":
            lambda state: state.has("Elifan", player),
        "Quiksand - Rock":
            lambda state: state.has("Elifan", player),
        "LavaPool - Rock":
            lambda state: state.has("Elifan", player),
        "T Forest - Rock":
            lambda state: state.has("Elifan", player),
    }
from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import BombQuestWorld

def can_jump(state, player):
    return state.has("Jump Shoes", player) or state.has("Wings", player)

def has_bomb_splash(state,player):
    return state.has("Flak Bomb", player) or state.has("Speed Bomb", player) or state.has("Homing Bomb", player) \
    or state.has("Right Bomb", player) or state.has("Left Bomb", player) or state.has("Robot Bomb", player)

def can_hit_flying(state, player):
    return state.has("Power Gloves", player) and (has_bomb_splash(state,player) or can_KO(state,player))

def can_KO(state,player):
    return state.has("Tackle Belt", player) or state.has("Gauntlets",player) or state.has("Hammer",player)

def can_deal_follower(state, player):
    return can_KO(state,player) or state.has("Land Mine",player)

def can_pass_tiles(state, player):
    return state.has("Dash Shoes", player) or can_jump(state, player) or state.has("Tackle Belt", player)

def can_bomb_throw(state,player):
    return state.has("Power Gloves", player) and has_bomb_splash(state,player)

def get_region_rules(player, options):
    from .Locations import monster_list
    goal_option = options.game_goal.value
    if goal_option == 0:
        space_rules = lambda state: \
                state.can_reach_location("Water Commander", player) and \
                state.can_reach_location("Electro Commander", player) and \
                state.can_reach_location("Hurricane Commander", player) and \
                state.can_reach_location("Pyro Commander", player)
    elif goal_option ==1:
        space_rules = lambda state: state.has_from_list(monster_list, player, len(monster_list)) and state.has("Leather Armor", player)
    elif goal_option == 2:
        space_rules = lambda state: state.has("White Card", player) and state.has("Black Card", player) and state.has("Honey Card", player)

    return {
        "Peece Town -> Forest E3":
            lambda state: state.can_reach_location("Water Commander", player) or options.open_regions,
        "Forest E3 -> Peece Town":
            lambda state: state.can_reach_location("Water Commander", player) or options.open_regions,
        "Peece Town -> Beach F5":
            lambda state: state.can_reach_location("Electro Commander", player) or options.open_regions,
        "Beach F5 -> Peece Town":
            lambda state: state.can_reach_location("Electro Commander", player) or options.open_regions,
        "Peece Town -> Desert D6":
            lambda state: state.can_reach_location("Hurricane Commander", player) or options.open_regions,
        "Desert D6 -> Peece Town":
            lambda state: state.can_reach_location("Hurricane Commander", player) or options.open_regions,
        "Peece Town -> Space":
            space_rules,

        # Field Zone
        "Field A3 -> Field A2":
            lambda state: can_jump(state, player),
        "Field A2 -> Field A3":
            lambda state: can_jump(state, player),

        "Field D3 -> Forest E3":
            lambda state: state.can_reach_location("Water Commander", player) or options.open_regions,
        "Forest E3 -> Field D3":
            lambda state: state.can_reach_location("Water Commander", player) or options.open_regions,

        "Field C4 -> Desert C5":
            lambda state: (state.can_reach_location("Pyro Commander", player) or options.open_regions) and can_jump(state, player),
        "Desert C5 -> Field C4":
            lambda state: (state.can_reach_location("Pyro Commander", player) or options.open_regions) and can_jump(state, player),
    
        "Field A4 -> Field A4 Ruins Depths":
            lambda state: lambda state: state.has("Steel Shoes", player),
        "Field A4 Ruins Depths -> Field A4":
            lambda state: lambda state: state.has("Steel Shoes", player),

        # Forest Zone
        "Forest F1 -> Forest G1":
            lambda state: can_jump(state, player),
        "Forest G1 -> Forest F1":
            lambda state: can_jump(state, player),

        "Forest H2 -> Forest H1":
            lambda state: can_jump(state, player),
        "Forest H1 -> Forest H2":
            lambda state: can_jump(state, player),

        "Forest H4 -> Beach H5":
            lambda state: state.has("Wings", player),
        "Beach H5 -> Forest H4":
            lambda state: state.has("Wings", player),

        "Forest G3 -> Forest G4":
            lambda state: can_jump(state, player),
        "Forest G4 -> Forest G3":
            lambda state: can_jump(state, player),

        "Forest F4 -> Beach F5":
            lambda state: state.can_reach_location("Electro Commander", player) or options.open_regions,
        "Beach F5 -> Forest F4":
            lambda state: state.can_reach_location("Electro Commander", player) or options.open_regions,
        

        # Beach Zone
        "Beach G7 -> Beach F6":
            lambda state: can_jump(state, player),
        "Beach F6 -> Beach G7":
            lambda state: can_jump(state, player),
        
        "Beach G7 -> Beach H6":
            lambda state: can_jump(state, player),
        "Beach H6 -> Beach G7":
            lambda state: can_jump(state, player),

        "Beach E6 -> Wind Base":
            lambda state: state.has("Hammer", player) and (can_hit_flying(state,player) or can_jump(state, player)),
        "Wind Base -> Beach E6":
            lambda state: state.has("Hammer", player) and (can_hit_flying(state,player) or can_jump(state, player)),

        "Beach E6 -> Desert D6":
            lambda state: state.can_reach_location("Hurricane Commander", player) or options.open_regions,    
        "Desert D6 -> Beach E6":
            lambda state: state.can_reach_location("Hurricane Commander", player) or options.open_regions,

        


        # Desert Zone
        "Desert D7 -> Desert D8":
            lambda state: state.has("Wings", player),
        "Desert D8 -> Desert D7":
            lambda state: state.has("Wings", player),
        
        "Desert C8 -> Desert D8":
            lambda state: can_jump(state, player),
        "Desert D8 -> Desert C8":
            lambda state: can_jump(state, player),

        "Desert A6 -> Desert A5":
            lambda state: can_jump(state, player),
        "Desert A5 -> Desert A6":
            lambda state: can_jump(state, player),

        "Desert A7 -> Desert A6":
            lambda state: state.has("Power Bracelets", player),
        "Desert A6 -> Desert A7":
            lambda state: state.has("Power Bracelets", player),

        
        # Bases
         # Thunder base
        "Thunder Base -> Thunder Base 2":
            lambda state: state.has("Power Gloves", player) or state.has("Full Fire", player),
        "Thunder Base 2 -> Thunder Base":
            lambda state: state.has("Power Gloves", player) or state.has("Full Fire", player),

        "Thunder Base 4 -> Thunder Base 5":
            lambda state: can_jump(state, player) and state.has("Steel Shoes", player),
        "Thunder Base 5 -> Thunder Base 4":
            lambda state: can_jump(state, player) and state.has("Steel Shoes", player),
        
        "Thunder Base 5 -> Thunder Base 6":
            lambda state: can_jump(state, player),
        "Thunder Base 6 -> Thunder Base 5":
            lambda state: can_jump(state, player),

         # Wind Base
        "Wind Base 2 -> Wind Base 3":
            lambda state: (state.has("Power Gloves", player) or can_jump(state, player)) and  state.has("Shield", player),

        "Wind Base 3 -> Wind Base 4":
            lambda state: can_jump(state, player),
        "Wind Base 4 -> Wind Base 3":
            lambda state: can_jump(state, player) and state.has("Power Bracelets", player),

        "Wind Base 4 -> Wind Base 5":
            lambda state: state.has("Power Bracelets", player),

        "Wind Base 5 -> Wind Base 6":
            lambda state: can_jump(state, player) or state.has("Safety Shoes", player),
        "Wind Base 5 -> Wind Base 8":
            lambda state: can_jump(state, player) or state.has("Safety Shoes", player),

        "Wind Base 8 -> Wind Base 9":
            lambda state: state.has("Helmet", player) and can_jump(state, player),
        "Wind Base 9 -> Wind Base 8":
            lambda state: state.has("Helmet", player) and can_jump(state, player),

         # Fire Base
        "Fire Base -> Fire Base 2":
            lambda state: can_pass_tiles(state, player),
        "Fire Base 2 -> Fire Base":
            lambda state: can_pass_tiles(state, player),
        
        "Fire Base 5 -> Fire Base 6":
            lambda state: can_jump(state, player),
        "Fire Base 6 -> Fire Base 5":
            lambda state: can_jump(state, player),

        "Fire Base 3 -> Fire Base 7":
            lambda state: state.has("Wings", player) or (state.has("Dash Shoes", player) and state.has("Safety Shoes", player)),
        "Fire Base 7 -> Fire Base 3":
            lambda state: state.has("Wings", player) or (state.has("Dash Shoes", player) and state.has("Safety Shoes", player)),
        
        "Fire Base 8 -> Fire Base 9":
            lambda state: state.has("Long-Fuse Bomb", player),
        "Fire Base 9 -> Fire Base 8":
            lambda state: state.has("Long-Fuse Bomb", player),
        
        # Caves
        "Beach Cavern -> Beach Cavern 2":
            lambda state: state.has("Tackle Belt", player) and state.has("Dash Shoes", player),
        "Beach Cavern 3 -> Beach Cavern 4":
            lambda state: state.has("Full Fire", player) and state.has("Remote Control", player),
        
    }

def get_location_rules(player, options):
    return {
        #Monsters
         # Field
        "Ghostey":
            lambda state: can_hit_flying(state,player),
        "Grein":
            lambda state: can_jump(state,player) and state.has("Tackle Belt", player) and ((state.has("Ice Bomb", player) or state.has("Skull Bomb", player)) or (can_KO(state,player) and state.has("Power Glove", player))),
        "Trent":
            lambda state: has_bomb_splash(state, player),

         # Forest
        "Mechabomb":
            lambda state: can_jump(state,player),
        "Curansee":
            lambda state: state.has("Steel Shoes", player) and(state.has("Land Mine", player) or can_KO(state,player)),
        "Sandey":
            lambda state: state.has("Steel Shoes", player) and can_jump(state,player),
        "Digadug":
            lambda state: can_KO(state, player) or state.has("Short-Fuse Bomb", player),
        "Fruity":
            lambda state: can_hit_flying(state, player),
        "Baddo":
            lambda state: has_bomb_splash(state, player),
        "Shelterine":
            lambda state: state.has("Scuba Gears", player) and state.has("Aqua Bomb", player),
        "Killer Moth":
            lambda state: can_hit_flying(state, player),
        "Balballoon":
            lambda state: can_hit_flying(state, player),
        
         # Beach
        "Gargoyle":
            lambda state: state.has("Land Mine", player) or state.has("Robot Bomb", player), 
        "Seeballon":
            lambda state: state.has("Lamp", player) and can_pass_tiles(state, player),
        "Gell":
            lambda state: can_hit_flying(state, player),
        "Skullhead":
            lambda state: can_jump(state, player) and can_hit_flying(state, player),
        "Puuyan":
            lambda state: state.has("Scuba Gears", player) and state.has("Aqua Bomb", player),
        "Dragon Pup":
            lambda state: can_jump(state, player) and (state.has("Short-Fuse Bomb", player) or can_bomb_throw(state, player)),
        "Radiobomb Jr":
            lambda state: can_deal_follower(state,player),
        "Hurricane Commander":
            lambda state: can_jump(state,player) and can_hit_flying(state,player) and state.has("Homing Bomb",player),

        # Desert
        "Pygmin":
            lambda state: can_bomb_throw(state, player),
        "Crystal Demon":
            lambda state: state.has("Hammer", player) and state.has("Safety Shoes", player) and can_hit_flying(state,player),
        "Walking Hat":
            lambda state: state.has("Hammer", player) and state.has("Power Bracelets", player),
        "Jackenboxx":
            lambda state: state.has("Power Gloves", player),
        "Shadow Knight":
            lambda state: state.has("Power Gloves", player),
        "Flyball":
            lambda state: can_hit_flying(state, player),
        "Tinklebear":
            lambda state: can_deal_follower(state, player),
        "Sparky":
            lambda state: can_hit_flying(state, player),
        "Pyro Commander":
            lambda state: can_bomb_throw(state, player),

        #Chests
        "Field Chest A1":
            lambda state: state.has("Teleport Armor", player) and state.has("Glasses", player),
        "Field Chest C2 Underwater":
            lambda state: state.has("Hammer", player) and state.has("Scuba Gears", player) and state.has("Aqua Bomb", player),
        "Field Chest B1":
            lambda state: can_jump(state, player),
        "Forest Chest G3":
            lambda state: state.has("Glasses", player),
        "Forest Chest F3":
            lambda state: state.has("Hammer", player),
        "Beach Chest F5":
            lambda state: state.has("Power Gloves", player) and state.has("Speed Bomb", player),
        "Beach Chest H8":
            lambda state: state.has("Glasses", player),
        "Beach Chest F7":
            lambda state: state.has("Wings", player) or state.has("Scuba Gears", player),
        "Beach Chest Wind Base":
            lambda state: state.has("Wings", player),
        "Desert Chest C5":
            lambda state: state.has("Glasses", player) and can_jump(state,player),

        # Underground
        "Peece Underground D4":
            lambda state: state.has("Shovel", player),
        "Field Underground C4":
            lambda state: state.has("Shovel", player),
        "Forest Underground Cavern":
            lambda state: state.has("Shovel", player),
        "Beach Underground G6":
            lambda state: state.has("Shovel", player),
        "Beach Underground E7":
            lambda state: state.has("Shovel", player) and state.has("Teleport Armor", player),
        "Desert Underground C6":
            lambda state: state.has("Shovel", player),
        "Desert Underground B6":
            lambda state: state.has("Shovel", player),

        # Statues
        "Field Bomber Statue":
            lambda state: state.has("Dance", player),
        "Forest Bomber Statue":
            lambda state: state.has("Dance", player),
        "Beach Bomber Statue":
            lambda state: state.has("Dance", player),
        "Desert Bomber Statue":
            lambda state: state.has("Dance", player) and state.has("Hammer", player),
    
        # Synthesis
        "Peece Synthesis Rubber":
            lambda state: state.has("Explosive Core", player) and state.has("Rubber", player),
        "Peece Synthesis Clock":
            lambda state: state.has("Explosive Core", player) and state.has("Clock", player),
        "Peece Synthesis Ice Shard":
            lambda state: state.has("Explosive Core", player) and state.has("Ice Shard", player),
        "Peece Synthesis Poison Ivy":
            lambda state: state.has("Explosive Core", player) and state.has("Poison Ivy", player),
        "Peece Synthesis Boomerang":
            lambda state: state.has("Explosive Core", player) and state.has("Boomerang", player),
        "Peece Synthesis Skull":
            lambda state: state.has("Explosive Core", player) and state.has("Skull", player),
    
        # Events
        "Peece Card Trade":
            lambda state: state.has("White Card", player) and state.has("Black Card", player) and state.has("Honey Card", player)
    }
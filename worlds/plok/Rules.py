from typing import Callable, Dict

from BaseClasses import CollectionState, MultiWorld

def can_spin(state, player):
    return state.has("Spin Jump",player)

def has_fp_vehicles(state, player):
    return state.has("Unicycle",player) and state.has("Car",player) and state.has("Jet Booster",player) and state.has("Motorcycle",player) and state.has("Helicopter",player)

def get_region_rules(player):
    return {
        "Cotton Island -> Akrillic":
            lambda state: state.has("Plok Flag", player) and state.has("Spin Jump", player) and state.has("HealthUp",player),
        "Akrillic -> Legacy Island":
            lambda state: state.has("Grandpappy journal", player) and state.has("HealthUp",player,2),
        "Akrillic -> Akrillic Cave":
            lambda state: state.has("Flashlight", player)and state.has("HealthUp",player, 4),
        "Akrillic Cave -> Flea Pit":
            lambda state: state.has("Flea Pit Rope", player) and state.has("Spin Jump", player) and state.has("HealthUp",player, 5),
        
        #"Akrillic -> Garlen Beach":
        "Akrillic -> Sleepy Dale":
            lambda state: state.has("Limb", player, 3),
        #"Akrillic -> Plok Town":
        "Akrillic -> Venge Thicket":
            lambda state: state.has("Limb", player, 2),
        #"Akrillic -> Dreamy Cove":

        #"Akrillic Cave -> Creepy Forest":
        "Akrillic Cave -> Creepy Crag":
            lambda state: state.has("Limb", player, 3),
        "Akrillic Cave -> Gohome Cavern":
            lambda state: state.has("Limb", player, 3),
        #"Akrillic Cave -> Crashing Rocks":

        "Flea Pit -> Cycling Clever":
            lambda state: state.has("Unicycle", player),
        "Flea Pit -> Road Hogging":
            lambda state: state.has("Car", player),
        "Flea Pit -> High Flying":
            lambda state: state.has("Jet Booster", player),
        "Flea Pit -> Easy Riding":
            lambda state: state.has("Motorcycle", player),
        "Flea Pit -> In A Spin":
            lambda state: state.has("Helicopter", player),
        "Flea Pit -> Real Rumblings":
            lambda state: state.has("Tank", player),
        "Flea Pit -> Silent Running":
            lambda state: state.has("UFO", player),

    }

def get_location_rules(player,needed_queen):

    guffin_state = []
    #for item in guffin_items:
    #    guffin_state.append(lambda state: state.has(guffin_items[item], player))
    return {
        "CI - Log Falls Clear":
            lambda state: state.has("Spin Jump", player),
        "CI - Log Falls Fruit": 
            lambda state: state.has("Spin Jump", player),
        "CI - Log Falls Squire Gift":
            lambda state: state.has("Spin Jump", player),
        "CI - Rickety Bridge Clear":
            lambda state: state.has("Spin Jump", player),
        "CI - Rickety Bridge Fruit":
            lambda state: state.has("Spin Jump", player),
        "CI - Crazy Cradles Clear":
            lambda state: state.has("Spin Jump", player),
        "CI - Blind Leap Clear":
            lambda state: state.has("Spin Jump", player),
        "CI - Blind Leap Spire Fruit":
            lambda state: state.has("Spin Jump", player),
        "CI - Beach Warp":
            lambda state: state.has("Helicopter", player) and state.has("HealthUp", player),
        "CI - Columns Warp":
            lambda state: state.has("Motorcycle", player),
        "CI - Rickety Bridge Warp":
            lambda state: state.has("Jet Booster", player) and state.has("Spin Jump", player),
        "CI - Blind Leap Warp":
            lambda state: state.has("Unicycle", player),
        "CI - Bobbin Bros Clear":
            lambda state: state.has("Limb", player) and  state.has("HealthUp", player, 2),

        "LI - Fools Gap Clear":
            lambda state: state.has("Spin Jump", player),
        "LI - Zig Zag Clear":
            lambda state: state.has("Spin Jump", player),
        "LI - Zig Zag Fruit":
            lambda state: state.has("Spin Jump", player),
        "LI - Sponge Rock Clear":
            lambda state: state.has("Spin Jump", player) or state.has("HealthUp", player, 2),
        "LI - Sponge Rocks Fruit":
            lambda state: state.has("Spin Jump", player) or state.has("HealthUp", player, 2),
        "LI - Swifty Peaks Fruit":
            lambda state: state.has("HealthUp", player) or state.has("Spin Jump", player),
        "LI - Swifty Peaks Clear":
            lambda state: state.has("Spin Jump", player),
        "LI - Crouch Hill Fruit":
            lambda state: state.has("Spin Jump", player),
        "LI - Crouch Hill Clear":
            lambda state: state.has("Spin Jump", player),
        "LI - Bobbin Bros Clear":
            lambda state: state.has("HealthUp", player, 5) and state.has("Limb", player),




        "AK - Penkinos Clear":
            lambda state: state.has("Limb", player),
        "AK - Dreamy Cove Warp":
            lambda state: state.has("Unicycle", player) and state.has("Fireman Costume", player),
        "AK - Womack Spider Clear":
            lambda state: state.has("Limb", player),
        "AK - Crashing Rocks Warp":
            lambda state: state.has("Motorcycle", player),
        "AK - Rockyfella Clear":
            lambda state: state.has("Limb", player),



        "FP - Flea Queen Clear":
            lambda state:  ((sum(
                        (state.has("Boxer Shorts", player),
                        state.has("Scarf", player),
                        state.has("Bang Flag", player),
                        state.has("Torn Flag", player),
                        state.has("Overalls", player),
                        state.has("Sports Flag", player),
                        state.has("Pirate Flag", player),

                        state.has("Bone", player),
                        state.has("Carrot", player),
                        state.has("Anvil", player),
                        state.has("Old Boot", player),
                        state.has("Used String", player),
                        state.has("Broken Vase", player),)
                        ) >= needed_queen)) and state.has("Springs", player)
    }

def get_flea_location_rules(player):
    pass
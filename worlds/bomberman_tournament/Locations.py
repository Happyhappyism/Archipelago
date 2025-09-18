from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import BomberTWorld


class BomberTLocation(Location):
    game = "Bomberman Tournament"


class BomberTLocationData(NamedTuple):
    region: str
    type: str
    code: Optional[int] = None
    can_create: Callable[["BomberTWorld"], bool] = lambda world: True
    address: Optional[int] = None
    mask: Optional[int] = None
    locked_item: Optional[str] = None

# Code = 0x1C2-Last 2 of address- bitnumber
location_data_table: Dict[str, BomberTLocationData] = {
    "L Forest - Ring Pickup": BomberTLocationData(
        region="L Forest",
        type="item",
        code=0x1C2AD6,
        address=0x352AD,
        mask=0x40
    ),
    "Alpha - Camera": BomberTLocationData(
        region="Alpha",
        type="item",
        code=0x1C2AD4,
        address=0x352AD,
        mask=0x10
    ),
    #"Spot Louie": BomberTLocationData(
    #    region="L Forest",
    #    type="event",
    #    code=0x1C2966,
    #    address=0x35296,
    #    mask=0x40,
    #),

    "Alpha - Turn in Louie Photo": BomberTLocationData(
        region="Alpha",
        type="item",
        code=0x1C2971,
        address=0x35297,
        mask=0x2
    ),
    #"Sharkun Puzzle": BomberTLocationData(
    #    region="ToPlain",
    #    type="event",
    #    code=0x1C2990,
    #    address=0x35299,
    #    mask=0x1,
    #),
    "Colosseum Streak": BomberTLocationData(
        region="Beta", # Transistor
        type="item",
        code=0x1C2993,
        address=0x35299,
        mask=0x8, 
    ),
    "ToPlain - Sampei Raindrop": BomberTLocationData(
        region="Delta", # Raindrop
        type="item",
        code=0x1C29A6,
        address=0x3529A,
        mask=0x40,
    ),
    "ToPlain - Sampei Return Fishhook": BomberTLocationData(
        region="Delta", # Raindrop
        type="item",
        code=0x1C29B0,
        address=0x3529B,
        mask=0x40,
    ),
    "Beluga - Fish hook": BomberTLocationData(
        region="Beluga", # Raindrop
        type="item",
        code=0x1C29A7,
        address=0x3529A,
        mask=0x40,
    ),
    "Wetwood - Heart": BomberTLocationData(
        region="Wet Woods",
        type="heart",
        code=0x1C29B3,
        address=0x3529B,
        mask=0x8,
    ),
    #"Kin Flour": BomberTLocationData(
    #    region="Epsilon",
    #    type="item",
    #    code=0x1C29C0,
    #    address=0x3529C,
    #    mask=0x1,
    #),
    #"Baked Bread": BomberTLocationData(
    #    region="Upsilon",
    #    type="item",
    #    code=0x1C29C1,
    #    address=0x3529C,
    #    mask=0x2,
    #),
    "Upsilon - Delivered Bread": BomberTLocationData(
        region="Upsilon",
        type="item",
        code=0x1C29C2,
        address=0x3529C,
        mask=0x4,
    ),
    "L Forest - Basement Heart": BomberTLocationData(
        region="L Forest",
        type="heart",
        code=0x1C2A02,
        address=0x352A0,
        mask=0x4,
    ),
    "FPalace - Balloon": BomberTLocationData(
        region="FPalace",
        type="item",
        code=0x1C2A03,
        address=0x352A0,
        mask=0x8,
    ),
    "Volcano - Meat Heart": BomberTLocationData(
        region="Volcano",
        type="heart",
        code=0x1C2A04,
        address=0x352A0,
        mask=0x10,
    ),
    "Desert - Cave Medicine": BomberTLocationData(
        region="Desert",
        type="event",
        code=0x1C2A05,
        address=0x352A0,
        mask=0x20,
    ),
    "Zeta - Step Counter": BomberTLocationData(
        region="Zeta",
        type="item",
        code=0x1C2A06,
        address=0x352A0,
        mask=0x40,
    ),
    "Ita - Purchased Beef": BomberTLocationData(
        region="Ita",
        type="item",
        code=0x1C2D40,
        address=0x352D4,
        mask=0x1,
    ),

    # Medals


    # Karabons
    "Alpha - Pommy": BomberTLocationData(
        region="Alpha",
        type="karabon",
        code=0x1C2A90,
        address=0x352A2,
        mask=0x10,
    ),
    "ShuraRd - Ceedrun": BomberTLocationData(
        region="ShuraRd",
        type="karabon",
        code=0x1C2A91,
        address=0x352A9,
        mask=0x2,
    ),
    "Magnet - Elifan": BomberTLocationData(
        region="MagBase",
        type="karabon",
        code=0x1C2A92,
        address=0x352A9,
        mask=0x4,
    ),
    "ToPlain - Sharkun": BomberTLocationData(
        region="ToPlain",
        type="karabon",
        code=0x1C2A94,
        address=0x352A9,
        mask=0x10,
    ),
    "LiteCave - Th Liger": BomberTLocationData(
        region="LiteCave",
        type="karabon",
        code=0x1C2A95,
        address=0x352A9,
        mask=0x20,
    ),
    "HighMt - Kai-man": BomberTLocationData(
        region="HighMt",
        type="karabon",
        code=0x1C2A97,
        address=0x352A9,
        mask=0x80,
    ),
    "HighMt - TwinDrag": BomberTLocationData(
        region="HighMt",
        type="karabon",
        code=0x1C2A96,
        address=0x352A9,
        mask=0x40,
    ),
    "Pretty - P Nucklz": BomberTLocationData(
        region="PttyBase",
        type="karabon",
        code=0x1C2AA0,
        address=0x352AA,
        mask=0x1,
    ),
    "Arctic - ToughGuy": BomberTLocationData(
        region="Arctic",
        type="karabon",
        code=0x1C2AA2,
        address=0x352AA,
        mask=0x40,
    ),
    "HtSpring - P Beast": BomberTLocationData(
        region="HtSpring",
        type="karabon",
        code=0x1C2AA3,
        address=0x352AA,
        mask=0x8,
    ),
    "IValley - Pteradon": BomberTLocationData(
        region="IValley",
        type="karabon",
        code=0x1C2AA4,
        address=0x352AA,
        mask=0x40,
    ),
    "Plasma - Dorako": BomberTLocationData(
        region="PlzmBase",
        type="karabon",
        code=0x1C2AA5,
        address=0x352AA,
        mask=0x40,
    ),
    "FPalace - Youno": BomberTLocationData(
        region="FPalace",
        type="karabon",
        code=0x1C2AB0,
        address=0x352AB,
        mask=0x40,
    ),
    "Zeta - Sibaloon": BomberTLocationData(
        region="Zeta",
        type="karabon",
        code=0x1C2AA7,
        address=0x352AA,
        mask=0x40,
    ),
    "OldBase - P Animal": BomberTLocationData(
        region="OldBase",
        type="karabon",
        code=0x1C2AB1,
        address=0x352AB,
        mask=0x40,
    ),
    "Omega - Unagi": BomberTLocationData(
        region="Omega",
        type="karabon",
        code=0x1C2AB2,
        address=0x352AB,
        mask=0x40,
    ),
    "Desert - Elekong": BomberTLocationData(
        region="Desert",
        type="karabon",
        code=0x1C2AB4,
        address=0x352AB,
        mask=0x40,
    ),
    "Golem - Youni": BomberTLocationData(
        region="GlmBase",
        type="karabon",
        code=0x1C2AA6,
        address=0x352AA,
        mask=0x40,
    ),
    "TForest - KameKing": BomberTLocationData(
        region="TForest",
        type="karabon",
        code=0x1C2AB6,
        address=0x352AB,
        mask=0x4,
    ),
    "Pretty - MarinGon": BomberTLocationData(
        region="PttyBase",
        type="karabon",
        code=0x1C2AB7,
        address=0x352AB,
        mask=0x4,
    ),
    "ColdSea - Firekong": BomberTLocationData(
        region="ColdSea",
        type="karabon",
        code=0x1C2AC7,
        address=0x352AC,
        mask=0x80,
    ),

    # Fusions

        # Fusions
    "Beta - Fuse Fangs": BomberTLocationData(
        region="Beta",
        type="karabon",
        code=0x1C2A93,
        address=0x352A9,
        mask=0x8,
        #locked_item="P Fangs",
    ),
    "Beta - Fuse Sea": BomberTLocationData(
        region="Beta",
        type="karabon",
        code=0x1C2AA1,
        address=0x352AA,
        mask=0x2,
        #locked_item="P Sea",
    ),
    "Beta - Fuse Dragon": BomberTLocationData(
        region="Beta",
        type="karabon",
        code=0x1C2AB3,
        address=0x352AB,
        mask=0x40,
        #locked_item="P Dragon",
    ),
    "Beta - Fuse SeaWing": BomberTLocationData(
        region="Beta",
        type="karabon",
        code=0x1C2AB5,
        address=0x352AB,
        mask=0x20,
        #locked_item="SeaWing",
    ),

    "Magnet - SID": BomberTLocationData(
        region="MagBase",
        type="chest",
        code=0x1C2A81,
        address=0x352A9,
        mask=0x8,
        #locked_item="P Fangs",
    ),
    "Pretty - SID": BomberTLocationData(
        region="PttyBase",
        type="chest",
        code=0x1C2A82,
        address=0x352AA,
        mask=0x2,
        #locked_item="P Sea",
    ),
    "Plasma - SID": BomberTLocationData(
        region="PlzmBase",
        type="chest",
        code=0x1C2A83,
        address=0x352AB,
        mask=0x40,
        #locked_item="P Dragon",
    ),
    "Golem - SID": BomberTLocationData(
        region="GlmBase",
        type="chest",
        code=0x1C2A84,
        address=0x352AB,
        mask=0x20,
        #locked_item="SeaWing",
    ),

    # Chests
    "LiteCave - Disinfectant Chest": BomberTLocationData(
        region="LiteCave",
        type="chest",
        code=0x1C2A80,
        address=0x352A8,
        mask=0x1,
    ),
    "Magnet - Crystal Chest": BomberTLocationData(
        region="MagBase",
        type="chest",
        code=0x1C2A41,
        address=0x352A4,
        mask=0x2,
    ),
    "Magnet - Silver Shoe Chest": BomberTLocationData(
        region="MagBase",
        type="chest",
        code=0x1C2A45,
        address=0x352A4,
        mask=0x4,
    ),
    "Magnet - Fireup Chest": BomberTLocationData(
        region="MagBase",
        type="chest",
        code=0x1C2A43,
        address=0x352A4,
        mask=0x8,
    ),
    "Magnet - Medicine Chest": BomberTLocationData(
        region="MagBase",
        type="chest",
        code=0x1C2A44,
        address=0x352A4,
        mask=0x10,
    ),
    "Pretty - Bombup Chest": BomberTLocationData(
        region="PttyBase",
        type="chest",
        code=0x1C2A46,
        address=0x352A4,
        mask=0x40,
    ),
    "Pretty - Crystal Chest": BomberTLocationData(
        region="PttyBase",
        type="chest",
        code=0x1C2A50,
        address=0x352A5,
        mask=0x1,
    ),
    "Pretty - Medicine Chest": BomberTLocationData(
        region="PttyBase",
        type="chest",
        code=0x1C2A51,
        address=0x352A5,
        mask=0x2,
    ),
    "Pretty - Silver Armor Chest": BomberTLocationData(
        region="PttyBase",
        type="chest",
        code=0x1C2A52,
        address=0x352A5,
        mask=0x4,
    ),
    "Plasma - Medicine Chest": BomberTLocationData(
        region="PlzmBase",
        type="chest",
        code=0x1C2A53,
        address=0x352A5,
        mask=0x8,
    ),
    "Plasma - Crystal Chest": BomberTLocationData(
        region="PlzmBase",
        type="chest",
        code=0x1C2A54,
        address=0x352A5,
        mask=0x10,
    ),
    "Plasma - Fireup Chest": BomberTLocationData(
        region="PlzmBase",
        type="chest",
        code=0x1C2A55,
        address=0x352A5,
        mask=0x20,
    ),
    "Plasma - Gold Shoes Chest": BomberTLocationData(
        region="PlzmBase",
        type="chest",
        code=0x1C2A57,
        address=0x352A5,
        mask=0x80,
    ),
    "Golem - Crystal Chest": BomberTLocationData(
        region="GlmBase",
        type="chest",
        code=0x1C2A60,
        address=0x352A6,
        mask=0x80,
    ),
    "Golem - 1F Medicine Chest": BomberTLocationData(
        region="GlmBase",
        type="chest",
        code=0x1C2A62,
        address=0x352A6,
        mask=0x80,
    ),
    "Golem - Gold Armor Chest": BomberTLocationData(
        region="GlmBase",
        type="chest",
        code=0x1C2A63,
        address=0x352A6,
        mask=0x80,
    ),
    "Golem - 2F North Chest": BomberTLocationData(
        region="GlmBase",
        type="chest",
        code=0x1C2A64,
        address=0x352A6,
        mask=0x80,
    ),
    "Golem - 2F East Chest": BomberTLocationData(
        region="GlmBase",
        type="chest",
        code=0x1C2A65,
        address=0x352A6,
        mask=0x80,
    ),
    "Golem - 2F South Chest": BomberTLocationData(
        region="GlmBase",
        type="chest",
        code=0x1C2A66,
        address=0x352A6,
        mask=0x80,
    ),
    "Golem - 2F West Chest": BomberTLocationData(
        region="GlmBase",
        type="chest",
        code=0x1C2A67,
        address=0x352A6,
        mask=0x80,
    ),

    "Fantasy - Final Small Medicine Chest": BomberTLocationData(
        region="Fantasy",
        type="chest",
        code=0x1C2A70,
        address=0x352A7,
        mask=0x80,
    ), 
    "Fantasy - Crystal Chest": BomberTLocationData(
        region="Fantasy",
        type="chest",
        code=0x1C2A71,
        address=0x352A7,
        mask=0x80,
    ), 
    "Fantasy - Final Large Medicine Chest": BomberTLocationData(
        region="Fantasy",
        type="chest",
        code=0x1C2A72,
        address=0x352A7,
        mask=0x80,
    ), 
    "Fantasy - First Small Medicine Chest": BomberTLocationData(
        region="Fantasy",
        type="chest",
        code=0x1C2A73,
        address=0x352A7,
        mask=0x80,
    ), 
    "Fantasy - First Large Medicine Chest": BomberTLocationData(
        region="Fantasy",
        type="chest",
        code=0x1C2A74,
        address=0x352A7,
        mask=0x80,
    ), 
    "Fantasy - Fireup Chest": BomberTLocationData(
        region="Fantasy",
        type="chest",
        code=0x1C2A75,
        address=0x352A7,
        mask=0x80,
    ), 
    "Fantasy - Bombup Chest": BomberTLocationData(
        region="Fantasy",
        type="chest",
        code=0x1C2A76,
        address=0x352A7,
        mask=0x80,
    ), 
    
    # Shops
    "Beta - Comic 1": BomberTLocationData(
        region="Beta",
        type="shop",
        code=0x1C28F0,
        address=0x3528F,
        mask=0x1,
    ),
    "Delta - Comic 2": BomberTLocationData(
        region="Delta",
        type="shop",
        code=0x1C28F1,
        address=0x3528F,
        mask=0x2,
    ),
    "Epsilon - Comic 3": BomberTLocationData(
        region="Epsilon",
        type="shop",
        code=0x1C28F2,
        address=0x3528F,
        mask=0x4,
    ),
    "Volcano - Comic 4": BomberTLocationData(
        region="Volcano",
        type="shop",
        code=0x1C28F3,
        address=0x352F,
        mask=0x8,
    ),
    "Theta - Comic 5": BomberTLocationData(
        region="Theta",
        type="shop",
        code=0x1C28F4,
        address=0x352F,
        mask=0x10,
    ),
    "Theta - Hammer": BomberTLocationData(
        region="Theta",
        type="shop",
        code=0x1C2AC2,
        address=0x352F,
        mask=0x8,
    ),

    # Dungeon Clears
    "Magnet - Magnet Bomber Defeated": BomberTLocationData(
        region="MagBase",
        type="event",
        code=0x1C28F5,
        address=0x35298,
        mask=0x10,
    ),
    "Pretty - Pretty Bomber Defeated": BomberTLocationData(
        region="PttyBase",
        type="event",
        code=0x1C2907,
        address=0x35298,
        mask=0x40,
    ),
    "Plasma - Plasma Bomber Defeated": BomberTLocationData(
        region="PlzmBase",
        type="event",
        code=0x1C2910,
        address=0x35291,
        mask=0x1,
    ),
    "Golem - Golem Bomber Defeated": BomberTLocationData(
        region="GlmBase",
        type="event",
        code=0x1C2911,
        address=0x3529E,
        mask=0x1,
    ),

    "Magnet - Magnet Clear": BomberTLocationData(
        region="MagBase",
        type="event",
        code=0x1C2984,
        address=0x35298,
        mask=0x10,
    ),
    "Pretty - Pretty Clear": BomberTLocationData(
        region="PttyBase",
        type="event",
        code=0x1C2986,
        address=0x35298,
        mask=0x10,
    ),
    "Plasma - Plasma Clear": BomberTLocationData(
        region="PlzmBase",
        type="event",
        code=0x1C29C5,
        address=0x35298,
        mask=0x10,
    ),
    "Golem - Golem Clear": BomberTLocationData(
        region="GlmBase",
        type="event",
        code=0x1C29E6,
        address=0x35298,
        mask=0x10,
    ),

    #Bomb Sythesis
    "Bomb Synthesis - Hold Bomb": BomberTLocationData(
        region="Alpha",
        type="bomb",
        code=0x1C2D43,
        address=0x352D4,
        mask=0x8,
    ),
    "Bomb Synthesis - Aqua Bomb": BomberTLocationData(
        region="Alpha",
        type="bomb",
        code=0x1C2D44,
        address=0x352D4,
        mask=0x10,
    ),
    "Bomb Synthesis - Power Bomb": BomberTLocationData(
        region="Alpha",
        type="bomb",
        code=0x1C2D45,
        address=0x352D4,
        mask=0x20,
    ),
    "Bomb Synthesis - RC Bomb": BomberTLocationData(
        region="Alpha",
        type="bomb",
        code=0x1C2D46,
        address=0x352D4,
        mask=0x40,
    ),
    "Bomb Synthesis - Landmine": BomberTLocationData(
        region="Alpha",
        type="bomb",
        code=0x1C2D47,
        address=0x352D4,
        mask=0x80,
    ),

    # Arcade
    "B Valley - Arcade": BomberTLocationData(
        region="B Valley",
        type="arcade",
        code=0x1C2700,
        address=0x352A9,
        mask=0x1
    ),
    "S Forest - Arcade": BomberTLocationData(
        region="S Forest",
        type="arcade",
        code=0x1C2701,
        address=0x352A9,
        mask=0x1
    ),
    "Upsilon - Arcade": BomberTLocationData(
        region="Upsilon",
        type="arcade",
        code=0x1C2702,
        address=0x352A9,
        mask=0x1
    ),
    "Volcano - Arcade": BomberTLocationData(
        region="Volcano",
        type="arcade",
        code=0x1C2703,
        address=0x352A9,
        mask=0x1
    ),

    # Special Events
    "Alpha - Return Ring": BomberTLocationData(
        region="Alpha",
        type="event",
        code=0x1C2A90,
        address=0x352A9,
        mask=0x1
    ),
    #"L Forest - Capture Louie Photo": BomberTLocationData(
    #    region="L Forest",
    #    type="event",
    #    code=0x1C2970,
    #    address=0x35297,
    #    mask=0x1,
    #),
    "Alpha - Kid Challenge": BomberTLocationData(
        region="Alpha",
        type="event",
        code=0x1C2983,
        address=0x35298,
        mask=0x8,
    ),
    "Finish Step Counter": BomberTLocationData(
        region="Alpha",
        type="event",
        code=0x1C2914,
        address=0x35291,
        mask=0x10,
    ),
    "Beta - Ralph's Challenge": BomberTLocationData(
        region="Beta",
        type="event",
        code=0x1C2975,
        address=0x35297,
        mask=0x20,
    ),
    "Omega - Fed Morg": BomberTLocationData(
        region="Omega",
        type="event",
        code=0x1C29E4,
        address=0x3529E,
        mask=0x10,
    ),

    #Clear Condition
    "Fantasy - Brain Bomber Defeated": BomberTLocationData(
        region="Fantasy",
        type="victory",
        code=0x1C2912,
        address=0x35291,
        mask=0xFF,
        locked_item="MAX",
    ),

}
rock_location_data_table: Dict[str, BomberTLocationData] = {
    # Elifan Blocks
    "L Forest - Side Rock": BomberTLocationData(
        region="L Forest",
        type="rock",
        code=0x1C2F63,
        address=0x352F6,
        mask=0x8,
    ),
    "L Forest - Main Rock": BomberTLocationData(
        region="L Forest",
        type="rock",
        code=0x1C2F64,
        address=0x352F6,
        mask=0x10,
    ),
    "Plains - Rock": BomberTLocationData(
        region="Plains",
        type="rock",
        code=0x1C2F67,
        address=0x352F6,
        mask=0x80,
    ),
    "ColdSea - Entrance Rock": BomberTLocationData(
        region="ColdSea",
        type="rock",
        code=0x1C2F66,
        address=0x352F6,
        mask=0x40,
    ),
    "ColdSea - Wall Rock": BomberTLocationData(
        region="ColdSea",
        type="rock",
        code=0x1C2F65,
        address=0x352F6,
        mask=0x20,
    ),
    "ColdSea - Tree Rock": BomberTLocationData(
        region="ColdSea",
        type="rock",
        code=0x1C2F62,
        address=0x352F6,
        mask=0x4,
    ),
    "Magbase - Outside Rock": BomberTLocationData(
        region="MagBase",
        type="rock",
        code=0x1C2F61,
        address=0x352F6,
        mask=0x2,
    ),
    "Wetwood - Rock": BomberTLocationData(
        region="Wet Woods",
        type="rock",
        code=0x1C2F71,
        address=0x352F7,
        mask=0x2,
    ),
    "S Forest - North Rock": BomberTLocationData(
        region="S Forest",
        type="rock",
        code=0x1C2F72,
        address=0x352F7,
        mask=0x4,
    ),
    "S Forest - South Rock": BomberTLocationData(
        region="S Forest",
        type="rock",
        code=0x1C2F73,
        address=0x352F7,
        mask=0x8,
    ),
    "SleetSt - Rock": BomberTLocationData(
        region="SleetSt",
        type="rock",
        code=0x1C2FA0,
        address=0x352FA,
        mask=0x1,
    ),
    "I Valley - Rock": BomberTLocationData(
        region="IValley",
        type="rock",
        code=0x1C2FA1,
        address=0x352FA,
        mask=0x2,
    ),
    "Blizzard - Rock": BomberTLocationData(
        region="Blizzard",
        type="rock",
        code=0x1C2FA2,
        address=0x352FA,
        mask=0x4,
    ),
    "SnowFld - Rock": BomberTLocationData(
        region="SnowFld",
        type="rock",
        code=0x1C2FA3,
        address=0x352FA,
        mask=0x8,
    ),
    "Jetty - Rock": BomberTLocationData(
        region="Jetty",
        type="rock",
        code=0x1C2FA4,
        address=0x352FA,
        mask=0x10,
    ),
    "Arctic - Rock": BomberTLocationData(
        region="Arctic",
        type="rock",
        code=0x1C2FA5,
        address=0x352FA,
        mask=0x20,
    ),
    "Quiksand - Rock": BomberTLocationData(
        region="Quiksand",
        type="rock",
        code=0x1C3074,
        address=0x35307,
        mask=0x10,
    ),
    "LavaPool - Rock": BomberTLocationData(
        region="LavaPool",
        type="rock",
        code=0x1C3075,
        address=0x35307,
        mask=0x20,
    ),
    "T Forest - Rock": BomberTLocationData(
        region="TForest",
        type="rock",
        code=0x1C3085,
        address=0x35308,
        mask=0x20,
    ),


}

location_table = {name: data.code for name, data in location_data_table.items() if data.code is not None}
rock_location_table = {name: data.code for name, data in rock_location_data_table.items() if data.code is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}

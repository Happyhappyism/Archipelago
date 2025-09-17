from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import BombQuestWorld


class BombQuestLocation(Location):
    game = "Bomberman Quest"

class BombQuestLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["BombQuestWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None
    ROM_item: Optional[int] = None
    WRAM_flags: Optional[int] = None
    flag_Mask: Optional[int] = None
    type: Optional[str] = None  # "Chest", "Monster", "Synthesis", "Boss", "Underground", "Synthesis"

location_data_table: Dict[str, BombQuestLocation] = {
    "Ballom": BombQuestLocationData(
    region="Field B4",
    address=0x1C3001,
    WRAM_flags=0xEB2,
    ROM_item=0x34E37,
    type="Monster"
    ),
    "Burol": BombQuestLocationData(
    region="Field A3",
    address=0x1C3002,
    WRAM_flags=0xEB3,
    ROM_item=0x34E39,
    type="Monster"
    ),
    "Kurin": BombQuestLocationData(
    region="Field C3",
    address=0x1C3003,
    WRAM_flags=0xEB4,
    ROM_item=0x34E3B,
    type="Monster"
    ),
    "Blobby": BombQuestLocationData(
    region="Field B2",
    address=0x1C3004,
    WRAM_flags=0xEB5,
    ROM_item=0x34E3D,
    type="Monster"
    ),
    "Pengy": BombQuestLocationData(
    region="Field D1",
    address=0x1C3005,
    WRAM_flags=0xEB6,
    ROM_item=0x34E3F,
    type="Monster"
    ),
    "Ghostey": BombQuestLocationData(
    region="Water Base",
    address=0x1C3006,
    WRAM_flags=0xEB7,
    ROM_item=0x34E41,
    type="Monster"
    ),
    "Parse": BombQuestLocationData(
    region="Field A4 Ruins Depths",
    address=0x1C3007,
    WRAM_flags=0xEB8,
    ROM_item=0x34E43,
    type="Monster"
    ),
    "Onil": BombQuestLocationData(
    region="Field A4",
    address=0x1C3008,
    WRAM_flags=0xEB9,
    ROM_item=0x34E45,
    type="Monster"
    ),
    "Grein": BombQuestLocationData(
    region="Field A1",
    address=0x1C3009,
    WRAM_flags=0xEBD,
    ROM_item=0x34E4D,
    type="Monster"
    ),
    "Borey": BombQuestLocationData(
    region="Field C1",
    address=0x1C300A,
    WRAM_flags=0xEC6,
    ROM_item=0x34E5F,
    type="Monster"
    ),
    "Archer": BombQuestLocationData(
    region="Field A2",
    address=0x1C300B,
    WRAM_flags=0xED0,
    ROM_item=0x34E73,
    type="Monster"
    ),
    "Trent": BombQuestLocationData(
    region="Field D2",
    address=0x1C300C,
    WRAM_flags=0xEE0,
    ROM_item=0x34E93,
    type="Monster"
    ),
    "Water Commander": BombQuestLocationData(
    region="Water Base",
    address=0x1C300D,
    WRAM_flags=0xEE2,
    ROM_item=0x34E97,
    type="Boss"
    ),

    "Mechabomb": BombQuestLocationData(
    region="Thunder Base 3",
    address=0x1C3011,
    WRAM_flags=0xEBA,
    ROM_item=0x34E47,
    type="Monster"
    ),
    "Curansee": BombQuestLocationData(
    region="Forest E1",
    address=0x1C3012,
    WRAM_flags=0xEBE,
    ROM_item=0x34E4F,
    type="Monster"
    ),
    "Sandey": BombQuestLocationData(
    region="Thunder Base 6",
    address=0x1C3013,
    WRAM_flags=0xEC0,
    ROM_item=0x34E53,
    type="Monster"
    ),
    "Digadug": BombQuestLocationData(
    region="Forest E2",
    address=0x1C3014,
    WRAM_flags=0xEC4,
    ROM_item=0x34E5B,
    type="Monster"
    ),
    "Fruity": BombQuestLocationData(
    region="Forest F2",
    address=0x1C3015,
    WRAM_flags=0xEC5,
    ROM_item=0x34E5D,
    type="Monster"
    ),
    "Torton": BombQuestLocationData(
    region="Forest H1",
    address=0x1C3016,
    WRAM_flags=0xEC8,
    ROM_item=0x34E63,
    type="Monster"
    ),
    "Baddo": BombQuestLocationData(
    region="Forest H3",
    address=0x1C3017,
    WRAM_flags=0xECC,
    ROM_item=0x34E6B,
    type="Monster"
    ),
    "Shelterine": BombQuestLocationData(
    region="Forest H2",
    address=0x1C3018,
    WRAM_flags=0xEC3,
    ROM_item=0x34E59,
    type="Monster"
    ),
    "Mad Flower": BombQuestLocationData(
    region="Forest E3",
    address=0x1C3019,
    WRAM_flags=0xED8,
    ROM_item=0x34E83,
    type="Monster"
    ),
    "Devil Ant": BombQuestLocationData(
    region="Forest G2",
    address=0x1C301A,
    WRAM_flags=0xED9,
    ROM_item=0x34E85,
    type="Monster"
    ),
    "Killer Moth": BombQuestLocationData(
    region="Forest G4",
    address=0x1C301B,
    WRAM_flags=0xEDA,
    ROM_item=0x34E87,
    type="Monster"
    ),
    "Balballoon": BombQuestLocationData(
    region="Forest G1",
    address=0x1C301C,
    WRAM_flags=0xEDC,
    ROM_item=0x34E8B,
    type="Monster"
    ),
    "Electro Commander": BombQuestLocationData(
    region="Thunder Base 7",
    address=0x1C301D,
    WRAM_flags=0xEE3,
    ROM_item=0x34E99,
    type="Boss"
    ),
    
    "Pinokion": BombQuestLocationData(
    region="Wind Base 5",
    address=0x1C3021,
    WRAM_flags=0xEBB,
    ROM_item=0x34E49,
    type="Monster"
    ),
    "Iceal": BombQuestLocationData(
    region="Beach F8",
    address=0x1C3022,
    WRAM_flags=0xEBC,
    ROM_item=0x34E4B,
    type="Monster"
    ),
    "Matango": BombQuestLocationData(
    region="Beach Cavern 4",
    address=0x1C3023,
    WRAM_flags=0xEBF,
    ROM_item=0x34E51,
    type="Monster"
    ),
    "Seeballon": BombQuestLocationData(
    region="Beach G8",
    address=0x1C3024,
    WRAM_flags=0xEC2,
    ROM_item=0x34E57,
    type="Monster"
    ),
    "Despider": BombQuestLocationData(
    region="Beach H6",
    address=0x1C3025,
    WRAM_flags=0xED2,
    ROM_item=0x34E77,
    type="Monster"
    ),
    "Gell": BombQuestLocationData(
    region="Beach G5",
    address=0x1C3026,
    WRAM_flags=0xEC7,
    ROM_item=0x34E61,
    type="Monster"
    ),
    "Gargoyle": BombQuestLocationData(
    region="Beach F5",
    address=0x1C3027,
    WRAM_flags=0xECA,
    ROM_item=0x34E67,
    type="Monster"
    ),
    "Krabbler": BombQuestLocationData(
    region="Beach F6",
    address=0x1C3028,
    WRAM_flags=0xECF,
    ROM_item=0x34E71,
    type="Monster"
    ),
    "Skullhead": BombQuestLocationData(
    region="Wind Base 3",
    address=0x1C3029,
    WRAM_flags=0xED5,
    ROM_item=0x34E7D,
    type="Monster"
    ),
    "Puuyan": BombQuestLocationData(
    region="Beach E8",
    address=0x1C302A,
    WRAM_flags=0xEDD,
    ROM_item=0x34E8D,
    type="Monster"
    ),
    "Dragon Pup": BombQuestLocationData(
    region="Beach E6",
    address=0x1C302B,
    WRAM_flags=0xEDE,
    ROM_item=0x34E8F,
    type="Monster"
    ),
    "Radiobomb Jr": BombQuestLocationData(
    region="Beach Cavern 2",
    address=0x1C302C,
    WRAM_flags=0xEE1,
    ROM_item=0x34E95,
    type="Monster"
    ),
    "Hurricane Commander": BombQuestLocationData(
    region="Wind Base 9",
    address=0x1C302D,
    WRAM_flags=0xEE4,
    ROM_item=0x34E9B,
    type="Boss"
    ),

    "Pygmin": BombQuestLocationData(
    region="Desert A8",
    address=0x1C3031,
    WRAM_flags=0xEC1,
    ROM_item=0x34E55,
    type="Monster"
    ),
    "Snaky": BombQuestLocationData(
    region="Desert A6",
    address=0x1C3032,
    WRAM_flags=0xEC9,
    ROM_item=0x34E65,
    type="Monster"
    ),
    "Crystal Demon": BombQuestLocationData(
    region="Desert C6",
    address=0x1C3033,
    WRAM_flags=0xECB,
    ROM_item=0x34E69,
    type="Monster"
    ),
    "Hippity Hop": BombQuestLocationData(
    region="Fire Base 2",
    address=0x1C3034,
    WRAM_flags=0xECD,
    ROM_item=0x34E6D,
    type="Monster"
    ),
    "Jackenboxx": BombQuestLocationData(
    region="Desert D6",
    address=0x1C3035,
    WRAM_flags=0xECE,
    ROM_item=0x34E6F,
    type="Monster"
    ),
    "Shadow Knight": BombQuestLocationData(
    region="Fire Base 9",
    address=0x1C3036,
    WRAM_flags=0xED1,
    ROM_item=0x34E75,
    type="Monster"
    ),
    "Flyball": BombQuestLocationData(
    region="Desert B7",
    address=0x1C3037,
    WRAM_flags=0xED3,
    ROM_item=0x34E79,
    type="Monster"
    ),
    "Tinklebear": BombQuestLocationData(
    region="Fire Base 7",
    address=0x1C3038,
    WRAM_flags=0xED4,
    ROM_item=0x34E7B,
    type="Monster"
    ),
    "Walking Hat": BombQuestLocationData(
    region="Desert A7",
    address=0x1C3039,
    WRAM_flags=0xED6,
    ROM_item=0x34E7F,
    type="Monster"
    ),
    "Sparky": BombQuestLocationData(
    region="Fire Base 4",
    address=0x1C303A,
    WRAM_flags=0xED7,
    ROM_item=0x34E81,
    type="Monster"
    ),
    "Hoopster": BombQuestLocationData(
    region="Desert D8",
    address=0x1C303B,
    WRAM_flags=0xEDB,
    ROM_item=0x34E89,
    type="Monster"
    ),
    "Yeti": BombQuestLocationData(
    region="Desert B5",
    address=0x1C303C,
    WRAM_flags=0xEDF,
    ROM_item=0x34E91,
    type="Monster"
    ),
    "Pyro Commander": BombQuestLocationData(
    region="Fire Base 10",
    address=0x1C303D,
    WRAM_flags=0xEE6,
    ROM_item=0x34E9D,
    type="Boss"
    ),


    "Forest Chest E1": BombQuestLocationData(
    region="Forest E1",
    address=0x1C3041,
    WRAM_flags=0xEA1,
    flag_Mask=0x2,
    ROM_item=0x4559B,
    type="Chest"
    ),
    "Forest Chest G3": BombQuestLocationData(
    region="Forest G3",
    address=0x1C3042,
    WRAM_flags=0xEA1,
    flag_Mask=0x4,
    ROM_item=0x4559D,
    type="Chest"
    ),
    "Field Chest A1": BombQuestLocationData(
    region="Field A1",
    address=0x1C3043,
    WRAM_flags=0xEA1,
    flag_Mask=0x8,
    ROM_item=0x4559F,
    type="Chest"
    ),
    "Beach Chest H8": BombQuestLocationData(
    region="Beach H8",
    address=0x1C3044,
    WRAM_flags=0xEA1,
    flag_Mask=0x10,
    ROM_item=0x455A1,
    type="Chest"
    ),
    "Field Chest C2 Underwater": BombQuestLocationData(
    region="Field C2",
    address=0x1C3045,
    WRAM_flags=0xEA1,
    flag_Mask=0x20,
    ROM_item=0x455A3,
    type="Chest"
    ),
    "Field Chest Water Base": BombQuestLocationData(
    region="Water Base",
    address=0x1C3046,
    WRAM_flags=0xEA1,
    flag_Mask=0x40,
    ROM_item=0x455A5,
    type="Chest"
    ),
    "Beach Chest Wind Base": BombQuestLocationData(
    region="Wind Base 7",
    address=0x1C3047,
    WRAM_flags=0xEA1,
    flag_Mask=0x80,
    ROM_item=0x455A7,
    type="Chest"
    ),

    "Forest Chest F3": BombQuestLocationData(
    region="Forest F3",
    address=0x1C3048,
    WRAM_flags=0xEA2,
    flag_Mask=0x1,
    ROM_item=0x455A9,
    type="Chest"
    ),
    "Beach Chest F1": BombQuestLocationData(
    region="Beach F5",
    address=0x1C3049,
    WRAM_flags=0xEA2,
    flag_Mask=0x2,
    ROM_item=0x455AB,
    type="Chest"
    ),
    "Beach Chest F7": BombQuestLocationData(
    region="Beach F7",
    address=0x1C304A,
    WRAM_flags=0xEA2,
    flag_Mask=0x4,
    ROM_item=0x455AD,
    type="Chest"
    ),
    "Desert Chest C5": BombQuestLocationData(
    region="Desert C5",
    address=0x1C304B,
    WRAM_flags=0xEA2,
    flag_Mask=0x8,
    ROM_item=0x455AF,
    type="Chest"
    ),
    "Desert Chest B8": BombQuestLocationData(
    region="Desert B8",
    address=0x1C304C,
    WRAM_flags=0xEA2,
    flag_Mask=0x10,
    ROM_item=0x455B1,
    type="Chest"
    ),
    "Field Chest B1": BombQuestLocationData(
    region="Field B1",
    address=0x1C304D,
    WRAM_flags=0xEA2,
    flag_Mask=0x20,
    ROM_item=0x455B3,
    type="Chest"
    ),

    "Field Bomber Statue": BombQuestLocationData(
    region="Field B3",
    address=0x1C3060,
    WRAM_flags=0xEA5,
    flag_Mask=0x1,
    ROM_item=0x455D9,
    type="Statue"
    ),
    "Forest Bomber Statue": BombQuestLocationData(
    region="Forest H1",
    address=0x1C3061,
    WRAM_flags=0xEA5,
    flag_Mask=0x2,
    ROM_item=0x455DB,
    type="Statue"
    ),
    "Beach Bomber Statue": BombQuestLocationData(
    region="Beach H5",
    address=0x1C3062,
    WRAM_flags=0xEA5,
    flag_Mask=0x4,
    ROM_item=0x455DD,
    type="Statue"
    ),
    "Desert Bomber Statue": BombQuestLocationData(
    region="Desert A5",
    address=0x1C3063,
    WRAM_flags=0xEA5,
    flag_Mask=0x8,
    ROM_item=0x455DF,
    type="Statue"
    ),

    "Peece Underground D4": BombQuestLocationData(
    region="Peece Town",
    address=0x1C3064,
    WRAM_flags=0xEA5,
    flag_Mask=0x10,
    ROM_item=0x455E1,
    type="Underground"
    ),
    "Field Underground C4": BombQuestLocationData(
    region="Field C4",
    address=0x1C3065,
    WRAM_flags=0xEA5,
    flag_Mask=0x20,
    ROM_item=0x455E3,
    type="Underground"
    ),
    "Forest Underground Cavern": BombQuestLocationData(
    region="Forest G1",
    address=0x1C3067,
    WRAM_flags=0xEA5,
    flag_Mask=0x80,
    ROM_item=0x455E7,
    type="Underground"
    ),
    "Beach Underground G6": BombQuestLocationData(
    region="Beach F7",
    address=0x1C3068,
    WRAM_flags=0xEA6,
    flag_Mask=0x1,
    ROM_item=0x455E9,
    type="Underground"
    ),
    "Beach Underground E7": BombQuestLocationData(
    region="Beach E7",
    address=0x1C3069,
    WRAM_flags=0xEA6,
    flag_Mask=0x2,
    ROM_item=0x455EB,
    type="Underground"
    ),
    "Desert Underground C6": BombQuestLocationData(
    region="Desert B5",
    address=0x1C306A,
    WRAM_flags=0xEA6,
    flag_Mask=0x4,
    ROM_item=0x455ED,
    type="Underground"
    ),
    "Desert Underground B6": BombQuestLocationData(
    region="Desert B6",
    address=0x1C306B,
    WRAM_flags=0xEA6,
    flag_Mask=0x8,
    ROM_item=0x455EF,
    type="Underground"
    ),

    "Peece Synthesis Rubber": BombQuestLocationData(
    region="Peece Town",
    address=0x1C3070,
    ROM_item=0x44F1F,
    flag_Mask=0x1,
    type="Synthesis"
    ),
    "Peece Synthesis Clock": BombQuestLocationData(
    region="Peece Town",
    address=0x1C3071,
    ROM_item=0x44F21,
    flag_Mask=0x2,
    type="Synthesis"
    ),
    "Peece Synthesis Ice Shard": BombQuestLocationData(
    region="Peece Town",
    address=0x1C3072,
    ROM_item=0x44F23,
    flag_Mask=0x4,
    type="Synthesis"
    ),
    "Peece Synthesis Poison Ivy": BombQuestLocationData(
    region="Peece Town",
    address=0x1C3073,
    ROM_item=0x44F25,
    flag_Mask=0x8,
    type="Synthesis"
    ),
    "Peece Synthesis Boomerang": BombQuestLocationData(
    region="Peece Town",
    address=0x1C3074,
    ROM_item=0x44F27,
    flag_Mask=0x10,
    type="Synthesis"
    ),
    "Peece Synthesis Skull": BombQuestLocationData(
    region="Peece Town",
    address=0x1C3075,
    ROM_item=0x44F29,
    flag_Mask=0x20,
    type="Synthesis"
    ),
    "Peece Card Trade": BombQuestLocationData(
    region="Peece Town",
    address=0x1C3078,
    WRAM_flags=0xE98,
    flag_Mask=0x1,
    type="Event"
    ),

}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
rom_location_map = {name: data.ROM_item for name, data in location_data_table.items() if (data.ROM_item is not None and data.type != "Synthesis")}

monster_flags = {data.address: data.WRAM_flags for name, data in location_data_table.items() if (data.type == "Monster" or data.type == "Boss") and (data.WRAM_flags is not None)}
monster_list = [name for name,data in location_data_table.items() if (data.type == "Monster" or data.type == "Boss") ]
#boss_flags = {data.code: data.WRAM_flags for name, data in location_data_table.items() if data.type == "Boss" and data.WRAM_flags is not None}
overworld_flags = {data.address: [data.WRAM_flags,  data.flag_Mask] for name, data in location_data_table.items() if (data.type == "Chest" or data.type == "Statue" or data.type == "Underground") and data.WRAM_flags is not None}
sythesis_flags = {data.address: data.flag_Mask for name, data in location_data_table.items() if (data.type == "Synthesis") and (data.flag_Mask is not None)}
sythesis_rom_map = {name: data.ROM_item for name, data in location_data_table.items() if (data.ROM_item is not None and data.type == "Synthesis")}
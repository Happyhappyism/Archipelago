from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import BombQuestWorld
    

class BombQuestItem(Item):
    game = "Bomberman Quest"

class BombQuestItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[["BombQuestWorld"], bool] = lambda world: True
    fillweight: Optional[float] = None
    WRAM_address: Optional[int] = None
    item_type: Optional[int] = None
    item_index: Optional[int] = None
    stackable: bool = False

item_data_table: Dict[str, BombQuestItemData] = {
    
    # Items
    "Wings": BombQuestItemData(
        code=0x1C3001,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x1,
        WRAM_address= 0xF24
    ),
    "Jump Shoes": BombQuestItemData(
        code=0x1C3002,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x2,
        WRAM_address= 0xF25
    ),
    "Dash Shoes": BombQuestItemData(
        code=0x1C3003,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x3,
        WRAM_address= 0xF26
    ),
    "Power Gloves": BombQuestItemData(
        code=0x1C3004,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x4,
        WRAM_address= 0xF27
    ),
    "Hammer": BombQuestItemData(
        code=0x1C3005,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x5,
        WRAM_address= 0xF28
    ),
    "Remote Control": BombQuestItemData(
        code=0x1C3006,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x6,
        WRAM_address= 0xF29
    ),
    "Tackle Belt": BombQuestItemData(
        code=0x1C3007,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x7,
        WRAM_address= 0xF2A
    ),
    # "Bomb": BombQuestItemData(
    #     code=0x1C3008,
    #     type=ItemClassification.progression,
    #    item_type = 0x0,
    #    item_index = 0x8,
    #     WRAM_address= 0xF2B
    # ),
    "Ice Bomb": BombQuestItemData(
        code=0x1C3009,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x9,
        WRAM_address= 0xF2C
    ),
    "Poison Bomb": BombQuestItemData(
        code=0x1C300A,
        type=ItemClassification.filler,
        item_type = 0x0,
        item_index = 0xA,
        WRAM_address= 0xF2D
    ),
    "Short-Fuse Bomb": BombQuestItemData(
        code=0x1C300B,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0xB,
        WRAM_address= 0xF2E
    ),
    "Long-Fuse Bomb": BombQuestItemData(
        code=0x1C300C,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0xC,
        WRAM_address= 0xF2F
    ),
    "Rubber Bomb": BombQuestItemData(
        code=0x1C300D,
        type=ItemClassification.useful,
        item_type = 0x0,
        item_index = 0xD,
        WRAM_address= 0xF30
    ),
    "Wide-Range Bomb": BombQuestItemData(
        code=0x1C300E,
        type=ItemClassification.useful,
        item_type = 0x0,
        item_index = 0xE,
        WRAM_address= 0xF31
    ),
    "Skull Bomb": BombQuestItemData(
        code=0x1C300F,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0xF,
        WRAM_address= 0xF32
    ),
    "Land Mine": BombQuestItemData(
        code=0x1C3010,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x10,
        WRAM_address= 0xF33
    ),
    "Flak Bomb": BombQuestItemData(
        code=0x1C3011,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x11,
        WRAM_address= 0xF34
    ),
    "Homing Bomb": BombQuestItemData(
        code=0x1C3012,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x12,
        WRAM_address= 0xF35
    ),
    "Speed Bomb": BombQuestItemData(
        code=0x1C3013,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x13,
        WRAM_address= 0xF36
    ),
    "Aqua Bomb": BombQuestItemData(
        code=0x1C3014,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x14,
        WRAM_address= 0xF37
    ),
    "Robot Bomb": BombQuestItemData(
        code=0x1C3015,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x15,
        WRAM_address= 0xF38
    ),
    "Right Bomb": BombQuestItemData(
        code=0x1C3016,
        type=ItemClassification.useful,
        item_type = 0x0,
        item_index = 0x16,
        WRAM_address= 0xF39
    ),
    "Left Bomb": BombQuestItemData(
        code=0x1C3017,
        type=ItemClassification.useful,
        item_type = 0x0,
        item_index = 0x17,
        WRAM_address= 0xF3A
    ),
    "Yo-yo": BombQuestItemData(
        code=0x1C3018,
        type=ItemClassification.useful,
        item_type = 0x0,
        item_index = 0x18,
        WRAM_address= 0xF3B
    ),
    "Dance": BombQuestItemData(
        code=0x1C3019,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x19,
        WRAM_address= 0xF3C
    ),
    "Shovel": BombQuestItemData(
        code=0x1C301A,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x1A,
        WRAM_address= 0xF3D
    ),
    "Shield": BombQuestItemData(
        code=0x1C301B,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x1B,
        WRAM_address= 0xF3E
    ),
    "Gauntlets": BombQuestItemData(
        code=0x1C301C,
        type=ItemClassification.progression,
        item_type = 0x0,
        item_index = 0x1C,
        WRAM_address= 0xF3F
    ),

    # Equipment
    "Silver Armor": BombQuestItemData(
        code=0x1C3101,
        type=ItemClassification.useful,
        item_type = 0x1,
        item_index = 0x1,
        WRAM_address= 0xF41
    ),
    "Gold Armor": BombQuestItemData(
        code=0x1C3102,
        type=ItemClassification.useful,
        item_type = 0x1,
        item_index = 0x2,
        WRAM_address= 0xF42
    ),
    "Platnium Armor": BombQuestItemData(
        code=0x1C3103,
        type=ItemClassification.useful,
        item_type = 0x1,
        item_index = 0x3,
        WRAM_address= 0xF43
    ),
    "Teleport Armor": BombQuestItemData(
        code=0x1C3104,
        type=ItemClassification.progression,
        item_type = 0x1,
        item_index = 0x4,
        WRAM_address= 0xF44
    ),
    "Steel Shoes": BombQuestItemData(
        code=0x1C3105,
        type=ItemClassification.progression,
        item_type = 0x1,
        item_index = 0x5,
        WRAM_address= 0xF45
    ),
    "Sneakers": BombQuestItemData(
        code=0x1C3106,
        type=ItemClassification.useful,
        item_type = 0x1,
        item_index = 0x6,
        WRAM_address= 0xF46,
        num_exist= 0
    ),
    "Rocket Shoes": BombQuestItemData(
        code=0x1C3107,
        type=ItemClassification.useful,
        item_type = 0x1,
        item_index = 0x7,
        WRAM_address= 0xF47
    ),
    "Combat Boots": BombQuestItemData(
        code=0x1C3108,
        type=ItemClassification.useful,
        item_type = 0x1,
        item_index = 0x8,
        WRAM_address= 0xF48
    ),
    "Safety Shoes": BombQuestItemData(
        code=0x1C3109,
        type=ItemClassification.progression,
        item_type = 0x1,
        item_index = 0x9,
        WRAM_address= 0xF49
    ),
    "Glasses": BombQuestItemData(
        code=0x1C310A,
        type=ItemClassification.progression,
        item_type = 0x1,
        item_index = 0xA,
        WRAM_address= 0xF4A
    ),
    "Power Bracelets": BombQuestItemData(
        code=0x1C310B,
        type=ItemClassification.progression,
        item_type = 0x1,
        item_index = 0xB,
        WRAM_address= 0xF4B
    ),
    "Scuba Gears": BombQuestItemData(
        code=0x1C310C,
        type=ItemClassification.progression,
        item_type = 0x1,
        item_index = 0xC,
        WRAM_address= 0xF4C
    ),
    "Helmet": BombQuestItemData(
        code=0x1C310D,
        type=ItemClassification.progression,
        item_type = 0x1,
        item_index = 0xD,
        WRAM_address= 0xF4D
    ),
    "Lamp": BombQuestItemData(
        code=0x1C310E,
        type=ItemClassification.progression,
        item_type = 0x1,
        item_index = 0xE,
        WRAM_address= 0xF4E
    ),
    "Full Fire": BombQuestItemData(
        code=0x1C310F,
        type=ItemClassification.progression,
        item_type = 0x1,
        item_index = 0xF,
        WRAM_address= 0xF4F
    ),
    "Leather Armor": BombQuestItemData(
        code=0x1C3110,
        type=ItemClassification.useful,
        item_type = 0x1,
        item_index = 0x10,
        WRAM_address= 0xF50
    ),

    # Components
    "Rubber": BombQuestItemData(
        code=0x1C3201,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0x1,
        WRAM_address= 0xF52
    ),
    "Clock": BombQuestItemData(
        code=0x1C3202,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0x2,
        WRAM_address= 0xF53
    ),
    "Ice Shard": BombQuestItemData(
        code=0x1C3203,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0x3,
        WRAM_address= 0xF54
    ),
    "Poison Ivy": BombQuestItemData(
        code=0x1C3204,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0x4,
        WRAM_address= 0xF55
    ),
    "Boomerang": BombQuestItemData(
        code=0x1C3205,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0x5,
        WRAM_address= 0xF56
    ),
    "Skull": BombQuestItemData(
        code=0x1C3206,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0x6,
        WRAM_address= 0xF57
    ),
    "Explosive Core": BombQuestItemData(
        code=0x1C3207,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0x7,
        WRAM_address= 0xF58,
        stackable= True
    ),
    "Fire": BombQuestItemData(
        code=0x1C3208,
        type=ItemClassification.useful,
        item_type = 0x2,
        item_index = 0x8,
        WRAM_address= 0xF59,
        stackable= True,
        num_exist=16
    ),

    "Armored Jacket": BombQuestItemData(
        code=0x1C3209,
        type=ItemClassification.filler,
        item_type = 0x2,
        item_index = 0x9,
        fillweight= 0.2,
        num_exist= 2,
        WRAM_address= 0xF5A
    ),
    "Stopwatch": BombQuestItemData(
        code=0x1C320A,
        type=ItemClassification.filler,
        item_type = 0x2,
        item_index = 0xA,
        fillweight= 0.3,
        num_exist= 2,
        WRAM_address= 0xF5B
    ),
    # "Flute": BombQuestItemData(
    #     code=0x1C320B,
    #     type=ItemClassification.progression,
    #     item_type = 0x2,
    #     item_index = 0xB,
    #     WRAM_address= 0xF5C
    # ),
    "Heart": BombQuestItemData(
        code=0x1C320C,
        type=ItemClassification.filler,
        item_type = 0x2,
        item_index = 0xC,
        fillweight= 0.2,
        WRAM_address= 0xF5D
    ),
    "Full Heart": BombQuestItemData(
        code=0x1C320D,
        type=ItemClassification.filler,
        item_type = 0x2,
        item_index = 0xD,
        fillweight= 0.5,
        WRAM_address= 0xF5E
    ),
    "White Card": BombQuestItemData(
        code=0x1C320E,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0xE,
        WRAM_address= 0xF5F
    ),
    "Black Card": BombQuestItemData(
        code=0x1C320F,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0xF,
        WRAM_address= 0xF60
    ),
    "Honey Card": BombQuestItemData(
        code=0x1C3210,
        type=ItemClassification.progression,
        item_type = 0x2,
        item_index = 0x10,
        WRAM_address= 0xF61
    ),

    # Concept, not implremented
    "Spaceship Fuel": BombQuestItemData(
        code=0x1C3301,
        type=ItemClassification.progression,
        num_exist=0,
    ),
    "Water Gemstone": BombQuestItemData(
        code=0x1C3302,
        type=ItemClassification.progression,
        num_exist=0,
    ),
    "Thunder Gemstone": BombQuestItemData(
        code=0x1C3303,
        type=ItemClassification.progression,
        num_exist=0,
    ),
    "Wind Gemstone": BombQuestItemData(
        code=0x1C3304,
        type=ItemClassification.progression,
        num_exist=0,
    ),
    "Fire Gemstone": BombQuestItemData(
        code=0x1C3305,
        type=ItemClassification.progression,
        num_exist=0,
    ),


}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
item_id_to_name = {data.code: name for name, data in item_data_table.items() if data.code is not None}
item_filler = [name for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]
item_filler_weight = [data.fillweight for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]

item_WRAM_address = {data.code: data.WRAM_address for name, data in item_data_table.items() if data.code is not None and data.WRAM_address is not None}
item_index = {name: [data.item_type, data.item_index] for name, data in item_data_table.items() if (data.code is not None and data.item_type is not None and data.item_index is not None)}
item_stackable = [data.code for name, data in item_data_table.items() if data.stackable== True]

base_index = [0x00, 0x1D, 0x2E]
item_sythesis_index = {name: (base_index[data.item_type] + data.item_index) for name, data in item_data_table.items() if (data.code is not None and data.item_type is not None and data.item_index is not None)}
item_card_index = {name: (data.WRAM_address & 0xFF) for name, data in item_data_table.items() if data.code is not None and data.WRAM_address is not None}
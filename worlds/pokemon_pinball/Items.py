from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification
# Testing 2
if TYPE_CHECKING:
    from . import PokePinballWorld
    
route_list = [
    "Viridian Forest",
    "Pewter City",
    "Mt Moon",
    "Cerulean City",
    "Vermilion City Seaside",
    "Vermilion City Streets",
    "Rock Mountain",
    "Lavender Town",
    "Celadon City",
    "Cycling Road",
    "Fuchsia City",
    "Safari Zone",
    "Saffron City",
    "Seafoam Islands",
    "Cinnabar Island",
    "Indigo Plateau"
]

class PokePinballItem(Item):
    game = "Pokemon Pinball"

class PokePinballItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[["PokePinballWorld"], bool] = lambda world: True
    recv_text: str = ""
    fillweight: Optional[float] = None

item_data_table: Dict[str, PokePinballItemData] = {
    
#    "Viridian City": PokePinballItemData(
#        code=0x1C2001,
#        type=ItemClassification.progression,
#        recv_text = "You can travel to Viridian City!"
#    ),
    "Viridian Forest": PokePinballItemData(
        code=0x1C2002,
        type=ItemClassification.progression,
        recv_text = "You can travel to Viridian Forest!"
    ),
    "Pewter City": PokePinballItemData(
        code=0x1C2003,
        type=ItemClassification.progression,
        recv_text= "You can travel to Pewter City!"
    ),
    "Mt Moon": PokePinballItemData(
        code=0x1C2004,
        type=ItemClassification.progression,
        recv_text= "You can travel to Mt Moon!"
    ),
    "Cerulean City": PokePinballItemData(
        code=0x1C2005,
        type=ItemClassification.progression,
        recv_text= "You can travel to Cerulean City!"
    ),
    "Vermilion City Seaside": PokePinballItemData(
        code=0x1C2006,
        type=ItemClassification.progression,
        recv_text= "You can travel to Vermilion City Seaside!"
    ),
    "Vermilion City Streets": PokePinballItemData(
        code=0x1C2007,
        type=ItemClassification.progression,
        recv_text= "You can travel to Vermilion City Streets!"
    ),
    "Rock Mountain": PokePinballItemData(
        code=0x1C2008,
        type=ItemClassification.progression,
        recv_text= "You can travel to Rock Mountain!"
    ),
    "Lavender Town": PokePinballItemData(
        code=0x1C2009,
        type=ItemClassification.progression,
        recv_text= "You can travel to Lavender Town!"
    ),
    "Celadon City": PokePinballItemData(
        code=0x1C200A,
        type=ItemClassification.progression,
        recv_text= "You can travel to Celadon City!"
    ),
    "Cycling Road": PokePinballItemData(
        code=0x1C200B,
        type=ItemClassification.progression,
        recv_text= "You can travel to Cycling Road!"
    ),
    "Fuchsia City": PokePinballItemData(
        code=0x1C200C,
        type=ItemClassification.progression,
        recv_text= "You can travel to Fuchsia City!"
    ),
    "Safari Zone": PokePinballItemData(
        code=0x1C200D,
        type=ItemClassification.progression,
        recv_text= "You can travel to Safari Zone!"
    ),
    "Saffron City": PokePinballItemData(
        code=0x1C200E,
        type=ItemClassification.progression,
        recv_text= "You can travel to Saffron City!"
    ),
    "Seafoam Islands": PokePinballItemData(
        code=0x1C200F,
        type=ItemClassification.progression,
        recv_text= "You can travel to Seafoam Islands!"
    ),
    "Cinnabar Island": PokePinballItemData(
        code=0x1C2010,
        type=ItemClassification.progression,
        recv_text= "You can travel to Cinnabar Island!"
    ),
    "Indigo Plateau": PokePinballItemData(
        code=0x1C2011,
        type=ItemClassification.progression,
        recv_text= "You can travel to Indigo Plateau!"
    ),
    "Red Table": PokePinballItemData(
        code=0x1C2012,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Blue Table": PokePinballItemData(
        code=0x1C2013,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Oaks Notes": PokePinballItemData(
        code=0x1C2020,
        type=ItemClassification.useful,
        recv_text= "Oak is ready to research!",
        num_exist=0,
    ),
    "Extra Ball": PokePinballItemData(
        code=0x1C2030,
        type=ItemClassification.filler,
        fillweight=0.1,
        recv_text= "Recieved Extra Ball!",
        num_exist=0,
    ),
    "Pika Power": PokePinballItemData(
        code=0x1C2031,
        type=ItemClassification.filler,
        fillweight=0.2,
        recv_text= "Recieved Pika Power!",
        num_exist=0,
    ),
    "Ball Saver": PokePinballItemData(
        code=0x1C2032,
        type=ItemClassification.filler,
        fillweight=0.5,
        recv_text= "Recieved Ball Saver!",
        num_exist=0,
    ),
    "Slots": PokePinballItemData(
        code=0x1C2033,
        type=ItemClassification.filler,
        fillweight=0.5,
        recv_text= "Slots are open!",
        num_exist=0,
    ),
    "Catchem Mode": PokePinballItemData(
        code=0x1C2034,
        type=ItemClassification.filler,
        fillweight=0.4,
        #recv_text= "Gotta Catch em All!",
        num_exist=0,
    ),
    "Evolution Mode": PokePinballItemData(
        code=0x1C2035,
        type=ItemClassification.filler,
        fillweight=0.3,
        #recv_text= "Gotta Catch em All!",
        num_exist=0,
    ),
    "Bonus Multiplier": PokePinballItemData(
        code=0x1C2036,
        type=ItemClassification.filler,
        fillweight=0.4,
        recv_text= "Bonus Multiplier!",
        num_exist=0,
    ),
    "Ball Upgrade": PokePinballItemData(
        code=0x1C2038,
        type=ItemClassification.filler,
        fillweight=0.5,
        num_exist = 0,
        #recv_text = "Recieved Ball Upgrade!"
    ),
    #"Victory": PokePinballItemData(
    #   code=0x1C203F,
     #   type=ItemClassification.progression,
    #    num_exist=0
    #),

}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
item_id_to_name = {data.code: name for name, data in item_data_table.items() if data.code is not None}
item_recv_text = {data.code: data.recv_text for name, data in item_data_table.items() if data.recv_text is not None}
item_filler = [name for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]
item_filler_weight = [data.fillweight for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]
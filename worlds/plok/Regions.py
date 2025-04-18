from typing import NamedTuple, Callable, List, Dict
from BaseClasses import CollectionState


class PlokRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, PlokRegionData] = {
    "Menu": PlokRegionData(["Cotton Island"]),
    "Cotton Island": PlokRegionData(["Akrillic"]),
    "Akrillic": PlokRegionData(["Legacy Island", "Akrillic Cave",
        "Garlen Beach","Sleepy Dale",
        "Plok Town","Venge Thicket","Dreamy Cove",]),
    "Akrillic Cave": PlokRegionData(["Flea Pit",
        "Creepy Forest","Creepy Crag","Gohome Cavern","Crashing Rocks"]),
    "Legacy Island": PlokRegionData([]),
    "Flea Pit": PlokRegionData(["Cycling Clever","Road Hogging","High Flying",
                                "Easy Riding","In A Spin","Real Rumblings","Silent Running"]),

    # Akrillic
    "Garlen Beach": PlokRegionData([]),
    "Sleepy Dale": PlokRegionData([]),
    "Plok Town": PlokRegionData([]),
    "Venge Thicket": PlokRegionData([]),
    "Dreamy Cove": PlokRegionData([]),

    "Creepy Forest": PlokRegionData([]),
    "Creepy Crag": PlokRegionData([]),
    "Gohome Cavern": PlokRegionData([]),
    "Crashing Rocks": PlokRegionData([]),

    # Flea Pit
    "Cycling Clever": PlokRegionData([]),
    "Road Hogging": PlokRegionData([]),
    "High Flying": PlokRegionData([]),
    "Easy Riding": PlokRegionData([]),
    "In A Spin": PlokRegionData([]),
    "Real Rumblings": PlokRegionData([]),
    "Silent Running": PlokRegionData([]),
}


def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit

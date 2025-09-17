from typing import Dict, List, NamedTuple


class BombQuestRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, BombQuestRegionData] = {
    "Menu": BombQuestRegionData(["Peece Town"]),
    "Peece Town": BombQuestRegionData(["Field C4","Forest E3", "Beach F5","Desert D6","Space"]),

    # Field Zone
    "Field A1": BombQuestRegionData(["Field A2"]),
    "Field A2": BombQuestRegionData(["Field A1","Field A3"]),
    "Field A3": BombQuestRegionData(["Field A2","Field B3"]),
    "Field A4": BombQuestRegionData(["Field B4", "Field A4 Ruins Depths"]),
    
    "Field A4 Ruins Depths": BombQuestRegionData(["Field A4"]),

    "Field B1": BombQuestRegionData(["Field B2","Field C1"]),
    "Field B2": BombQuestRegionData(["Field B1","Field C2"]),
    "Field B3": BombQuestRegionData(["Field B4","Field A3","Field C3"]),
    "Field B4": BombQuestRegionData(["Field A4","Field B3","Field C4"]),

    "Field C1": BombQuestRegionData(["Field B1","Field D1"]),
    "Field C2": BombQuestRegionData(["Field B2","Field C3"]),
    "Field C3": BombQuestRegionData(["Field B3","Field C2"]),
    "Field C4": BombQuestRegionData(["Field B4","Peece Town", "Desert C5"]),

    "Field D1": BombQuestRegionData(["Field C1","Field D2"]),
    "Field D2": BombQuestRegionData(["Field D1","Field D3"]),
    "Field D3": BombQuestRegionData(["Field D2","Forest E3","Water Base"]),
    "Water Base": BombQuestRegionData(["Field D3"]),

    # Forest Zone
    "Forest E1": BombQuestRegionData(["Forest F1","Forest E2"]),
    "Forest E2": BombQuestRegionData(["Forest E1","Forest F2"]),
    "Forest E3": BombQuestRegionData(["Forest F3","Field D3","Peece Town"]),

    "Forest F1": BombQuestRegionData(["Forest E1","Forest F2","Forest G1"]),
    "Forest F2": BombQuestRegionData(["Forest F1","Forest E2","Forest F3"]),
    "Forest F3": BombQuestRegionData(["Forest E3","Forest F2"]),
    "Forest F4": BombQuestRegionData(["Forest G4","Thunder Base","Beach F5"]),

    "Forest G1": BombQuestRegionData(["Forest F1","Forest G2"]),
    "Forest G2": BombQuestRegionData(["Forest G1","Forest H2"]),
    "Forest G3": BombQuestRegionData(["Forest H3","Forest G4"]),
    "Forest G4": BombQuestRegionData(["Forest G3","Forest F4"]),

    "Forest H1": BombQuestRegionData(["Forest H2"]),
    "Forest H2": BombQuestRegionData(["Forest G2","Forest H1", "Forest H3"]),
    "Forest H3": BombQuestRegionData(["Forest H2","Forest H4","Forest G3"]),
    "Forest H4": BombQuestRegionData(["Forest H3","Beach H5"]),

    "Thunder Base": BombQuestRegionData(["Forest F4", "Thunder Base 2"]),
    "Thunder Base 2": BombQuestRegionData(["Thunder Base","Thunder Base 3"]),
    "Thunder Base 3": BombQuestRegionData(["Thunder Base 2","Thunder Base 4"]),
    "Thunder Base 4": BombQuestRegionData(["Thunder Base 3","Thunder Base 5"]),
    "Thunder Base 5": BombQuestRegionData(["Thunder Base 4","Thunder Base 6"]),
    "Thunder Base 6": BombQuestRegionData(["Thunder Base 5","Thunder Base 7"]),
    "Thunder Base 7": BombQuestRegionData(["Thunder Base 6"]),

    # Beach Zone
    "Beach E6": BombQuestRegionData(["Beach E7","Desert D6","Wind Base"]),
    "Beach E7": BombQuestRegionData(["Beach E6","Beach E8","Beach F7"]),
    "Beach E8": BombQuestRegionData(["Beach F8","Beach E7"]),

    "Beach F5": BombQuestRegionData(["Forest F4","Peece Town","Beach G5"]),
    "Beach F6": BombQuestRegionData(["Beach G7"]),
    "Beach F7": BombQuestRegionData(["Beach F8","Beach E7"]),
    "Beach F8": BombQuestRegionData(["Beach G8","Beach F7","Beach E8"]),

    "Beach G5": BombQuestRegionData(["Beach G6","Beach F5"]),
    "Beach G6": BombQuestRegionData(["Beach G5","Beach G7",]),
    "Beach G7": BombQuestRegionData(["Beach F6","Beach H6","Beach G6"]),
    "Beach G8": BombQuestRegionData(["Beach H8","Beach F8"]),

    "Beach H5": BombQuestRegionData(["Forest H4"]),
    "Beach H6": BombQuestRegionData(["Beach G7","Beach H7", "Beach Cavern"]),
    "Beach H7": BombQuestRegionData(["Beach H6","Beach H8"]),
    "Beach H8": BombQuestRegionData(["Beach H7","Beach G8"]),

    "Wind Base": BombQuestRegionData(["Beach E6","Wind Base 2"]),
    "Wind Base 2": BombQuestRegionData(["Wind Base", "Wind Base 3"]),
    "Wind Base 3": BombQuestRegionData(["Wind Base 2", "Wind Base 4"]),
    "Wind Base 4": BombQuestRegionData(["Wind Base 3", "Wind Base 5"]),
    "Wind Base 5": BombQuestRegionData(["Wind Base 4", "Wind Base 6", "Wind Base 8"]),
    "Wind Base 6": BombQuestRegionData(["Wind Base 5", "Wind Base 7"]),
    "Wind Base 7": BombQuestRegionData(["Wind Base 6"]),
    "Wind Base 8": BombQuestRegionData(["Wind Base 5", "Wind Base 9"]),
    "Wind Base 9": BombQuestRegionData(["Wind Base 8"]),

    "Beach Cavern": BombQuestRegionData(["Beach H6","Beach Cavern 2"]),
    "Beach Cavern 2": BombQuestRegionData(["Beach Cavern","Beach Cavern 3"]),
    "Beach Cavern 3": BombQuestRegionData(["Beach Cavern 2","Beach Cavern 4"]),
    "Beach Cavern 4": BombQuestRegionData(["Beach Cavern 3"]),


    # Desert Zone
    "Desert A5": BombQuestRegionData(["Desert A6"]),
    "Desert A6": BombQuestRegionData(["Desert A5","Desert A7","Desert B6"]),
    "Desert A7": BombQuestRegionData(["Desert A8","Desert A6"]),
    "Desert A8": BombQuestRegionData(["Desert A7","Desert B8"]),

    "Desert B5": BombQuestRegionData(["Desert B6","Desert C5"]),
    "Desert B6": BombQuestRegionData(["Desert B5","Desert A6"]),
    "Desert B7": BombQuestRegionData(["Desert C6"]),
    "Desert B8": BombQuestRegionData(["Desert C8","Desert A8"]),

    "Desert C5": BombQuestRegionData(["Fire Base","Desert B5","Field C4"]),
    "Desert C6": BombQuestRegionData(["Desert B7"]),
    "Desert C7": BombQuestRegionData(["Desert C8","Desert C6"]),
    "Desert C8": BombQuestRegionData(["Desert B8","Desert D8","Desert C7"]),

    "Desert D6": BombQuestRegionData(["Peece Town","Desert D7","Beach E6"]),
    "Desert D7": BombQuestRegionData(["Desert D6","Desert D8"]),
    "Desert D8": BombQuestRegionData(["Desert D7","Desert C8"]),

    "Fire Base": BombQuestRegionData(["Desert C5", "Fire Base 2"]),
    "Fire Base 2": BombQuestRegionData(["Fire Base", "Fire Base 5"]),
    "Fire Base 3": BombQuestRegionData(["Fire Base 4", "Fire Base 6", "Fire Base 7"]),
    "Fire Base 4": BombQuestRegionData(["Fire Base 3"]),
    "Fire Base 5": BombQuestRegionData(["Fire Base 2", "Fire Base 6"]),
    "Fire Base 6": BombQuestRegionData(["Fire Base 3", "Fire Base 5"]),
    "Fire Base 7": BombQuestRegionData(["Fire Base 3", "Fire Base 8"]),
    "Fire Base 8": BombQuestRegionData(["Fire Base 7", "Fire Base 9"]),
    "Fire Base 9": BombQuestRegionData(["Fire Base 8", "Fire Base 10"]),
    "Fire Base 10": BombQuestRegionData(["Fire Base 9"]),

    "Space": BombQuestRegionData(),
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit
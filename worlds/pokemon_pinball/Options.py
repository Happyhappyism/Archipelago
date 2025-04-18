from dataclasses import dataclass
from Options import Choice, Range, Toggle, DefaultOnToggle, Removed, PerGameCommonOptions, OptionSet, StartInventoryPool, DeathLink

class DexGoal(Removed):
    """If enabled will require you to catch a certain number of Pokemon to clear the game"""
    display_name = "Dex Completion Goal"

class DexNeed(Range):
    """Determines how many Pokemon you need to catch to complete the game"""
    display_name = "Dex Completion Requirement"
    range_start = 1
    range_end = 150
    default = 100

class MapMove(Choice):
    """Controls what button is needed to move between areas during gameplay"""
    option_a     = 0b00000001 # A Button
    option_b     = 0b00000010 # B Button
    option_sel   = 0b00000100 # Select Button
    option_start = 0b00001000 # Start Button
    option_right = 0b00010000 # Right Button
    option_left  = 0b00100000 # Left Button
    option_up    = 0b01000000 # Up Button
    option_down  = 0b10000000 # Down Button
    default      = 0b00010000 # Right

class BalanceEncounter(DefaultOnToggle):
    """If enabled, will rebalance the encounter tables to make encountering rarer pokemon more common"""
    display_name = "Balanced Encounters"

class BallSaver(Toggle):
    """If enabled, the game will make the ball saved permanent"""
    display_name = "Permanent Ball Saver"

class DoubleTimer(Toggle):
    """The amount of minutes you have to catch a Pokemon before it runs away"""
    display_name = "Double Timer"

class StrongShake(Toggle):
    """If enabled, increases the strength of tilting, this can produce some odd results so use at your own risk"""

class ColorRando(Toggle):
    """If enabled, the game will randomize the colors of the Pokemon"""
    display_name = "Randomize Pokemon Colors"

class MapColor(Toggle):
    """If enabled, the game will randomize the colors of the maps"""
    display_name = "Randomize Map Colors"

class RequiredMons(OptionSet):
    """Which Pokeon are required to be caught to clear the game, leave blank if you don't want any"""
    valid_keys = {
    "Bulbasaur",
    "Ivysaur",
    "Venusaur",
    "Charmander",
    "Charmeleon",
    "Charizard",
    "Squirtle",
    "Wartortle",
    "Blastoise",
    "Caterpie",
    "Metapod",
    "Butterfree",
    "Weedle",
    "Kakuna",
    "Beedrill",
    "Pidgey",
    "Pidgeotto",
    "Pidgeot",
    "Rattata",
    "Raticate",
    "Spearow",
    "Fearow",
    "Ekans",
    "Arbok",
    "Pikachu",
    "Raichu",
    "Sandshrew",
    "Sandslash",
    "Nidoran Female",
    "Nidorina",
    "Nidoqueen",
    "Nidoran Male",
    "Nidorino",
    "Nidoking",
    "Clefairy",
    "Clefable",
    "Vulpix",
    "Ninetales",
    "Jigglypuff",
    "Wigglytuff",
    "Zubat",
    "Golbat",
    "Oddish",
    "Gloom",
    "Vileplume",
    "Paras",
    "Parasect",
    "Venonat",
    "Venomoth",
    "Diglett",
    "Dugtrio",
    "Meowth",
    "Persian",
    "Psyduck",
    "Golduck",
    "Mankey",
    "Primeape",
    "Growlithe",
    "Arcanine",
    "Poliwag",
    "Poliwhirl",
    "Poliwrath",
    "Abra",
    "Kadabra",
    "Alakazam",
    "Machop",
    "Machoke",
    "Machamp",
    "Bellsprout",
    "Weepinbell",
    "Victreebel",
    "Tentacool",
    "Tentacruel",
    "Geodude",
    "Graveler",
    "Golem",
    "Ponyta",
    "Rapidash",
    "Slowpoke",
    "Slowbro",
    "Magnemite",
    "Magneton",
    "Farfetchd",
    "Doduo",
    "Dodrio",
    "Seel",
    "Dewgong",
    "Grimer",
    "Muk",
    "Shellder",
    "Cloyster",
    "Gastly",
    "Haunter",
    "Gengar",
    "Onix",
    "Drowzee",
    "Hypno",
    "Krabby",
    "Kingler",
    "Voltorb",
    "Electrode",
    "Exeggcute",
    "Exeggutor",
    "Cubone",
    "Marowak",
    "Hitmonlee",
    "Hitmonchan",
    "Lickitung",
    "Koffing",
    "Weezing",
    "Rhyhorn",
    "Rhydon",
    "Chansey",
    "Tangela",
    "Kangaskhan",
    "Horsea",
    "Seadra",
    "Goldeen",
    "Seaking",
    "Staryu",
    "Starmie",
    "Mr Mime",
    "Scyther",
    "Jynx",
    "Electabuzz",
    "Magmar",
    "Pinsir",
    "Tauros",
    "Magikarp",
    "Gyarados",
    "Lapras",
    "Ditto",
    "Eevee",
    "Vaporeon",
    "Jolteon",
    "Flareon",
    "Porygon",
    "Omanyte",
    "Omastar",
    "Kabuto",
    "Kabutops",
    "Aerodactyl",
    "Snorlax",
    "Articuno",
    "Zapdos",
    "Moltres",
    "Dratini",
    "Dragonair",
    "Dragonite",
    "Mewtwo",
    "Mew",
    }

@dataclass
class PokePinballOptions(PerGameCommonOptions):
    #goal_dex: DexGoal
    dex_needed: DexNeed
    required_mons: RequiredMons
    map_btn: MapMove
    rebalance_encounters: BalanceEncounter
    permanent_ball_saver: BallSaver
    strong_tilt: StrongShake
    double_timer: DoubleTimer
    mon_colors: ColorRando
    map_colors: MapColor
    death_link: DeathLink
    

from dataclasses import dataclass
from Options import Choice, Range, Toggle, DefaultOnToggle, Removed, PerGameCommonOptions, OptionSet, StartInventoryPool, DeathLink

class Goal(Choice):
    """Game's Goal
    Engines - Collect all 4 engines by beating the 4 commanders to beat the game
    Chaos Bomber - Defeat every monster then fight chaos bomber to beat the game
    Cards - Collect the 3 Trading Cards and turn them in Peece Town"""
    option_engines = 0
    option_choas_bomber = 1
    option_cards = 2
    display_name = "Goal"

class NeededEngines(Range):
    """Number of engines needed to access the final stage"""
    display_name = "Engines Needed"
    range_start = 0
    range_end = 4
    default = 4

class OpenRegions(DefaultOnToggle):
    """Moves the guards in Peece town and removes the statue barries to allow you to move freely between regions"""

class SpeedStart(DefaultOnToggle):
    """Start with the Sneakers, highly recommended"""

class StartFire(Toggle):
    """Start the game with a Fire item"""

class StartHealth(Range):
    """Starting Health"""
    range_start = 1
    range_end = 5
    default = 3

class HealingSave(DefaultOnToggle):
    """Saving the game will heal you"""

class NeededMonsters(Range):
    """Number of monsters needed to defeat to access the final stage"""
    display_name = "Monsters Needed"
    range_start = 0
    range_end = 48
    default = 48

class RandomSound(Toggle):
    """Shuffle sound effects"""

class RandomMusic(Toggle):
    """Shuffle Music"""

class RandomPalette(Toggle):
    """Randomize some colors"""

@dataclass
class BombQuestOptions(PerGameCommonOptions):
    game_goal: Goal
    death_link: DeathLink
    open_regions: OpenRegions
    sneakers_start: SpeedStart
    fire_start: StartFire
    health_start: StartHealth
    save_heal: HealingSave
    sound_shuffle:RandomSound
    music_shuffle: RandomMusic
    palette_random: RandomPalette
    #needed_monsters: NeededMonsters
    #needed_engines: NeededEngines

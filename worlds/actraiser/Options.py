from typing import Dict
from dataclasses import dataclass
from Options import Choice, Option, Range, Toggle, DefaultOnToggle, StartInventoryPool, PerGameCommonOptions, DeathLink, Removed

#class Goal(Choice):
#    display_name = "Goal"
#    option_death_heim = 0
#    option_population = 1
#    default = 0

class PopulationGoal(DefaultOnToggle):
    """If enabled will require you to reach a certain population count 
    set by the Population Goal Count option to clear the game"""
    display_name = "Goal Requires Population Count"

class CrystalGoal(Toggle):
    """If enabled will require you to have a certain number of Dheim Crystals
    set by the Crystal Count option"""
    display_name = "Goal Requires Dheim Crystals"

class DheimRequire(DefaultOnToggle):
    """If enabled will require you to visit Deathheim after reaching all goal requirements
    to clear the game"""
    display_name = "Tanzra Required"

class CrystalBoss(DefaultOnToggle):
    """If enabled it will place 6 of the Dheim crystals on the act 2 bosses"""
    display_name = "Boss Crystals"

class CrystalCount(Range):
    """Number of Dheim Crystals required to access Death Heim, 
    if Pool Crystal is disabled this value should not exceed 6"""
    display_name = "Crystal Count"
    range_start = 6
    range_end = 40
    default = 6

class MaxCrystal(Range):
    """Total Number of Dheim Crystals in the Pool
    Does nothing if you don't have Dheim Crystals as part of your goal"""
    display_name = "Max Crystals"
    range_start = 6
    range_end = 50
    default = 6

class PopGoalCount(Range):
    """Total Population needed to reach the population goal,
    Does nothing if you don't have population goal set"""
    display_name = "Population Goal Count"
    range_start = 250
    range_end = 4652 # Max possible population, logic is not designed for this
    default = 4500 # Amount required for level 17

class ConstructSpeed(Toggle):
    """Reduces the amount of time it takes for construction phases to begin
    enable if you want a slightly faster game"""
    display_name = "Halve Construction Wait Time"

class LevelUps(Range):
    """Amount of Level Up items added into the pool. 
    This is seperate from the Level Up locations that are checks.
    a lower number may result in a slower and harder run"""
    display_name = "Level Count"
    range_start = 9
    range_end = 16
    default = 16

class RandomLevel(Toggle):
    """Randomizes the level requirement to enter each first act of an action stage."""
    display_name = "Random Level Requirement"
    

class MaxLevel(Range):
    """Maximum required level to access a non death heim action stage
    does nothing if you don't have Random Level Requirement enabled
    This value should not exceed Level Count option"""
    display_name = "Max Level Requirement"
    range_start = 10
    range_end = 16
    default = 14

class FlameSword(DefaultOnToggle):
    """Adds a flame sword that is normally only in Aitos Act 1 as a permanent upgrade into the item pool
    This does tend to make the game easier."""
    display_name = "Flame Sword"

class ArrowUpgrades(Range):
    """Adds permanent arrow upgrades into the pool which increase the damage of your arrows"""
    range_start = 0
    range_end = 7
    default = 3

class IncTraps(Toggle):
    """Includes Traps (Only one made so far) Into the Filler item pool"""
    auto_display_name = "Include Traps"

class Catraiser(Toggle):
    """Meow!"""


class RandomMusic(Toggle):
    """Randomized the Music that plays on each map"""
    display_name = "Randomize Music"

class RandomColor(Toggle):
    """Randomized Color Pallettes for many things in the game"""
    display_name = "Randomize Colors"


class RandomObj(Toggle):
    """Randomized Enemies within an action stage"""
    display_name = "Randomize Enemies"

class RandomOrb(Toggle):
    """Randomized Items Dropped From Orbs"""
    display_name = "Randomize Orb Drops"

class RandomLair(Toggle):
    """Randomized Monster Lairs"""
    display_name = "Randomize Lairs"

@dataclass
class ActraiserOptions(PerGameCommonOptions):
    #goal: Goal
    population_goal: PopulationGoal
    crystal_goal: CrystalGoal
    tanzra_require: DheimRequire
    boss_crystal: CrystalBoss
    crystal_count: CrystalCount
    max_crystal: MaxCrystal
    pop_goal_count: PopGoalCount
    fast_construct: ConstructSpeed
    level_count: LevelUps
    random_level: RandomLevel
    max_level: MaxLevel
    fire_sword: FlameSword
    arrow_count: ArrowUpgrades
    include_traps: IncTraps
    catraiser: Catraiser
    random_music: RandomMusic
    random_color: RandomColor
    random_object: RandomObj
    random_orb: RandomOrb
    random_lair: RandomLair
    death_link: DeathLink
    
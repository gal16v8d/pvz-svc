"""Define possible puzzle values in the app"""

from enum import Enum


class PuzzleCategory(str, Enum):
    """Puzzle values"""

    I_ZOMBIE: str = "I, Zombie"
    VASEBREAKER: str = "Vasebreaker"

"""Define possible zombie toughness values in the app"""

from enum import Enum


class ZombieToughness(str, Enum):
    """Toughness values for zombies"""

    EXTREME: str = "extreme"
    EXT_HIGH: str = "extremely high"
    HIGH: str = "high"
    LOW: str = "low"
    MEDIUM: str = "medium"
    VERY_HIGH: str = "very high"

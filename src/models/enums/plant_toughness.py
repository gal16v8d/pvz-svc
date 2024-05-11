"""Define possible toughness values in the app"""

from enum import Enum


class PlantToughness(str, Enum):
    """Toughness values for plants"""

    HIGH: str = "high"
    VERY_HIGH: str = "very high"

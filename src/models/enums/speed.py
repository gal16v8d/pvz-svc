"""Define possible speed values in the app"""

from enum import Enum


class Speed(str, Enum):
    """Speed values"""

    FAST: str = "fast"
    NORMAL: str = "normal"
    SLOW: str = "slow"

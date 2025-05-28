"""Define possible recharge values in the app"""

from enum import Enum


class Recharge(str, Enum):
    """Recharge values"""

    FAST: str = "fast"
    SLOW: str = "slow"
    VERY_SLOW: str = "very slow"

from enum import Enum


class Recharge(str, Enum):
    FAST: str = 'fast'
    SLOW: str = 'slow'
    VERY_SLOW: str = 'very slow'

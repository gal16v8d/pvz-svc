from enum import Enum


class Damage(str, Enum):
    HEAVY: str = 'heavy'
    LIGHT: str = 'light'
    MASSIVE: str = 'massive'
    NORMAL: str = 'normal'
    VERY_HEAVY: str = 'very heavy'
    VERY_LIGHT: str = 'very light'

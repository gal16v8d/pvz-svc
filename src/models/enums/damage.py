from enum import Enum


class Damage(str, Enum):
    HEAVY: str = 'heavy'
    MASSIVE: str = 'massive'
    NORMAL: str = 'normal'
    NORMAL_FOR_EACH: str = 'normal (for each pea)'
    VERY_HEAVY: str = 'very heavy'
    VERY_LIGHT: str = 'very light'

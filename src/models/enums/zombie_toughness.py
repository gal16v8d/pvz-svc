from enum import Enum


class ZombieToughness(str, Enum):
    EXTREME: str = 'extreme',
    EXT_HIGH: str = 'extremely high',
    HIGH: str = 'high',
    LOW: str = 'low',
    MEDIUM: str = 'medium',
    VERY_HIGH: str = 'very high'

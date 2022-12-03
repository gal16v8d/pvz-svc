from enum import Enum


class Speed(str, Enum):
    FAST: str = 'fast'
    NORMAL: str = 'normal'
    SLOW: str = 'slow'

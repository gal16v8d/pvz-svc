from enum import Enum


class Production(str, Enum):
    DOUBLE: str = 'double'
    LOW: str = 'low'
    NORMAL: str = 'normal'

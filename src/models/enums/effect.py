from enum import Enum


class Effect(str, Enum):
    IMMOBILIZE: str = 'immobilizes zombies'
    PENETRATES: str = 'penetrates screen doors'
    SLOWS: str = 'slows zombies'

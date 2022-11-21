from enum import Enum


class Effect(str, Enum):
    INMOBILIZE: str = 'inmobilizes zombies'
    PENETRATES: str = 'penetrates screen doors'
    SLOWS: str = 'slows zombies'

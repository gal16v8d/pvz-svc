'''Define possible effect values in the app'''
from enum import Enum


class Effect(str, Enum):
    '''Effects that some plants can do'''
    IMMOBILIZE: str = 'immobilizes zombies'
    PENETRATES: str = 'penetrates screen doors'
    SLOWS: str = 'slows zombies'

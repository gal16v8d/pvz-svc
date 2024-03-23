'''Define Damage possible values in the app'''
from enum import Enum


class Damage(str, Enum):
    '''Damage that a plant can do to the enemy'''
    HEAVY: str = 'heavy'
    LIGHT: str = 'light'
    MASSIVE: str = 'massive'
    NORMAL: str = 'normal'
    VERY_HEAVY: str = 'very heavy'
    VERY_LIGHT: str = 'very light'

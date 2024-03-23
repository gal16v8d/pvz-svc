'''Define a value for reference in adventure mode'''
from enum import Enum


class AdventureRef(str, Enum):
    '''Represents object to be achieved after pass the level '''
    ITEM: str = 'item'
    PLANT: str = 'plant'

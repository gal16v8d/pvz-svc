'''Define Level model'''
import uuid
from typing import List, Optional

from pydantic import Field
from pymongo import database

from models.base_constraint import BaseConstraint
from models.base_model import PvZBaseModel
from models.enums import AdventureRef


class LevelBase(PvZBaseModel):
    '''Level data'''

    class Config:
        '''Define Swagger config'''
        json_schema_extra = {
            'example': {
                'level': '1-1',
                'unlock': ['uuid'],
                'ref': 'plant',
                'is_minigame': False
            }
        }


class Level(LevelBase):
    '''Fields that can be populated'''
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    level: str = Field(..., min_length=3)
    unlock: List[str] = Field(...)
    ref: AdventureRef = Field(...)
    is_minigame: bool = Field(...)
    notes: Optional[str] = Field(default=None)


class LevelPartial(LevelBase):
    '''Fields that can be updated'''
    level: Optional[str] = Field(default=None)
    unlock: Optional[List[str]] = Field(default=None)
    ref: Optional[AdventureRef] = Field(default=None)
    is_minigame: Optional[bool] = Field(default=None)


class LevelConstraint(BaseConstraint):
    '''Fields that have some constraints for save/update (level)'''
    def __init__(self, db: database.Database) -> None:
        super().__init__(db, 'levels', ['level'])

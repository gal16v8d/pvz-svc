'''Define Puzzle model'''
import uuid
from typing import Optional

from pydantic import Field
from pymongo import database

from consts.constants import NAME
from models.base_constraint import BaseConstraint
from models.base_model import PvZBaseModel
from models.enums import PuzzleCategory


class PuzzleBase(PvZBaseModel):
    '''Puzzle data'''

    class Config:
        '''Define Swagger config'''
        json_schema_extra = {
            'example': {
                'name': 'Vasebreaker',
                'category': 'Vasebreaker',
                'with_streak': 'false'
            }
        }


class Puzzle(PuzzleBase):
    '''Fields that can be populated'''
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(..., min_length=3)
    category: PuzzleCategory = Field(...)
    with_streak: bool = Field(default=False)


class PuzzlePartial(PuzzleBase):
    '''Fields that can be updated'''
    name: Optional[str] = Field(default=None)
    category: Optional[PuzzleCategory] = Field(default=None)
    with_streak: bool = Field(default=False)


class PuzzleConstraint(BaseConstraint):
    '''Fields that have some constraints for save/update (name)'''
    def __init__(self, db: database.Database) -> None:
        super().__init__(db, 'puzzles', [NAME])

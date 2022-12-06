import uuid
from typing import Optional, Any

from pydantic import BaseModel, Field

from consts.constants import NAME, NUMBER
from models.base_constraint import BaseConstraint
from models.enums import *


class LevelBase(BaseModel):

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
        return BaseModel.dict(self, *args, **kwargs)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                'level': '1-1',
                'unlock': ['uuid'],
                'ref': 'plant',
                'is_minigame': False
            }
        }


class Level(LevelBase):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    level: str = Field(..., min_length=3)
    unlock: list[str] = Field(...)
    ref: AdventureRef = Field(...)
    is_minigame: bool = Field(...)
    notes: Optional[str] = Field(default=None)


class LevelPartial(LevelBase):
    level: Optional[str] = Field(default=None)
    unlock: Optional[list[str]] = Field(default=None)
    ref: Optional[AdventureRef] = Field(default=None)
    is_minigame: Optional[bool] = Field(default=None)


class LevelConstraint(BaseConstraint):
    def __init__(self, db: Any, collection: str = 'levels',
                 attrib: str = 'level') -> None:
        super().__init__(db, collection, attrib)

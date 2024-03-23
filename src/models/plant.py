'''Define Plant model'''
import uuid
from typing import List, Optional

from pydantic import BaseModel, Field
from pymongo import database

from consts.constants import NAME, NUMBER
from models.base_constraint import BaseConstraint
from models.base_model import PvZBaseModel
from models.enums import (Damage, Effect, Recharge,
                          Usage, PlantToughness, Production)


class PlantBase(PvZBaseModel):
    '''Plant data'''
    production: Optional[List[Production]] = Field(default=None)
    toughness: Optional[PlantToughness] = Field(default=None)
    damage: Optional[List[Damage]] = Field(default=None)
    damage_notes: Optional[str] = Field(default=None)
    range: Optional[str] = Field(default=None)
    usage: Optional[List[Usage]] = Field(default=None)
    effect: Optional[Effect] = Field(default=None)
    firing_speed: Optional[str] = Field(default=None)
    special: Optional[str] = Field(default=None)
    constraint: Optional[List[str]] = Field(default=None)
    cost: Optional[int] = Field(default=None, ge=0, le=500)
    recharge: Optional[Recharge] = Field(default=None)

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
        return BaseModel.dict(self, *args, **kwargs)

    class Config:
        '''Define Swagger config'''
        json_schema_extra = {
            'example': {
                'name': 'Winter Melons',
                'description': 'Winter Melons do heavy damage '
                'and slow groups of zombies',
                'damage': ['very heavy'],
                'range': 'lobbed',
                'firing_speed': '1/2 x',
                'special': 'Melons damage and freeze nearby enemies on impact',
                'constraint': ['Must be planted on melon-pults'],
                'text': 'Winter Melon tries to calm his nerves.'
                'He hears the zombies approach.'
                'Will he make it? will anyone make it?',
                'cost': 200,
                'recharge': 'very slow'
            }
        }


class Plant(PlantBase):
    '''Fields that can be populated'''
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    number: int = Field(..., ge=0, le=48)
    name: str = Field(..., min_length=3)
    description: str = Field(..., min_length=10)
    text: str = Field(..., min_length=10)


class PlantPartial(PlantBase):
    '''Fields that can be updated'''
    number: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)


class PlantConstraint(BaseConstraint):
    '''Fields that have some constraints for save/update (name/number)'''
    def __init__(self, db: database.Database) -> None:
        super().__init__(db, 'plants', [NAME, NUMBER])

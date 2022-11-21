import uuid
from typing import Optional

from pydantic import BaseModel, Field

from models.enums import Damage, Effect, Recharge, Toughness, Usage


class PlantBase(BaseModel):
    production: Optional[list[str]] = Field(default=None)
    toughness: Optional[Toughness] = Field(default=None)
    damage: Optional[Damage] = Field(default=None)
    range: Optional[str] = Field(default=None)
    usage: Optional[list[Usage]] = Field(default=None)
    effect: Optional[Effect] = Field(default=None)
    firing_speed: Optional[str] = Field(default=None)
    special: Optional[str] = Field(default=None)
    constraint: Optional[list[str]] = Field(default=None)
    cost: Optional[int] = Field(default=None)
    recharge: Optional[Recharge] = Field(default=None)

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
            return BaseModel.dict(self, *args, **kwargs)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                'name': 'Winter Melons',
                'description': 'Winter Melons do heavy damage '
                'and slow groups of zombies',
                'damage': 'very heavy',
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
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(..., min_length=3)
    description: str = Field(..., min_length=10)
    text: str = Field(...)


class PlantPartial(PlantBase):
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)

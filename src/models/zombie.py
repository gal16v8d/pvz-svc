import uuid
from typing import Optional, Any

from pydantic import BaseModel, Field

from consts.constants import NAME, NUMBER
from models.base_constraint import BaseConstraint
from models.enums import *


class ZombieBase(BaseModel):
    description: Optional[str] = Field(default=None)
    toughness_notes: Optional[dict[str, ZombieToughness]] = Field(default=None)
    speed: Optional[list[Speed]] = Field(default=None)
    speed_notes: Optional[str] = Field(default=None)
    special: Optional[str] = Field(default=None)
    weakness: Optional[list[str]] = Field(default=None)
    constraint: Optional[str] = Field(default=None)

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
        return BaseModel.dict(self, *args, **kwargs)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                'name': 'Imp',
                'description': 'Imps are tiny zombies'
                ' hurled by Gargantuar deep into your defenses',
                'toughness': 'low',
                'text': "Imp may be small, but he's wiry."
                "He's proficient in zombie judo, zombie karate"
                " and zombie bare-knuckle brawling. He also "
                "plays the melodica."
            }
        }


class Zombie(ZombieBase):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    number: int = Field(..., ge=1, le=26)
    name: str = Field(..., min_length=3)
    text: str = Field(..., min_length=10)
    toughness: ZombieToughness = Field(...)


class ZombiePartial(ZombieBase):
    number: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)
    toughness: Optional[ZombieToughness] = Field(default=None)


class ZombieNameConstraint(BaseConstraint):
    def __init__(self, db: Any, collection: str = 'zombies',
                 attrib: str = NAME) -> None:
        super().__init__(db, collection, attrib)


class ZombieNumberConstraint(BaseConstraint):
    def __init__(self, db: Any, collection: str = 'zombies',
                 attrib: str = NUMBER) -> None:
        super().__init__(db, collection, attrib)

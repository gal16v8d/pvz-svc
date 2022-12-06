import uuid
from typing import Optional, Any

from pydantic import BaseModel, Field

from consts.constants import NAME, NUMBER
from models.base_constraint import BaseConstraint
from models.enums import *


class ItemBase(BaseModel):

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
        return BaseModel.dict(self, *args, **kwargs)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                'name': 'Shovel',
                'note': 'Let you dig up a plant to make room for another'
            }
        }


class Item(ItemBase):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(..., min_length=3)
    note: str = Field(..., min_length=3)


class ItemPartial(ItemBase):
    name: Optional[str] = Field(default=None)
    note: Optional[str] = Field(default=None)


class ItemConstraint(BaseConstraint):
    def __init__(self, db: Any, collection: str = 'items',
                 attrib: str = NAME) -> None:
        super().__init__(db, collection, attrib)

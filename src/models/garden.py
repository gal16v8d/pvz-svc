import uuid
from typing import Optional, Any

from pydantic import BaseModel, Field

from consts.constants import NAME, NUMBER
from models.base_constraint import BaseConstraint
from models.enums import *


class GardenBase(BaseModel):

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
        return BaseModel.dict(self, *args, **kwargs)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                'number': 1,
                'name': 'Day Garden',
                'max_plants': 32,
                'coin_helper': True
            }
        }


class Garden(GardenBase):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    number: int = Field(..., ge=1, le=4)
    name: str = Field(..., min_length=3)
    max_plants: int = Field(..., ge=1, le=32)
    coin_helper: bool = Field(...)


class GardenPartial(GardenBase):
    number: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    max_plants: Optional[int] = Field(default=None)
    coin_helper: Optional[bool] = Field(default=None)


class GardenNameConstraint(BaseConstraint):
    def __init__(self, db: Any, collection: str = 'gardens',
                 attrib: str = NAME) -> None:
        super().__init__(db, collection, attrib)


class GardenNumberConstraint(BaseConstraint):
    def __init__(self, db: Any, collection: str = 'gardens',
                 attrib: str = NUMBER) -> None:
        super().__init__(db, collection, attrib)

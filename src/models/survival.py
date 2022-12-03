import uuid
from typing import Optional, Any

from pydantic import BaseModel, Field

from consts.constants import NAME
from models.base_constraint import BaseConstraint


class SurvivalBase(BaseModel):

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
        return BaseModel.dict(self, *args, **kwargs)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                'name': 'Survival: Day',
                'flags': 4,
                'endless': False
            }
        }


class Survival(SurvivalBase):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(..., min_length=3)
    flags: Optional[int] = Field(default=None)
    endless: Optional[bool] = Field(default=None)


class SurvivalPartial(SurvivalBase):
    name: Optional[str] = Field(default=None)
    flags: Optional[int] = Field(default=None)
    endless: Optional[bool] = Field(default=None)


class SurvivalConstraint(BaseConstraint):
    def __init__(self, db: Any, collection: str = 'survivals',
                 attrib: str = NAME) -> None:
        super().__init__(db, collection, attrib)

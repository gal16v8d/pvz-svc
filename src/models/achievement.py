import uuid
from typing import Optional

from pydantic import BaseModel, Field


class AchievementBase(BaseModel):

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
            return BaseModel.dict(self, *args, **kwargs)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                'name': 'Home Lawn Security',
                'description': 'Complete adventure mode'
            }
        }


class Achievement(AchievementBase):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(..., min_length=3)
    description: str = Field(..., min_length=10)


class AchievementPartial(AchievementBase):
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

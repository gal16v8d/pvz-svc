import uuid
from typing import Optional

from pydantic import BaseModel, Field
from models.enums import PuzzleCategory


class PuzzleBase(BaseModel):

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
            return BaseModel.dict(self, *args, **kwargs)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                'name': 'Vasebreaker',
                'category': 'Vasebreaker',
                'with_streak': 'false'
            }
        }


class Puzzle(PuzzleBase):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(..., min_length=3)
    category: PuzzleCategory = Field(...)
    with_streak: bool = Field(default=False)


class PuzzlePartial(PuzzleBase):
    name: Optional[str] = Field(default=None)
    category: Optional[PuzzleCategory] = Field(default=None)
    with_streak: bool = Field(default=False)

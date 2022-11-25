import uuid

from pydantic import BaseModel, Field


class MiniGame(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(..., min_length=3)

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get('exclude_none') is not None:
            kwargs['exclude_none'] = True
            return BaseModel.dict(self, *args, **kwargs)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                'name': 'ZomBotany'
            }
        }

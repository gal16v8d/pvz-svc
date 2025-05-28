"""Define base generic model for PvZ models"""

from pydantic import BaseModel as PydanticBaseModel


class PvZBaseModel(PydanticBaseModel):
    """Define common attributes for all the models"""

    def dict(self, *args, **kwargs):
        """Convenient method to transform model to dict"""
        return super().model_dump(*args, **kwargs, exclude_none=True)

    class Config:
        """Define common configuration"""

        populate_by_name = True

"""Define base generic model for PvZ models"""

from pydantic import BaseModel as PydanticBaseModel, ConfigDict


class PvZBaseModel(PydanticBaseModel):
    """Define common attributes for all the models"""

    model_config = ConfigDict(populate_by_name=True)

    def dict(self, *args, **kwargs):
        """Convenient method to transform model to dict"""
        return super().model_dump(*args, **kwargs, exclude_none=True)

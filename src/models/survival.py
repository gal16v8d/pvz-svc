"""Define Survival model"""

import uuid
from typing import Optional

from pydantic import Field
from pymongo import database

from consts.constants import NAME
from models.base_constraint import BaseConstraint
from models.base_model import PvZBaseModel


class SurvivalBase(PvZBaseModel):
    """Survival data"""

    class Config:
        """Define Swagger config"""

        json_schema_extra = {
            "example": {"name": "Survival: Day", "flags": 4, "endless": False}
        }


class Survival(SurvivalBase):
    """Fields that can be populated"""

    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(..., min_length=3)
    flags: Optional[int] = Field(default=None)
    endless: Optional[bool] = Field(default=None)


class SurvivalPartial(SurvivalBase):
    """Fields that can be updated"""

    name: Optional[str] = Field(default=None)
    flags: Optional[int] = Field(default=None)
    endless: Optional[bool] = Field(default=None)


class SurvivalConstraint(BaseConstraint):
    """Fields that have some constraints for save/update (name)"""

    def __init__(self, db: database.Database) -> None:
        super().__init__(db, "survivals", [NAME])

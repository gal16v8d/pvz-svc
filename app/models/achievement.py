"""Define Achievement model"""

import uuid
from typing import Optional

from pydantic import ConfigDict, Field
from pymongo import database

from app.consts.constants import NAME
from app.models.base_model import PvZBaseModel
from app.models.base_constraint import BaseConstraint


class AchievementBase(PvZBaseModel):
    """Achievement data"""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Home Lawn Security",
                "description": "Complete adventure mode",
            }
        }
    )


class Achievement(AchievementBase):
    """Fields that can be populated"""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    name: str = Field(..., min_length=3)
    description: str = Field(..., min_length=10)


class AchievementPartial(AchievementBase):
    """Fields that can be updated"""

    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)


class AchievementConstraint(BaseConstraint):
    """Fields that have some constraints for save/update"""

    def __init__(self, db: database.Database) -> None:
        super().__init__(db, "achievements", [NAME])

"""Define Garden model"""

import uuid
from typing import Optional

from pydantic import ConfigDict, Field
from pymongo import database

from app.consts.constants import NAME, NUMBER
from app.models.base_constraint import BaseConstraint
from app.models.base_model import PvZBaseModel


class GardenBase(PvZBaseModel):
    """Garden data"""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "number": 1,
                "name": "Day Garden",
                "max_plants": 32,
                "coin_helper": True,
            }
        }
    )


class Garden(GardenBase):
    """Fields that can be populated"""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    number: int = Field(..., ge=1, le=4)
    name: str = Field(..., min_length=3)
    max_plants: int = Field(..., ge=1, le=32)
    coin_helper: bool = Field(...)


class GardenPartial(GardenBase):
    """Fields that can be updated"""

    number: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    max_plants: Optional[int] = Field(default=None)
    coin_helper: Optional[bool] = Field(default=None)


class GardenConstraint(BaseConstraint):
    """Fields that have some constraints for save/update (number)"""

    def __init__(self, db: database.Database) -> None:
        super().__init__(db, "gardens", [NAME, NUMBER])

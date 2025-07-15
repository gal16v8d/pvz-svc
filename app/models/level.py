"""Define Level model"""

import uuid
from typing import Optional

from pydantic import ConfigDict, Field
from pymongo import database

from app.models.base_constraint import BaseConstraint
from app.models.base_model import PvZBaseModel
from app.models.enums import AdventureRef


class LevelBase(PvZBaseModel):
    """Level data"""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "level": "1-1",
                "unlock": ["uuid"],
                "ref": "plant",
                "is_minigame": False,
            }
        }
    )


class Level(LevelBase):
    """Fields that can be populated"""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    level: str = Field(..., min_length=3)
    unlock: list[str] = Field(...)
    ref: AdventureRef = Field(...)
    is_minigame: bool = Field(...)
    notes: Optional[str] = Field(default=None)


class LevelPartial(LevelBase):
    """Fields that can be updated"""

    level: Optional[str] = Field(default=None)
    unlock: Optional[list[str]] = Field(default=None)
    ref: Optional[AdventureRef] = Field(default=None)
    is_minigame: Optional[bool] = Field(default=None)


class LevelConstraint(BaseConstraint):
    """Fields that have some constraints for save/update (level)"""

    def __init__(self, db: database.Database) -> None:
        super().__init__(db, "levels", ["level"])

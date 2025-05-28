"""Define Minigame model"""

import uuid

from pydantic import Field
from pymongo import database

from app.consts.constants import NAME
from app.models.base_constraint import BaseConstraint
from app.models.base_model import PvZBaseModel


class MiniGame(PvZBaseModel):
    """MiniGame data"""

    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(..., min_length=3)

    class Config:
        """Define Swagger config"""

        json_schema_extra = {"example": {"name": "ZomBotany"}}


class MiniGameConstraint(BaseConstraint):
    """Fields that have some constraints for save/update (name)"""

    def __init__(self, db: database.Database) -> None:
        super().__init__(db, "minigames", [NAME])

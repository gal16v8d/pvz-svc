"""Define Item model"""

import uuid
from typing import Optional

from pydantic import Field
from pymongo import database

from app.consts.constants import NAME
from app.models.base_constraint import BaseConstraint
from app.models.base_model import PvZBaseModel


class ItemBase(PvZBaseModel):
    """Item data"""

    class Config:
        """Define Swagger config"""

        json_schema_extra = {
            "example": {
                "name": "Shovel",
                "note": "Let you dig up a plant to make room for another",
            }
        }


class Item(ItemBase):
    """Fields that can be populated"""

    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(..., min_length=3)
    note: str = Field(..., min_length=3)


class ItemPartial(ItemBase):
    """Fields that can be updated"""

    name: Optional[str] = Field(default=None)
    note: Optional[str] = Field(default=None)


class ItemConstraint(BaseConstraint):
    """Fields that have some constraints for save/update (name)"""

    def __init__(self, db: database.Database) -> None:
        super().__init__(db, "items", [NAME])

"""Define Zombie model"""

import uuid
from typing import Optional

from pydantic import Field
from pymongo import database

from app.consts.constants import NAME, NUMBER
from app.models.base_constraint import BaseConstraint
from app.models.base_model import PvZBaseModel
from app.models.enums import Speed, ZombieToughness


class ZombieBase(PvZBaseModel):
    """Zombie data"""

    description: Optional[str] = Field(default=None)
    toughness_notes: Optional[dict[str, ZombieToughness]] = Field(default=None)
    speed: Optional[list[Speed]] = Field(default=None)
    speed_notes: Optional[str] = Field(default=None)
    special: Optional[str] = Field(default=None)
    weakness: Optional[list[str]] = Field(default=None)
    constraint: Optional[str] = Field(default=None)

    class Config:
        """Define Swagger config"""

        json_schema_extra = {
            "example": {
                "name": "Imp",
                "description": "Imps are tiny zombies"
                " hurled by Gargantuar deep into your defenses",
                "toughness": "low",
                "text": "Imp may be small, but he's wiry."
                "He's proficient in zombie judo, zombie karate"
                " and zombie bare-knuckle brawling. He also "
                "plays the melodica.",
            }
        }


class Zombie(ZombieBase):
    """Fields that can be populated"""

    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    number: int = Field(..., ge=1, le=26)
    name: str = Field(..., min_length=3)
    text: str = Field(..., min_length=10)
    toughness: ZombieToughness = Field(...)


class ZombiePartial(ZombieBase):
    """Fields that can be updated"""

    number: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)
    toughness: Optional[ZombieToughness] = Field(default=None)


class ZombieConstraint(BaseConstraint):
    """Fields that have some constraints for save/update (name/number)"""

    def __init__(self, db: database.Database) -> None:
        super().__init__(db, "zombies", [NAME, NUMBER])

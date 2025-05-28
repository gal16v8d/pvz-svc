"""Define all the models in a single file"""

from app.models.achievement import AchievementConstraint
from app.models.garden import GardenConstraint
from app.models.item import ItemConstraint
from app.models.level import LevelConstraint
from app.models.minigame import MiniGameConstraint
from app.models.plant import PlantConstraint
from app.models.puzzle import PuzzleConstraint
from app.models.survival import SurvivalConstraint
from app.models.zombie import ZombieConstraint

all_models = [
    AchievementConstraint,
    GardenConstraint,
    ItemConstraint,
    LevelConstraint,
    MiniGameConstraint,
    PlantConstraint,
    PuzzleConstraint,
    SurvivalConstraint,
    ZombieConstraint,
]

'''Define all the models in a single file'''
from models.achievement import AchievementConstraint
from models.garden import GardenConstraint
from models.item import ItemConstraint
from models.level import LevelConstraint
from models.minigame import MiniGameConstraint
from models.plant import PlantConstraint
from models.puzzle import PuzzleConstraint
from models.survival import SurvivalConstraint
from models.zombie import ZombieConstraint

all_models = [AchievementConstraint, GardenConstraint,
              ItemConstraint, LevelConstraint,
              MiniGameConstraint, PlantConstraint,
              PuzzleConstraint, SurvivalConstraint,
              ZombieConstraint]

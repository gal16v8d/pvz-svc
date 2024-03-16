'''Define all the models in a single file'''
from models.achievement import AchievementConstraint
from models.garden import GardenNameConstraint, GardenNumberConstraint
from models.item import ItemConstraint
from models.level import LevelConstraint
from models.minigame import MiniGameConstraint
from models.plant import PlantNameConstraint, PlantNumberConstraint
from models.puzzle import PuzzleConstraint
from models.survival import SurvivalConstraint
from models.zombie import ZombieNameConstraint, ZombieNumberConstraint

all_models = [AchievementConstraint, GardenNameConstraint,
              GardenNumberConstraint, ItemConstraint,
              LevelConstraint, MiniGameConstraint,
              PlantNameConstraint, PlantNumberConstraint,
              PuzzleConstraint, SurvivalConstraint,
              ZombieNameConstraint, ZombieNumberConstraint]

"""Define all the routes in a single file to easily access any of these"""

from app.models.achievement import Achievement, AchievementPartial
from app.models.garden import Garden, GardenPartial
from app.models.item import Item, ItemPartial
from app.models.level import Level, LevelPartial
from app.models.minigame import MiniGame
from app.models.plant import Plant, PlantPartial
from app.models.puzzle import Puzzle, PuzzlePartial
from app.models.survival import Survival, SurvivalPartial
from app.models.zombie import Zombie, ZombiePartial
from app.routes.base_route import BaseRoute
from app.routes.health import health_router

all_routes = [
    health_router,
    BaseRoute("achievements", Achievement, AchievementPartial, Achievement).router,
    BaseRoute("gardens", Garden, GardenPartial, Garden).router,
    BaseRoute("items", Item, ItemPartial, Item).router,
    BaseRoute("levels", Level, LevelPartial, Level).router,
    BaseRoute("minigames", MiniGame, MiniGame, MiniGame).router,
    BaseRoute("plants", Plant, PlantPartial, Plant).router,
    BaseRoute("puzzles", Puzzle, PuzzlePartial, Puzzle).router,
    BaseRoute("survivals", Survival, SurvivalPartial, Survival).router,
    BaseRoute("zombies", Zombie, ZombiePartial, Zombie).router,
]

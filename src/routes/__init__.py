""" Define all the routes in a single file to easily access any of these"""

from routes.health import health_router

from routes.achievement import achievement_router
from routes.garden import garden_router
from routes.item import item_router
from routes.level import level_router
from routes.minigame import minigame_router
from routes.plant import plant_router
from routes.puzzle import puzzle_router
from routes.survival import survival_router
from routes.zombie import zombie_router

all_routes = [
    health_router,
    achievement_router,
    garden_router,
    item_router,
    level_router,
    minigame_router,
    plant_router,
    puzzle_router,
    survival_router,
    zombie_router,
]

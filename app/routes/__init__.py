""" Define all the routes in a single file to easily access any of these"""

from app.routes.health import health_router

from app.routes.achievement import achievement_router
from app.routes.garden import garden_router
from app.routes.item import item_router
from app.routes.level import level_router
from app.routes.minigame import minigame_router
from app.routes.plant import plant_router
from app.routes.puzzle import puzzle_router
from app.routes.survival import survival_router
from app.routes.zombie import zombie_router

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

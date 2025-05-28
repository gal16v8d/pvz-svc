from http import HTTPStatus

from fastapi import Body, Path, Request

from app.models.zombie import Zombie, ZombiePartial

from .base_route import BaseRoute


db_key: str = "zombies"
base_instance = BaseRoute(db_key, Zombie)
zombie_router = base_instance.router


@zombie_router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_description="Create a Zombie",
    response_model=Zombie,
)
def create_zombie(request: Request, zombie: Zombie = Body(...)) -> Zombie:
    return base_instance.create(request, zombie)


@zombie_router.put(
    "/{model_id}", response_description="Update a Zombie", response_model=Zombie
)
def update_zombie(
    request: Request, model_id: str = Path(...), zombie: ZombiePartial = Body(...)
) -> Zombie:
    return base_instance.update(request, model_id, zombie)

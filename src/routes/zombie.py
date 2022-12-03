from http import HTTPStatus

from fastapi import Body, Path, Request
from fastapi.encoders import jsonable_encoder

from models.zombie import Zombie, ZombiePartial

from .base_route import BaseRoute

db_key: str = 'zombies'

base_instance = BaseRoute(db_key, Zombie)
zombie_router = base_instance.router


@zombie_router.post('/', status_code=HTTPStatus.CREATED,
                    response_description='Create a Zombie',
                    response_model=Zombie)
def create_zombie(request: Request, zombie: Zombie = Body(...)) -> Zombie:
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(zombie)
    return base_instance.create(request, enc_data)


@zombie_router.put('/{id}',
                   response_description='Update a Zombie',
                   response_model=Zombie)
def update_zombie(request: Request, id: str = Path(...),
                  zombie: ZombiePartial = Body(...)) -> Zombie:
    base_instance.validate_env(request)
    zombie = {k: v for k, v in zombie.dict().items() if v is not None}
    return base_instance.update(request, id, zombie)

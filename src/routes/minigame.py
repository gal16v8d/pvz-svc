from http import HTTPStatus

from fastapi import Body, Path, Request
from fastapi.encoders import jsonable_encoder

from models.minigame import MiniGame

from .base_route import BaseRoute


db_key: str = 'minigames'
base_instance = BaseRoute(db_key, MiniGame)
minigame_router = base_instance.router


@minigame_router.post('/', status_code=HTTPStatus.CREATED,
                      response_description='Create a MiniGame',
                      response_model=MiniGame)
def create_minigame(request: Request, minigame: MiniGame = Body(...)
                    ) -> MiniGame:
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(minigame)
    return base_instance.create(request, enc_data)


@minigame_router.put('/{model_id}',
                     response_description='Update a MiniGame',
                     response_model=MiniGame)
def update_minigame(request: Request, model_id: str = Path(...),
                    minigame: MiniGame = Body(...)) -> MiniGame:
    base_instance.validate_env(request)
    minigame = {k: v for k, v in minigame.dict().items() if v is not None}
    return base_instance.update(request, model_id, minigame)

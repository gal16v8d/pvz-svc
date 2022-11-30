from http import HTTPStatus

from fastapi import Body, Request, Path
from fastapi.encoders import jsonable_encoder

from models.minigame import MiniGame

from .base_route import BaseRoute

db_key: str = 'minigames'

base_instance = BaseRoute(db_key, MiniGame)
minigame_router = base_instance.router


@minigame_router.post('/', status_code=HTTPStatus.CREATED,
                      response_description='Create a MiniGame',
                      response_model=MiniGame)
def create_survival(request: Request, minigame: MiniGame = Body(...)
                    ) -> MiniGame:
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(minigame)
    new_data = request.app.database[db_key].insert_one(enc_data)
    created_data: MiniGame = request.app.database[db_key].find_one(
        {'_id': new_data.inserted_id}
    )
    return created_data


@minigame_router.put('/{id}',
                     response_description='Update a MiniGame',
                     response_model=MiniGame)
def update_puzzle(request: Request, id: str = Path(...),
                  minigame: MiniGame = Body(...)) -> MiniGame:
    base_instance.validate_env(request)
    minigame = {k: v for k, v in minigame.dict().items() if v is not None}
    if len(minigame) >= 1:
        update_result = request.app.database[db_key].update_one(
            {'_id': id}, {'$set': minigame}
        )

        if update_result.modified_count == 0:
            base_instance.id_not_found(id)

    return base_instance.find_by_id(request, id)

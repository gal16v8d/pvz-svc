from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Body, HTTPException, Request, Response, Path
from fastapi.encoders import jsonable_encoder

from consts import constants
from models.minigame import MiniGame

db_key: str = 'minigames'

minigame_router: APIRouter = APIRouter(
    tags=['minigames'],
    prefix='/api/minigames',
)


@minigame_router.get('/',
                     response_description='List all minigames',
                     response_model=List[MiniGame])
def list_minigame(request: Request) -> List[MiniGame]:
    return list(request.app.database[db_key].find())


@minigame_router.get('/{id}',
                     response_description='Get a single minigame by id',
                     response_model=MiniGame)
def find_minigame(request: Request, id: str = Path(...)) -> MiniGame:
    '''
    List a MiniGame by id

    This one check in our app db using the id if it exists or not.

    Parameters:
    - **id:uuid** -> Object uuid to find a MiniGame in db.

    Returns the MiniGame if found, else a not found with a custom message.
    '''
    if (
        existing_data :=
        request.app.database[db_key].find_one({'_id': id})
    ) is not None:
        return existing_data

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                        detail=f'MiniGame with ID {id} not found')


@minigame_router.post('/', status_code=HTTPStatus.CREATED,
                      response_description='Create a MiniGame',
                      response_model=MiniGame)
def create_minigame(request: Request, minigame: MiniGame = Body(...)
                    ) -> MiniGame:
    if (request.app.env == 'dev'):
        enc_data = jsonable_encoder(minigame)
        new_data = request.app.database[db_key].insert_one(enc_data)
        created_data: MiniGame = request.app.database[db_key].find_one(
            {'_id': new_data.inserted_id}
        )
        return created_data

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)


@minigame_router.put('/{id}',
                     response_description='Update a MiniGame',
                     response_model=MiniGame)
def update_minigame(request: Request, id: str = Path(...),
                    minigame: MiniGame = Body(...)) -> MiniGame:
    if (request.app.env == 'dev'):
        minigame = {k: v for k, v in minigame.dict().items() if v is not None}
        if len(minigame) >= 1:
            update_result = request.app.database[db_key].update_one(
                {'_id': id}, {'$set': minigame}
            )

            if update_result.modified_count == 0:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'MiniGame with ID {id} not found')

        return find_minigame(request, id)

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)


@minigame_router.delete('/{id}', response_description='Delete a Minigame')
def delete_minigame(request: Request, response: Response,
                    id: str = Path(...)) -> Response:
    if (request.app.env == 'dev'):
        delete_result = request.app.database[db_key].delete_one({
            '_id': id})

        if delete_result.deleted_count == 1:
            response.status_code = HTTPStatus.NO_CONTENT
            return response

        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f'MiniGame with ID {id} not found')

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)

from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Body, HTTPException, Request, Response, Path
from fastapi.encoders import jsonable_encoder

from consts import constants
from models.puzzle import Puzzle, PuzzlePartial

db_key: str = 'puzzles'

puzzle_router: APIRouter = APIRouter(
    tags=['puzzles'],
    prefix='/api/puzzles',
)


@puzzle_router.get('/',
                   response_description='List all puzzles',
                   response_model=List[Puzzle])
def list_puzzle(request: Request) -> List[Puzzle]:
    return list(request.app.database[db_key].find())


@puzzle_router.get('/{id}',
                   response_description='Get a single puzzle by id',
                   response_model=Puzzle)
def find_puzzle(request: Request, id: str = Path(...)) -> Puzzle:
    '''
    List a Puzzle by id

    This one check in our app db using the id if it exists or not.

    Parameters:
    - **id:uuid** -> Object uuid to find a Puzzle in db.

    Returns the Puzzle if found, else a not found with a custom message.
    '''
    if (
        existing_data :=
        request.app.database[db_key].find_one({'_id': id})
    ) is not None:
        return existing_data

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                        detail=f'Puzzle with ID {id} not found')


@puzzle_router.post('/', status_code=HTTPStatus.CREATED,
                    response_description='Create a Puzzle',
                    response_model=Puzzle)
def create_puzzle(request: Request, puzzle: Puzzle = Body(...)) -> Puzzle:
    if (request.app.env == 'dev'):
        enc_data = jsonable_encoder(puzzle)
        new_data = request.app.database[db_key].insert_one(enc_data)
        created_data: Puzzle = request.app.database[db_key].find_one(
            {'_id': new_data.inserted_id}
        )
        return created_data

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)


@puzzle_router.put('/{id}',
                   response_description='Update a Puzzle',
                   response_model=Puzzle)
def update_puzzle(request: Request, id: str = Path(...),
                  puzzle: PuzzlePartial = Body(...)) -> Puzzle:
    if (request.app.env == 'dev'):
        puzzle = {k: v for k, v in puzzle.dict().items() if v is not None}
        if len(puzzle) >= 1:
            update_result = request.app.database[db_key].update_one(
                {'_id': id}, {'$set': puzzle}
            )

            if update_result.modified_count == 0:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'Puzzle with ID {id} not found')

        return find_puzzle(request, id)

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)


@puzzle_router.delete('/{id}', response_description='Delete a Puzzle')
def delete_puzzle(request: Request, response: Response,
                  id: str = Path(...)) -> Response:
    if (request.app.env == 'dev'):
        delete_result = request.app.database[db_key].delete_one({
            '_id': id})

        if delete_result.deleted_count == 1:
            response.status_code = HTTPStatus.NO_CONTENT
            return response

        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f'Puzzle with ID {id} not found')

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)

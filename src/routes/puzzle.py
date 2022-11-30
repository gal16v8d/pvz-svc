from http import HTTPStatus

from fastapi import Body, Request, Path
from fastapi.encoders import jsonable_encoder

from models.puzzle import Puzzle, PuzzlePartial

from .base_route import BaseRoute

db_key: str = 'puzzles'

base_instance = BaseRoute(db_key, Puzzle)
puzzle_router = base_instance.router


@puzzle_router.post('/', status_code=HTTPStatus.CREATED,
                    response_description='Create a Puzzle',
                    response_model=Puzzle)
def create_puzzle(request: Request, puzzle: Puzzle = Body(...)) -> Puzzle:
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(puzzle)
    new_data = request.app.database[db_key].insert_one(enc_data)
    created_data: Puzzle = request.app.database[db_key].find_one(
        {'_id': new_data.inserted_id}
    )
    return created_data


@puzzle_router.put('/{id}',
                   response_description='Update a Puzzle',
                   response_model=Puzzle)
def update_puzzle(request: Request, id: str = Path(...),
                  puzzle: PuzzlePartial = Body(...)) -> Puzzle:
    base_instance.validate_env(request)
    puzzle = {k: v for k, v in puzzle.dict().items() if v is not None}
    if len(puzzle) >= 1:
        update_result = request.app.database[db_key].update_one(
            {'_id': id}, {'$set': puzzle}
        )

        if update_result.modified_count == 0:
            base_instance.id_not_found(id)

    return base_instance.find_by_id(request, id)

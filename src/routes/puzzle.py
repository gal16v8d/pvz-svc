from http import HTTPStatus

from fastapi import Body, Path, Request
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
    return base_instance.create(request, enc_data)


@puzzle_router.put('/{model_id}',
                   response_description='Update a Puzzle',
                   response_model=Puzzle)
def update_puzzle(request: Request, model_id: str = Path(...),
                  puzzle: PuzzlePartial = Body(...)) -> Puzzle:
    base_instance.validate_env(request)
    puzzle = {k: v for k, v in puzzle.dict().items() if v is not None}
    return base_instance.update(request, model_id, puzzle)

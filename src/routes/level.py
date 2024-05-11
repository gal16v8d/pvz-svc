from http import HTTPStatus

from fastapi import Body, Path, Request
from fastapi.encoders import jsonable_encoder

from models.level import Level, LevelPartial

from .base_route import BaseRoute


db_key: str = "levels"
base_instance = BaseRoute(db_key, Level)
level_router = base_instance.router


@level_router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_description="Create a Level",
    response_model=Level,
)
def create_adventure(request: Request, level: Level = Body(...)) -> Level:
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(level)
    return base_instance.create(request, enc_data)


@level_router.put(
    "/{model_id}", response_description="Update a Level", response_model=Level
)
def update_adventure(
    request: Request, model_id: str = Path(...), level: LevelPartial = Body(...)
) -> Level:
    base_instance.validate_env(request)
    level = {k: v for k, v in level.dict().items() if v is not None}
    return base_instance.update(request, model_id, level)

from http import HTTPStatus

from fastapi import Body, Path, Request

from app.models.level import Level, LevelPartial

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
    return base_instance.create(request, level)


@level_router.put(
    "/{model_id}", response_description="Update a Level", response_model=Level
)
def update_adventure(
    request: Request, model_id: str = Path(...), level: LevelPartial = Body(...)
) -> Level:
    return base_instance.update(request, model_id, level)

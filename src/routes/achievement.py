"""Route for achievements api"""

from http import HTTPStatus

from fastapi import Body, Path, Request
from fastapi.encoders import jsonable_encoder

from models.achievement import Achievement, AchievementPartial

from .base_route import BaseRoute


db_key: str = "achievements"
base_instance = BaseRoute(db_key, Achievement)
achievement_router = base_instance.router


@achievement_router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_description="Create an Achievement",
    response_model=Achievement,
)
def create_achievement(
    request: Request, achievement: Achievement = Body(...)
) -> Achievement:
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(achievement)
    return base_instance.create(request, enc_data)


@achievement_router.put(
    "/{model_id}",
    response_description="Update an Achievement",
    response_model=Achievement,
)
def update_achievement(
    request: Request,
    model_id: str = Path(...),
    achievement: AchievementPartial = Body(...),
) -> Achievement:
    base_instance.validate_env(request)
    achievement = {k: v for k, v in achievement.dict().items() if v is not None}
    return base_instance.update(request, model_id, achievement)

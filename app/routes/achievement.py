"""Route for achievements api"""

from http import HTTPStatus

from fastapi import Body, Path, Request

from app.models.achievement import Achievement, AchievementPartial

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
    return base_instance.create(request, achievement)


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
    return base_instance.update(request, model_id, achievement)

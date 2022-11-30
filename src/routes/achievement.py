from http import HTTPStatus

from fastapi import Body, Request, Path
from fastapi.encoders import jsonable_encoder

from models.achievement import Achievement, AchievementPartial

from .base_route import BaseRoute

db_key: str = 'achievements'

base_instance = BaseRoute(db_key, Achievement)
achievement_router = base_instance.router


@achievement_router.post('/', status_code=HTTPStatus.CREATED,
                         response_description='Create an Achievement',
                         response_model=Achievement)
def create_survival(request: Request, achievement: Achievement = Body(...)
                    ) -> Achievement:
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(achievement)
    new_data = request.app.database[db_key].insert_one(enc_data)
    created_data: Achievement = request.app.database[db_key].find_one(
        {'_id': new_data.inserted_id}
    )
    return created_data


@achievement_router.put('/{id}',
                        response_description='Update an Achievement',
                        response_model=Achievement)
def update_puzzle(request: Request, id: str = Path(...),
                  achievement: AchievementPartial = Body(...)) -> Achievement:
    base_instance.validate_env(request)
    achievement = {k: v for k, v in achievement.dict().items()
                   if v is not None}
    if len(achievement) >= 1:
        update_result = request.app.database[db_key].update_one(
            {'_id': id}, {'$set': achievement}
        )

        if update_result.modified_count == 0:
            base_instance.id_not_found(id)

    return base_instance.find_by_id(request, id)

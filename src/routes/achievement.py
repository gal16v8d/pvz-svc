from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Body, HTTPException, Request, Response, Path
from fastapi.encoders import jsonable_encoder

from consts import constants
from models.achievement import Achievement, AchievementPartial

db_key: str = 'achievements'

achievement_router: APIRouter = APIRouter(
    tags=['achievements'],
    prefix='/api/achievements',
)


@achievement_router.get('/',
                        response_description='List all achievements',
                        response_model=List[Achievement])
def list_achievements(request: Request) -> List[Achievement]:
    return list(request.app.database[db_key].find())


@achievement_router.get('/{id}',
                        response_description='Get a single achievement by id',
                        response_model=Achievement)
def find_achievement(request: Request, id: str = Path(...)) -> Achievement:
    '''
    List a Achievement by id

    This one check in our app db using the id if it exists or not.

    Parameters:
    - **id:uuid** -> Object uuid to find an Achievement in db.

    Returns the Achievement if found, else a not found with a custom message.
    '''
    if (
        existing_data :=
        request.app.database[db_key].find_one({'_id': id})
    ) is not None:
        return existing_data

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                        detail=f'Achievement with ID {id} not found')


@achievement_router.post('/', status_code=HTTPStatus.CREATED,
                         response_description='Create an achievement',
                         response_model=Achievement)
def create_achievement(request: Request,
                       achievement: Achievement = Body(...)) -> Achievement:
    if (request.app.env == 'dev'):
        enc_data = jsonable_encoder(achievement)
        new_data = request.app.database[db_key].insert_one(
            enc_data)
        created_data: Achievement = request.app.database[db_key].find_one(
            {'_id': new_data.inserted_id}
        )
        return created_data

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)


@achievement_router.put('/{id}',
                        response_description='Update an achievement',
                        response_model=Achievement)
def update_achievement(request: Request, id: str = Path(...),
                       achievement: AchievementPartial = Body(...)
                       ) -> Achievement:
    if (request.app.env == 'dev'):
        achievement = {k: v for k, v in achievement.dict().items()
                       if v is not None}
        if len(achievement) >= 1:
            update_result = request.app.database[db_key].update_one(
                {'_id': id}, {'$set': achievement}
            )

            if update_result.modified_count == 0:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'Achievement with ID {id} not found')

        return find_achievement(request, id)

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)


@achievement_router.delete('/{id}',
                           response_description='Delete an Achievement')
def delete_achievement(request: Request, response: Response,
                       id: str = Path(...)) -> Response:
    if (request.app.env == 'dev'):
        delete_result = request.app.database[db_key].delete_one({
            '_id': id})

        if delete_result.deleted_count == 1:
            response.status_code = HTTPStatus.NO_CONTENT
            return response

        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f'Achievement with ID {id} not found')

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)

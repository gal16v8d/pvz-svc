from http import HTTPStatus

from fastapi import Body, Request, Path
from fastapi.encoders import jsonable_encoder

from models.survival import Survival, SurvivalPartial

from .base_route import BaseRoute

db_key: str = 'survivals'

base_instance = BaseRoute(db_key, Survival)
survival_router = base_instance.router


@survival_router.post('/', status_code=HTTPStatus.CREATED,
                      response_description='Create a Survival',
                      response_model=Survival)
def create_survival(request: Request, survival: Survival = Body(...)
                    ) -> Survival:
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(survival)
    created_data: Survival = base_instance.create(request, enc_data)
    return created_data


@survival_router.put('/{id}',
                     response_description='Update a Survival',
                     response_model=Survival)
def update_puzzle(request: Request, id: str = Path(...),
                  survival: SurvivalPartial = Body(...)) -> Survival:
    base_instance.validate_env(request)
    survival = {k: v for k, v in survival.dict().items() if v is not None}
    if len(survival) >= 1:
        update_result = request.app.database[db_key].update_one(
            {'_id': id}, {'$set': survival}
        )

        if update_result.modified_count == 0:
            base_instance.id_not_found(id)

    return base_instance.find_by_id(request, id)

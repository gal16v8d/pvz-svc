from http import HTTPStatus

from fastapi import Body, Path, Request
from fastapi.encoders import jsonable_encoder

from models.survival import Survival, SurvivalPartial

from .base_route import BaseRoute


db_key: str = "survivals"
base_instance = BaseRoute(db_key, Survival)
survival_router = base_instance.router


@survival_router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_description="Create a Survival",
    response_model=Survival,
)
def create_survival(request: Request, survival: Survival = Body(...)) -> Survival:
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(survival)
    return base_instance.create(request, enc_data)


@survival_router.put(
    "/{model_id}", response_description="Update a Survival", response_model=Survival
)
def update_survival(
    request: Request, model_id: str = Path(...), survival: SurvivalPartial = Body(...)
) -> Survival:
    base_instance.validate_env(request)
    survival = {k: v for k, v in survival.dict().items() if v is not None}
    return base_instance.update(request, model_id, survival)

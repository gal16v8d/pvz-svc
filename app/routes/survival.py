from http import HTTPStatus

from fastapi import Body, Path, Request

from app.models.survival import Survival, SurvivalPartial

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
    return base_instance.create(request, survival)


@survival_router.put(
    "/{model_id}", response_description="Update a Survival", response_model=Survival
)
def update_survival(
    request: Request, model_id: str = Path(...), survival: SurvivalPartial = Body(...)
) -> Survival:
    return base_instance.update(request, model_id, survival)

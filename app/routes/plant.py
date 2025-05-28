from http import HTTPStatus

from fastapi import Body, Path, Request

from app.models.plant import Plant, PlantPartial

from .base_route import BaseRoute


db_key: str = "plants"
base_instance = BaseRoute(db_key, Plant)
plant_router = base_instance.router


@plant_router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_description="Create a Plant",
    response_model=Plant,
)
def create_plant(request: Request, plant: Plant = Body(...)) -> Plant:
    return base_instance.create(request, plant)


@plant_router.put(
    "/{model_id}", response_description="Update a Plant", response_model=Plant
)
def update_plant(
    request: Request, model_id: str = Path(...), plant: PlantPartial = Body(...)
) -> Plant:
    return base_instance.update(request, model_id, plant)

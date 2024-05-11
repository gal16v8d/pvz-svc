from http import HTTPStatus

from fastapi import Body, Path, Request
from fastapi.encoders import jsonable_encoder

from models.plant import Plant, PlantPartial

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
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(plant)
    return base_instance.create(request, enc_data)


@plant_router.put(
    "/{model_id}", response_description="Update a Plant", response_model=Plant
)
def update_plant(
    request: Request, model_id: str = Path(...), plant: PlantPartial = Body(...)
) -> Plant:
    base_instance.validate_env(request)
    plant = {k: v for k, v in plant.dict().items() if v is not None}
    return base_instance.update(request, model_id, plant)

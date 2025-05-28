from http import HTTPStatus

from fastapi import Body, Path, Request

from app.models.garden import Garden, GardenPartial

from .base_route import BaseRoute


db_key: str = "gardens"
base_instance = BaseRoute(db_key, Garden)
garden_router = base_instance.router


@garden_router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_description="Create a Garden",
    response_model=Garden,
)
def create_garden(request: Request, garden: Garden = Body(...)) -> Garden:
    return base_instance.create(request, garden)


@garden_router.put(
    "/{model_id}", response_description="Update a Garden", response_model=Garden
)
def update_garden(
    request: Request, model_id: str = Path(...), garden: GardenPartial = Body(...)
) -> Garden:
    return base_instance.update(request, model_id, garden)

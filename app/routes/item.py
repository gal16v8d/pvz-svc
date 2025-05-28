from http import HTTPStatus

from fastapi import Body, Path, Request
from app.models.item import Item, ItemPartial

from .base_route import BaseRoute


db_key: str = "items"
base_instance = BaseRoute(db_key, Item)
item_router = base_instance.router


@item_router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_description="Create an Item",
    response_model=Item,
)
def create_item(request: Request, item: Item = Body(...)) -> Item:
    return base_instance.create(request, item)


@item_router.put(
    "/{model_id}", response_description="Update an Item", response_model=Item
)
def update_item(
    request: Request, model_id: str = Path(...), item: ItemPartial = Body(...)
) -> Item:
    return base_instance.update(request, model_id, item)

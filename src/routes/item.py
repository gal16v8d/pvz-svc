from http import HTTPStatus

from fastapi import Body, Path, Request
from fastapi.encoders import jsonable_encoder

from models.item import Item, ItemPartial

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
    base_instance.validate_env(request)
    enc_data = jsonable_encoder(item)
    return base_instance.create(request, enc_data)


@item_router.put(
    "/{model_id}", response_description="Update an Item", response_model=Item
)
def update_item(
    request: Request, model_id: str = Path(...), item: ItemPartial = Body(...)
) -> Item:
    base_instance.validate_env(request)
    item = {k: v for k, v in item.dict().items() if v is not None}
    return base_instance.update(request, model_id, item)

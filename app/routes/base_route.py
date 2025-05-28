"""Base crud data to any implementation that use common http methods"""

from http import HTTPStatus
from typing import Any, NoReturn

from fastapi import APIRouter, HTTPException, Path, Request, Response
from fastapi.encoders import jsonable_encoder

from app.consts.constants import PVZ_READ_ONLY
from app.consts import env
from app.core.env import current_env
from app.models.base_model import PvZBaseModel


class BaseRoute:
    """Route to inherit"""

    def __init__(self, path: str, model: PvZBaseModel) -> None:
        self.path = path
        self.model = model
        self.single_path = self.path.capitalize()[:-1]
        self.router = APIRouter(tags=[path], prefix=f"/api/{path}")
        self.router.add_api_route(
            "/",
            self.list_all,
            response_description=f"List all {self.path}",
            response_model=list[self.model],
            methods=["GET"],
        )
        self.router.add_api_route(
            "/{model_id}",
            self.find_by_id,
            response_description=f"Get one {self.single_path}",
            response_model=self.model,
            methods=["GET"],
        )
        self.router.add_api_route(
            "/{model_id}",
            self.delete,
            status_code=HTTPStatus.NO_CONTENT,
            response_description=f"Delete one {self.single_path}",
            response_model={},
            methods=["DELETE"],
        )

    @staticmethod
    def validate_env() -> None:
        """
        Helps to put the API in read-only mode for prod.
        """
        if current_env == env.PROD_ENV:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail=PVZ_READ_ONLY
            )

    def not_modified(self) -> NoReturn:
        """Raise exception if no data edited"""
        raise HTTPException(status_code=HTTPStatus.NOT_MODIFIED)

    def id_not_found(self, model_id: str) -> NoReturn:
        """Raise exception when id not found"""
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"{self.single_path}" f" with ID {model_id} not found",
        )

    def list_all(self, request: Request) -> list[PvZBaseModel]:
        """List all the data for the given path"""
        return list(request.app.database[self.path].find())

    def find_by_id(self, request: Request, model_id: str = Path(...)) -> PvZBaseModel:
        """
        List by id

        This one check in our app db using the object id.

        Parameters:
        - **model_id:uuid** -> Object uuid to find any match in db.

        Returns the related data if found,
        else a not found with a custom message.
        """
        if (
            existing_data := request.app.database[self.path].find_one({"_id": model_id})
        ) is not None:
            return existing_data

        self.id_not_found(model_id)

    def create(self, request: Request, data: Any) -> Any:
        """Generic method to create the data in the API"""
        BaseRoute.validate_env()
        enc_data = jsonable_encoder(data)
        new_data = request.app.database[self.path].insert_one(enc_data)
        created_data = request.app.database[self.path].find_one(
            {"_id": new_data.inserted_id}
        )
        return created_data

    def update(self, request: Request, model_id: str, data: Any) -> Any:
        """Generic method to update data in the API"""
        BaseRoute.validate_env()
        data_dict = {k: v for k, v in data.dict().items() if v is not None}
        if len(data_dict) >= 1:
            update_result = request.app.database[self.path].update_one(
                {"_id": model_id}, {"$set": data_dict}
            )

            if update_result.modified_count == 0:
                existing_data = self.find_by_id(request, model_id)
                if existing_data is not None:
                    self.not_modified()

        return self.find_by_id(request, model_id)

    def delete(
        self, request: Request, response: Response, model_id: str = Path(...)
    ) -> Response:
        """Generic method to delete data in the API"""
        BaseRoute.validate_env()
        delete_result = request.app.database[self.path].delete_one({"_id": model_id})

        if delete_result.deleted_count == 1:
            response.status_code = HTTPStatus.NO_CONTENT
            return response

        self.id_not_found(model_id)

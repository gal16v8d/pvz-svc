"""Base crud data to any implementation that use common http methods"""

from http import HTTPStatus
from typing import NoReturn, TypeVar

from fastapi import APIRouter, Body, HTTPException, Path, Request, Response

from app.consts.constants import PVZ_READ_ONLY
from app.consts import env
from app.core.env import current_env
from app.models.base_model import PvZBaseModel


ReadSchemaType = TypeVar("ReadSchemaType", bound=PvZBaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=PvZBaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PvZBaseModel)


class BaseRoute:
    """Route to inherit"""

    def __init__(
        self,
        path: str,
        create_model: type[CreateSchemaType],
        update_model: type[UpdateSchemaType],
        read_model: type[ReadSchemaType] = None,
    ) -> None:
        self.path = path
        self.create_model = create_model
        self.update_model = update_model
        self.read_model = read_model
        self.single_path = self.path.capitalize()[:-1]
        self.router = APIRouter(tags=[path], prefix=f"/api/{path}")
        self.router.add_api_route(
            "/",
            self.list_all,
            response_description=f"List all {self.path}",
            response_model=list[self.read_model],
            methods=["GET"],
        )
        self.router.add_api_route(
            "/{model_id}",
            self.find_by_id,
            response_description=f"Get one {self.single_path}",
            response_model=self.read_model,
            methods=["GET"],
        )
        self.router.add_api_route(
            "/",
            self._build_create_fn(self.create_model, self.read_model),
            status_code=HTTPStatus.CREATED,
            response_description=f"Create a {self.single_path}",
            response_model=self.read_model,
            methods=["POST"],
        )
        self.router.add_api_route(
            "/{model_id}",
            self._build_update_fn(self.update_model, self.read_model),
            response_description=f"Update a {self.single_path}",
            response_model=self.read_model,
            methods=["PATCH"],
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

    def _not_modified(self) -> NoReturn:
        """Raise exception if no data edited"""
        raise HTTPException(status_code=HTTPStatus.NOT_MODIFIED)

    def _id_not_found(self, model_id: str) -> NoReturn:
        """Raise exception when id not found"""
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"{self.single_path}" f" with ID {model_id} not found",
        )

    def _build_create_fn(
        self, schema: CreateSchemaType, read_schema: ReadSchemaType
    ) -> callable:
        """
        Build a function to create a new instance of the schema.
        This is useful for creating instances in the database.
        """

        def create_fn(request: Request, data: schema = Body(...)) -> read_schema:
            """Create a new instance of the schema in the database"""
            BaseRoute.validate_env()
            database = request.app.database
            new_data = database[self.path].insert_one(
                data.model_dump(by_alias=True, exclude_none=True)
            )
            created_data = database[self.path].find_one({"_id": new_data.inserted_id})
            return created_data

        return create_fn

    def _build_update_fn(
        self, schema: UpdateSchemaType, read_schema: ReadSchemaType
    ) -> callable:
        def update_fn(
            request: Request, model_id: str, data: schema = Body(...)
        ) -> read_schema:
            """Generic method to update data in the API"""
            BaseRoute.validate_env()
            data_dict = {
                k: v
                for k, v in data.model_dump(
                    by_alias=True, exclude={"id"}, exclude_none=True
                ).items()
                if v is not None
            }
            if len(data_dict) == 0:
                self._not_modified()

            existing_data = self.find_by_id(request, model_id)
            if existing_data is None:
                self._id_not_found(model_id)
            else:
                update_result = request.app.database[self.path].update_one(
                    {"_id": model_id}, {"$set": data_dict}
                )

                if update_result.modified_count == 0:
                    self._not_modified()

            return self.find_by_id(request, model_id)
        return update_fn

    def list_all(self, request: Request) -> list[ReadSchemaType]:
        result = []
        if request.query_params:
            query_params = {k: v for k, v in request.query_params.items()}
            result = list(request.app.database[self.path].find(query_params))
        # If no query params, return all data
        else:
            result = list(request.app.database[self.path].find())
        if len(result) == 0:
            # If no data found, raise not found exception
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="No data found",
            )
        return result

    def find_by_id(
        self, request: Request, model_id: str = Path(...)
    ) -> CreateSchemaType:
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

        self._id_not_found(model_id)

    def delete(
        self, request: Request, response: Response, model_id: str = Path(...)
    ) -> Response:
        """Generic method to delete data in the API"""
        BaseRoute.validate_env()
        delete_result = request.app.database[self.path].delete_one({"_id": model_id})

        if delete_result.deleted_count == 1:
            response.status_code = HTTPStatus.NO_CONTENT
            return response

        self._id_not_found(model_id)

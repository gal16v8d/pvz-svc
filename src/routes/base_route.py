from http import HTTPStatus
from typing import List, Any
from fastapi import APIRouter, Request, Response, Path, HTTPException

from consts import constants


class BaseRoute:

    def __init__(self, path: str, type: Any):
        self.path = path
        self.type = type
        self.single_path = self.path.capitalize()[:-1]
        self.router = APIRouter(tags=[path], prefix=f'/api/{path}')
        self.router.add_api_route(
            '/', self.list_all,
            response_description=f'List all {self.path}',
            response_model=List[self.type], methods=['GET'])
        self.router.add_api_route(
            '/{id}', self.find_by_id,
            response_description=f'Get one {self.single_path}',
            response_model=self.type, methods=['GET'])
        self.router.add_api_route(
            '/{id}', self.delete,
            status_code=HTTPStatus.NO_CONTENT,
            response_description=f'Delete one {self.single_path}',
            response_model={}, methods=['DELETE'])

    def id_not_found(self, id: str):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f'{self.single_path}'
                            f' with ID {id} not found')

    def validate_env(self, request: Request):
        if (request.app.env == 'prod'):
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                                detail=constants.PVZ_READ_ONLY)

    def list_all(self, request: Request) -> List[Any]:
        return list(request.app.database[self.path].find())

    def find_by_id(self, request: Request, id: str = Path(...)) -> Any:
        '''
        List by id

        This one check in our app db using the object id.

        Parameters:
        - **id:uuid** -> Object uuid to find any match in db.

        Returns the related data if found,
        else a not found with a custom message.
        '''
        if (
            existing_data :=
            request.app.database[self.path].find_one({'_id': id})
        ) is not None:
            return existing_data

        self.id_not_found(id)

    def create(self, request: Request, data: Any) -> Any:
        new_data = request.app.database[self.path].insert_one(data)
        created_data = request.app.database[self.path].find_one(
            {'_id': new_data.inserted_id}
        )
        return created_data

    def delete(self, request: Request,
               response: Response, id: str = Path(...)) -> Response:
        self.validate_env(request)
        delete_result = request.app.database[self.path].delete_one({
            '_id': id})

        if delete_result.deleted_count == 1:
            response.status_code = HTTPStatus.NO_CONTENT
            return response

        self.id_not_found(id)

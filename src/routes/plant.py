from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Body, HTTPException, Request, Response, Path
from fastapi.encoders import jsonable_encoder

from consts import constants
from models.plant import Plant, PlantPartial

db_key: str = 'plants'

plant_router: APIRouter = APIRouter(
    tags=['plants'],
    prefix='/api/plants',
)


@plant_router.get('/',
                  response_description='List all plants',
                  response_model=List[Plant])
def list_plants(request: Request) -> List[Plant]:
    return list(request.app.database[db_key].find())


@plant_router.get('/{id}',
                  response_description='Get a single plant by id',
                  response_model=Plant)
def find_plant(request: Request, id: str = Path(...)) -> Plant:
    '''
    List a Plant by id

    This one check in our app db using the id if it exists or not.

    Parameters:
    - **id:uuid** -> Object uuid to find a Plant in db.

    Returns the Plant if found, else a not found with a custom message.
    '''
    if (
        existing_plant :=
        request.app.database[db_key].find_one({'_id': id})
    ) is not None:
        return existing_plant

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                        detail=f'Plant with ID {id} not found')


@plant_router.post('/', status_code=HTTPStatus.CREATED,
                   response_description='Create a Plant', response_model=Plant)
def create_plant(request: Request, plant: Plant = Body(...)) -> Plant:
    if (request.app.env == 'dev'):
        plant_enc = jsonable_encoder(plant)
        new_plant = request.app.database[db_key].insert_one(plant_enc)
        created_plant: Plant = request.app.database[db_key].find_one(
            {'_id': new_plant.inserted_id}
        )
        return created_plant

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)


@plant_router.put('/{id}',
                  response_description='Update a plant',
                  response_model=Plant)
def update_plant(request: Request, id: str = Path(...),
                 plant: PlantPartial = Body(...)) -> Plant:
    if (request.app.env == 'dev'):
        plant = {k: v for k, v in plant.dict().items() if v is not None}
        if len(plant) >= 1:
            update_result = request.app.database[db_key].update_one(
                {'_id': id}, {'$set': plant}
            )

            if update_result.modified_count == 0:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'Plant with ID {id} not found')

        return find_plant(request, id)

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)


@plant_router.delete('/{id}', response_description='Delete a plant')
def delete_plant(request: Request, response: Response,
                 id: str = Path(...)) -> Response:
    if (request.app.env == 'dev'):
        delete_result = request.app.database[db_key].delete_one({
            '_id': id})

        if delete_result.deleted_count == 1:
            response.status_code = HTTPStatus.NO_CONTENT
            return response

        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f'Plant with ID {id} not found')

    raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                        detail=constants.PVZ_READ_ONLY)

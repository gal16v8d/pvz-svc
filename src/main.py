from http import HTTPStatus
import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from models import all_models
from routes import all_routes


app: FastAPI = FastAPI(title="pvz-service",
                       description="Plants vs Zombies Info API",
                       version="0.0.1",
                       )


def create_indexes(db):
    for model in all_models:
        model(db).create_indexes()


@app.exception_handler(DuplicateKeyError)
def duplicate_key_exc_handler(request: Request, exc: DuplicateKeyError):
    return JSONResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                        content={'message': f'Error -> {exc.details}'})


@app.on_event('startup')
def startup_db_client():
    db_url = os.getenv('DB_PVZ')
    print(f'db_url is defined? {db_url is not None}')
    app.mongodb_client = MongoClient(db_url)
    app.database = app.mongodb_client.get_default_database()
    app.env = os.getenv('PVZ_ENV')
    print('Connected to the MongoDB database!')
    create_indexes(app.database)
    print('Indexes updated!')


@app.on_event('shutdown')
def shutdown_db_client():
    app.mongodb_client.close()


for route in all_routes:
    app.include_router(route)

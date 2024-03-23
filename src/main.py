from http import HTTPStatus
import os

from contextlib import asynccontextmanager
from dotenv import dotenv_values
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pymongo import MongoClient, database
from pymongo.errors import DuplicateKeyError

from models import all_models
from routes import all_routes


def create_indexes(db: database.Database):
    '''Create all the db indexes if needed'''
    for model in all_models:
        model(db).create_indexes()


@asynccontextmanager
async def lifespan(application: FastAPI):
    '''Allow to run startup and shutdown actions'''
    # Setup
    current_env = os.getenv('PVZ_ENV')
    if current_env == 'prod':
        db_url = os.getenv('DB_PVZ')
    else:
        config = dotenv_values('.env')
        db_url = config['DB_PVZ']
    print(f'db_url is defined? {db_url is not None}')
    application.mongodb_client = MongoClient(db_url)
    application.database = application.mongodb_client.get_default_database()
    application.env = current_env
    print('Connected to the MongoDB database!')
    create_indexes(application.database)
    print('Indexes updated!')
    yield
    # Teardown
    application.mongodb_client.close()


app: FastAPI = FastAPI(title="pvz-service",
                       description="Plants vs Zombies Info API",
                       version="0.0.1",
                       lifespan=lifespan
                       )

for route in all_routes:
    app.include_router(route)


@app.exception_handler(DuplicateKeyError)
def duplicate_key_exc_handler(request: Request, exc: DuplicateKeyError):
    return JSONResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                        content={'message': f'Error -> {exc.details}'})

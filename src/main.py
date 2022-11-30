from dotenv import dotenv_values

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from http import HTTPStatus
from models import *
from routes import *

config = dotenv_values('.env')
app: FastAPI = FastAPI(title="pvz-service",
                       description="Plants vs Zombies Info API",
                       version="0.0.1",
                       )


def create_indexes(db):
    AchievementConstraint(db).create_indexes()
    MiniGameConstraint(db).create_indexes()
    PlantConstraint(db).create_indexes()
    PuzzleConstraint(db).create_indexes()
    SurvivalConstraint(db).create_indexes()


@app.exception_handler(DuplicateKeyError)
def duplicate_key_exc_handler(request: Request, exc: DuplicateKeyError):
    return JSONResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                        content={'message': f'Error -> {exc.details}'})


@app.on_event('startup')
def startup_db_client():
    app.mongodb_client = MongoClient(config['ATLAS_URI'])
    app.database = app.mongodb_client[config['DB_NAME']]
    app.env = config['ENV']
    print('Connected to the MongoDB database!')
    create_indexes(app.database)
    print('Indexes updated!')


@app.on_event('shutdown')
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(health_router)
app.include_router(achievement_router)
app.include_router(minigame_router)
app.include_router(plant_router)
app.include_router(puzzle_router)
app.include_router(survival_router)

from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import *

config = dotenv_values('.env')
app: FastAPI = FastAPI(title="pvz-service",
                       description="Plants vs Zombies Info API",
                       version="0.0.1",
                       )


@app.on_event('startup')
def startup_db_client():
    app.mongodb_client = MongoClient(config['ATLAS_URI'])
    app.database = app.mongodb_client[config['DB_NAME']]
    app.env = config['ENV']
    print('Connected to the MongoDB database!')


@app.on_event('shutdown')
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(health_router)
app.include_router(achievement_router)
app.include_router(minigame_router)
app.include_router(plant_router)
app.include_router(puzzle_router)

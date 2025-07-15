"""Define man fast api target to run"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pymongo.errors import DuplicateKeyError

from app.core.database import pvz_database
from app.core.env import current_env
from app.handlers.error_handlers import (
    duplicate_key_exc_handler,
    general_exc_handler,
    http_exc_handler,
)
from app.routes import all_routes


@asynccontextmanager
async def lifespan(application: FastAPI):
    """Allow to run startup and shutdown actions"""
    application.database = pvz_database
    application.env = current_env
    yield
    # Teardown
    pvz_database.client.close()


app: FastAPI = FastAPI(
    title="pvz-service",
    description="Plants vs Zombies Info API",
    version="0.0.1",
    lifespan=lifespan,
)

for route in all_routes:
    app.include_router(route)

app.add_exception_handler(HTTPException, http_exc_handler)
app.add_exception_handler(DuplicateKeyError, duplicate_key_exc_handler)
app.add_exception_handler(Exception, general_exc_handler)

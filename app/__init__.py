"""Define man fast api target to run"""

from http import HTTPStatus

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError

from app.core.database import pvz_database
from app.core.env import current_env
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


@app.exception_handler(DuplicateKeyError)
def duplicate_key_exc_handler(_: Request, exc: DuplicateKeyError) -> JSONResponse:
    """On duplicate error, return UNPROCESSABLE_ENTITY"""
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={"message": f"Error -> {exc.details}"},
    )

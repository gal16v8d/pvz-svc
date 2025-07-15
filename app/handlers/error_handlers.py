"""Error handlers for FastAPI application."""

from http import HTTPStatus

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError


def http_exc_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """On http exception, return JSON response with error details."""
    return JSONResponse(
        status_code=HTTPStatus(exc.status_code),
        content={"path": request.url.path, "message": f"Error -> {exc.detail if exc.detail else str(exc)}"},
    )


def duplicate_key_exc_handler(request: Request, exc: DuplicateKeyError) -> JSONResponse:
    """On duplicate error, return UNPROCESSABLE_ENTITY"""
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={"path": request.url.path, "message": f"Error -> {exc.details}"},
    )


def general_exc_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle general exceptions"""
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={
            "path": request.url.path,
            "message": f"An unexpected error occurred: {str(exc)}",
        },
    )

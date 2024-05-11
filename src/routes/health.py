"""Health router"""

from typing import Dict
from fastapi import APIRouter


health_router: APIRouter = APIRouter(
    tags=["health"],
)


@health_router.get("/health", response_description="Check current API status")
def health() -> Dict[str, str]:
    """QUick endpoint to check app status"""
    return {"status": "UP"}

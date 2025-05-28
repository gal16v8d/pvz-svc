"""Health router"""

from fastapi import APIRouter


health_router: APIRouter = APIRouter(
    tags=["health"],
)


@health_router.get("/health", response_description="Check current API status")
def health() -> dict[str, str]:
    """Quick endpoint to check app status"""
    return {"status": "UP"}

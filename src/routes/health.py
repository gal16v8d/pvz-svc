from fastapi import APIRouter
from typing import Dict

health_router: APIRouter = APIRouter(
    tags=['health'],
)


@health_router.get('/health',
                   response_description='Check current API status')
def health() -> Dict[str, str]:
    return {'status': 'UP'}

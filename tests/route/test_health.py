"""Testing health route"""

from http import HTTPStatus
from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    """Check health path properly respond"""
    response = client.get("/health")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"status": "UP"}

"""Test config module"""

import os
from typing import Any
import pytest

from fastapi.testclient import TestClient
import mongomock


def pytest_sessionstart(session) -> None:
    os.environ["PVZ_ENV"] = "prod"


def pytest_sessionfinish(session) -> None:
    os.environ.pop("PVZ_ENV")


@pytest.fixture
def client() -> Any:
    from app import app

    app.mongodb_client = mongomock.MongoClient()
    app.database = app.mongodb_client["pvzDB"]
    test_client: TestClient = TestClient(app)
    yield test_client

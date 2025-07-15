"""Base tests"""

from http import HTTPStatus
from fastapi.testclient import TestClient


def test_list_all_plants(client: TestClient) -> None:
    """Check list all respond"""
    response = client.get("/api/plants")
    assert response.status_code == HTTPStatus.OK


def test_post_wont_work_with_bad_structure(client: TestClient) -> None:
    """Check bad scenario wont work by bad structure"""
    response = client.post(
        "/api/plants",
        json={
            "name": "Winter Melons",
            "description": "Winter Melons do heavy damage "
            "and slow groups of zombies",
            "damage": "infinite",
            "range": "lobbed",
            "firing_speed": "1/2 x",
            "special": "Melons damage and freeze nearby enemies on impact",
            "constraint": ["Must be planted on melon-pults"],
            "text": "Winter Melon tries to calm his nerves...",
            "cost": 200,
            "recharge": "very slow",
        },
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_post_wont_work_in_prod(client: TestClient) -> None:
    """Check post should not work for prod env"""
    response = client.post(
        "/api/plants",
        json={
            "number": 11,
            "name": "Fume-Shroom",
            "description": "Fume-Shrooms shoot fumes that can pass through screen doors.",
            "damage": ["normal"],
            "range": "all zombies in the fume cloud",
            "effect": "penetrates screen doors",
            "firing_speed": "1/2 x",
            "constraint": ["Sleeps during the day"],
            "text": "'I was in a dead-end job producing yeast...",
            "cost": 75,
            "recharge": "fast",
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_put_wont_work_in_prod(client: TestClient) -> None:
    """Check put should not work for prod env"""
    response = client.put(
        "/api/plants/1",
        json={
            "name": "Fume-Shroom",
            "description": "Fume-Shrooms shoot fumes that can pass through screen doors.",
            "damage": ["normal"],
            "range": "all zombies in the fume cloud",
            "effect": "penetrates screen doors",
            "firing_speed": "1/2 x",
            "constraint": ["Sleeps during the day"],
            "text": "'I was in a dead-end job producing yeast...",
            "cost": 75,
            "recharge": "fast",
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_delete_wont_work_in_prod(client: TestClient) -> None:
    """Check delete should not work for prod env"""
    response = client.delete("/api/plants/1")
    assert response.status_code == HTTPStatus.UNAUTHORIZED

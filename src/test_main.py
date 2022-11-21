from http import HTTPStatus
from fastapi.testclient import TestClient
import mongomock
from main import app


client: TestClient = TestClient(app)
app.mongodb_client = mongomock.MongoClient()
app.database = app.mongodb_client['pvzDB']
app.env = 'prod'


def test_health():
    response = client.get('/health')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'status': 'UP'
    }


def test_list_all_plants():
    response = client.get('/api/plants')
    assert response.status_code == HTTPStatus.OK


def test_post_wont_work_with_bad_structure():
    response = client.post('/api/plants', json={
        'name': 'Winter Melons',
        'description': 'Winter Melons do heavy damage '
        'and slow groups of zombies',
        'damage': 'infinite',
        'range': 'lobbed',
        'firing_speed': '1/2 x',
        'special': 'Melons damage and freeze nearby enemies on impact',
        'constraint': ['Must be planted on melon-pults'],
        'text': 'Winter Melon tries to calm his nerves.'
        'He hears the zombies approach.'
        'Will he make it? will anyone make it?',
        'cost': 200,
        'recharge': 'very slow'
    })
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_post_wont_work_in_prod():
    response = client.post('/api/plants', json={
        'name': 'Winter Melons',
        'description': 'Winter Melons do heavy damage '
        'and slow groups of zombies',
        'damage': 'very heavy',
        'range': 'lobbed',
        'firing_speed': '1/2 x',
        'special': 'Melons damage and freeze nearby enemies on impact',
        'constraint': ['Must be planted on melon-pults'],
        'text': 'Winter Melon tries to calm his nerves.'
        'He hears the zombies approach.'
        'Will he make it? will anyone make it?',
        'cost': 200,
        'recharge': 'very slow'
    })
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_put_wont_work_in_prod():
    response = client.put('/api/plants/1', json={
        'name': 'Winter Melons',
        'description': 'Winter Melons do heavy damage '
        'and slow groups of zombies',
        'damage': 'very heavy',
        'range': 'lobbed',
        'firing_speed': '1/2 x',
        'special': 'Melons damage and freeze nearby enemies on impact',
        'constraint': ['Must be planted on melon-pults'],
        'text': 'Winter Melon tries to calm his nerves.'
        'He hears the zombies approach.'
        'Will he make it? will anyone make it?',
        'cost': 200,
        'recharge': 'very slow'
    })
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_delete_wont_work_in_prod():
    response = client.delete('/api/plants/1')
    assert response.status_code == HTTPStatus.UNAUTHORIZED

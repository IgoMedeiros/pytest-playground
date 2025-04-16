import pytest
from api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_user(client):
    response = client.post('/users', json={'id': 1, 'name': 'Alice'})

    assert response.status_code == 200
    assert response.json == {'id': 1, 'name': 'Alice'}

def test_get_user(client):
    client.post('/users', json={'id': 2, 'name': 'Alice'})

    response = client.get('/users/2')

    assert response.status_code == 200
    assert response.json == {'id': 2, 'name': 'Alice'}
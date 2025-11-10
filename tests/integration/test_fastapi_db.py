import pytest


@pytest.mark.integration
@pytest.mark.slow
def test_items_db_crud(generated_fastapi_client_db):
    client = generated_fastapi_client_db

    # Initially empty
    r = client.get('/api/items')
    assert r.status_code == 200
    assert r.json() == []

    # Create item
    payload = {'name': 'foo', 'description': 'bar'}
    r = client.post('/api/items', json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data['id'] == 1
    assert data['name'] == 'foo'

    # List includes created
    r = client.get('/api/items')
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 1
    assert items[0]['name'] == 'foo'

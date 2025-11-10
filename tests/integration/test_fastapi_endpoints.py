import pytest


@pytest.mark.integration
def test_root_and_health(generated_fastapi_client):
    client = generated_fastapi_client

    r = client.get("/")
    assert r.status_code == 200
    j = r.json()
    assert j.get("status") in ("ok", "healthy") or "message" in j

    r2 = client.get("/health")
    assert r2.status_code == 200
    assert r2.json().get("status") == "healthy"


@pytest.mark.integration
def test_items_crud(generated_fastapi_client):
    client = generated_fastapi_client

    # Check routes present
    routes = [r.path for r in client.app.routes]
    # For debugging, ensure the expected path is registered
    assert "/api/items" in routes, f"Expected /api/items in routes, got: {routes}"

    # Initially empty (router is included under /api prefix)
    r = client.get("/api/items")
    assert r.status_code == 200
    assert r.json() == []

    # Create item
    payload = {"title": "Test item", "description": "desc"}
    r2 = client.post("/api/items", json=payload)
    assert r2.status_code == 201
    created = r2.json()
    assert created["id"] == 1
    assert created["title"] == payload["title"]

    # List should contain the item
    r3 = client.get("/api/items")
    assert r3.status_code == 200
    items = r3.json()
    assert len(items) == 1
    assert items[0]["title"] == payload["title"]

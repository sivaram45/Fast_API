from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_create_item():
    response = client.post("/items", params={"item": "apple"})
    assert response.status_code == 200
    assert "apple" in response.json()


def test_get_items_with_limit():
    response = client.get("/items?limit=1")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_item_by_id():
    response = client.get("/items/0")
    assert response.status_code == 200
    assert response.json() == "apple"


def test_get_item_not_found():
    response = client.get("/items/100")
    assert response.status_code == 404
    assert response.json()["detail"] == "item not found"


def test_update_item():
    response = client.put("/items/0", params={"new_item": "banana"})
    assert response.status_code == 200
    assert "banana" in response.json()


def test_delete_item():
    response = client.delete("/items/0")
    assert response.status_code == 200

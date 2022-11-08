from fastapi.testclient import TestClient
from api.routes.main import main

client = TestClient(main)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello!"}
    
import pytest
from fastapi.testclient import TestClient
from run import app

client = TestClient(app)


# Aircraft
def test_create_aircraft():
    payload = {
        "name": "Gulfstream G650"
    }
    response = client.post("/aircrafts", json=payload)
    assert response.status_code == 200


def test_get_aircraft():
    response = client.get("/aircrafts/1")
    assert response.status_code == 200
    assert response.json() == {
        "aircraft_id": 1,
        "name": "Gulfstream G650"
    }


def test_update_aircraft():
    payload = {
        "name": "Updated Aircraft"
    }
    response = client.put("/aircrafts/2", json=payload)
    assert response.status_code == 200
    assert response.json() == {
        'message': 'Aircraft updated successfully'
    }


def test_delete_aircraft():
    response = client.delete("/aircrafts/1")
    assert response.status_code == 200


def test_get_aircraft_not_found():
    response = client.get("/aircrafts/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Aircraft not found"}

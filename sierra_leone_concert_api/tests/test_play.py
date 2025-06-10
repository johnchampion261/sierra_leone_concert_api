from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_plays():
    response = client.get("/plays/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_play():
    play_data = {
        "title": "Test Play",
        "description": "A play for testing.",
        "director_id": 1  # Make sure a director with ID 1 exists
    }
    response = client.post("/plays/", json=play_data)
    assert response.status_code in [200, 201]
    assert response.json()["title"] == "Test Play"

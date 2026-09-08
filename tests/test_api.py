import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "active"
    assert response.json()["system"] == "Alpha Matrix Pro API"

def test_connect_endpoint_invalid_credentials():
    payload = {
        "server": "test_server",
        "login": 0,
        "password": "wrong"
    }
    response = client.post("/connect", json=payload)
    assert response.status_code in [400, 500]

def test_trade_endpoint_no_connection():
    payload = {
        "symbol": "EURUSD",
        "action": "BUY",
        "volume": 1.0,
        "sl": 0.0,
        "tp": 0.0
    }
    response = client.post("/trade", json=payload)
    assert response.status_code == 400

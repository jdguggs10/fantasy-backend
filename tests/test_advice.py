from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    resp = client.post("/advice", json={"conversation":[{"role":"user","content":"Ping"}]})
    assert resp.status_code == 200

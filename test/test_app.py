import json
from myapp import app
def test_hello():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"].startswith("Hello CI/CD")

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200

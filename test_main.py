from fastapi.testclient import TestClient
# We import 'app' even though we haven't created it yet. 
# It will fail, which is what we want for TDD.
try:
    from main import app
    client = TestClient(app)
except ImportError:
    client = None

def test_read_main():
    if not client:
        assert False, "App not created yet"
    response = client.get("/api/sweets")
    # We expect a 200 OK status
    assert response.status_code == 200
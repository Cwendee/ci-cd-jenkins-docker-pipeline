def test_health_endpoint():
    from app import app
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

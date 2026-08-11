import pytest

from main import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_200_and_message(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.get_json()


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_unknown_route_returns_404(client):
    response = client.get("/rota-que-nao-existe")
    assert response.status_code == 404
    assert "error" in response.get_json()


def test_db_status_responds_even_without_database(client):
    response = client.get("/db-status")
    assert response.status_code in (200, 503)
    assert "database" in response.get_json()

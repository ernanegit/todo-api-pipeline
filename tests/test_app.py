from app import app
import pytest


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_get_todos(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json) >= 2


def test_add_todo(client):
    new_todo = {"task": "Test task"}
    response = client.post("/todos", json=new_todo)
    assert response.status_code == 201
    assert response.json["task"] == "Test task"
def test_get_todo_by_id(client):
    response = client.get('/todos/1')
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_get_todo_not_found(client):
    response = client.get('/todos/999')
    assert response.status_code == 404
    assert 'error' in response.json

def test_delete_todo(client):
    response = client.delete('/todos/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Todo deleted'
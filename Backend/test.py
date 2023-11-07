# test_app.py

from fastapi.testclient import TestClient
from main import app  # Reemplaza 'app' con la importación real de tu aplicación
import pytest

client = TestClient(app)  # Reemplaza 'app' con la importación real de tu aplicación

# Prueba para crear un usuario
def test_create_user():
    payload = {"username": "testuser", "email": "testuser@example.com"}
    response = client.post("/users/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"

# Prueba para obtener un usuario por ID
def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data

# Prueba para actualizar un usuario por ID
def test_update_user():
    payload = {"username": "updateduser", "email": "updateduser@example.com"}
    response = client.put("/users/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "updateduser"
    assert data["email"] == "updateduser@example.com"

# Prueba para eliminar un usuario por ID
def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 204

# Ejecutar las pruebas con pytest
if __name__ == '__main__':
    pytest.main()

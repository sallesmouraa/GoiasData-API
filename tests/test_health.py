from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "GoiasData-API em execução.",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


def test_healthcheck() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_listar_tabelas() -> None:
    response = client.get("/api/v1/dados/tabelas")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_tabela_inexistente_retorna_404() -> None:
    response = client.get("/api/v1/dados/tabelas/tabela_inexistente/colunas")

    assert response.status_code == 404
    assert "não encontrada" in response.json()["detail"]

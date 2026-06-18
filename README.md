# GoiasData-API

API RESTful construída com **FastAPI** para disponibilizar, de forma rápida e padronizada, dados socioeconômicos, demográficos e do mercado de trabalho do estado de Goiás. As informações foram extraídas, tratadas e estruturadas a partir de 95 planilhas, sendo consolidadas em um banco **SQLite** para consultas eficientes, integração com aplicações externas e apoio a análises e tomada de decisão.

## Visão geral

O projeto utiliza o arquivo `GoiasData_Database.sqlite` como fonte de dados local e expõe endpoints HTTP para exploração inicial das tabelas disponíveis.

Nesta primeira estruturação, o foco foi criar uma base simples e funcional para permitir:
- subir a API localmente;
- validar a saúde da aplicação;
- listar tabelas do banco;
- inspecionar colunas;
- consultar registros iniciais.

## Stack

- Python 3.11+
- FastAPI
- Uvicorn
- SQLite
- Pytest
- Pydantic

## Estrutura do projeto

```text
app/
  api/
    routes/
      dados.py
      health.py
  core/
    config.py
  db/
    connection.py
  schemas/
    database.py
  services/
    database_service.py
  main.py
tests/
  test_health.py
requirements.txt
GoiasData_Database.sqlite
README.md
```

## Como executar localmente

### 1. Criar e ativar ambiente virtual

No Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar a API

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:
- API: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## Endpoints iniciais

### Health
- `GET /health`
  - Verifica se a aplicação está em execução.

### Root
- `GET /`
  - Retorna mensagem inicial e atalhos para documentação.

### Dados
- `GET /api/v1/dados/tabelas`
  - Lista as tabelas disponíveis no banco SQLite.

- `GET /api/v1/dados/tabelas/{table_name}/colunas`
  - Lista as colunas de uma tabela específica.

- `GET /api/v1/dados/tabelas/{table_name}/registros?limit=10`
  - Retorna registros de uma tabela, com limite configurável entre 1 e 100.

## Testes

Para executar os testes:

```bash
pytest
```

Atualmente há cobertura inicial para:
- endpoint raiz;
- healthcheck;
- listagem de tabelas;
- erro 404 para tabela inexistente.

## Observações

- O banco SQLite permanece versionado no repositório como fonte local de dados.
- Esta implementação é uma base inicial e pode evoluir para filtros, paginação, versionamento mais rico e endpoints analíticos específicos.
- A validação do nome das tabelas foi endurecida para aceitar apenas tabelas realmente existentes no banco.
- Dependendo do schema real do banco, pode ser necessário refinamento adicional nos endpoints para nomes de tabelas e colunas mais amigáveis.

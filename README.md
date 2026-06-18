# GoiásData API

API RESTful desenvolvida com **FastAPI** para disponibilizar, de forma rápida e padronizada, dados socioeconômicos, demográficos e do mercado de trabalho do estado de Goiás.

As informações são estruturadas a partir de planilhas e consolidadas no arquivo **`GoiasData_Database.sqlite`**.

## Visão geral

O projeto expõe endpoints HTTP para exploração inicial das tabelas disponíveis no banco SQLite, permitindo:

- validar a saúde da aplicação;
- listar tabelas disponíveis;
- inspecionar colunas;
- consultar registros com limite configurável.

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

### 1) Clonar o repositório

```bash
git clone https://github.com/sallesmouraa/GoiasData-API.git
cd GoiasData-API
```

### 2) Criar e ativar ambiente virtual

No Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3) Instalar dependências

```bash
pip install -r requirements.txt
```

### 4) Executar a API

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

- API: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## Endpoints disponíveis

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

## Exemplo de uso com curl

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/dados/tabelas" \
  -H "accept: application/json"
```

## Testes

Para executar os testes:

```bash
pytest
```

Cobertura inicial:

- endpoint raiz;
- healthcheck;
- listagem de tabelas;
- erro 404 para tabela inexistente.

## Fonte e atualização dos dados

Para evolução do projeto, recomenda-se manter documentado:

- origem de cada conjunto de dados (órgão/fonte);
- data da última atualização;
- periodicidade de atualização;
- transformações aplicadas na carga.

## Boas práticas para evolução

- adicionar filtros e paginação por endpoint;
- ampliar validações e tratamento de erros;
- incrementar cobertura de testes;
- configurar CI com lint + testes.

## Contribuição

Contribuições são bem-vindas.

Fluxo sugerido:

1. Faça um fork do projeto
2. Crie uma branch (`feat/minha-melhoria`)
3. Commit das alterações (`git commit -m "docs: melhora README"`)
4. Push da branch
5. Abra um Pull Request

## Licença

Defina aqui a licença do projeto (ex.: MIT) para esclarecer regras de uso e redistribuição.

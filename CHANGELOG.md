# Changelog

Todo o histórico de mudanças notáveis para este projeto será documentado neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.1.0] - 2024

### Added

- Estrutura inicial da API FastAPI
- Endpoint de health check (`GET /health`)
- Endpoint raiz com informações da API (`GET /`)
- Endpoints para listagem de tabelas (`GET /api/v1/dados/tabelas`)
- Endpoints para inspeção de colunas (`GET /api/v1/dados/tabelas/{table_name}/colunas`)
- Endpoints para consulta de registros (`GET /api/v1/dados/tabelas/{table_name}/registros`)
- Testes unitários iniciais
- Documentação Swagger/OpenAPI automática
- Validação de nomes de tabelas contra SQL injection
- Suporte a SQLite como banco de dados
- Configuração via variáveis de ambiente (`.env`)

### Planned

- Filtros avançados e busca
- Paginação melhorada
- Autenticação e autorização
- Endpoints analíticos específicos
- Cache de resultados
- Versionamento de API
- Documentação expandida

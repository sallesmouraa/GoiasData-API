# Guia de Contribuição - GoiasData-API

Obrigado por se interessar em contribuir com o GoiasData-API! Este documento fornece diretrizes e instruções para contribuidores.

## Como Contribuir

### Reportar Bugs

Antes de criar um relatório de bug, faça uma busca rápida na aba de Issues para verificar se o problema já foi reportado.

Ao reportar um bug, inclua:

- **Título claro e descritivo**
- **Descrição exata do comportamento observado**
- **Comportamento esperado**
- **Passos para reproduzir o problema**
- **Informações do seu ambiente** (Python version, SO, etc.)

### Sugerir Melhorias

Melhorias podem incluir novos recursos, aprimoramentos de funcionalidades existentes, ou melhorias de documentação.

Ao sugerir melhorias, inclua:

- **Título claro e descritivo**
- **Descrição detalhada da melhoria sugerida**
- **Justificativa da melhoria**
- **Exemplos de uso ou contexto**

### Pull Requests

1. **Fork o repositório** e crie sua branch baseada em `main`:
   ```bash
   git checkout -b feature/sua-feature
   ```

2. **Instale as dependências de desenvolvimento**:
   ```bash
   make install-dev
   ```

3. **Faça suas mudanças** e adicione testes se necessário

4. **Execute os testes**:
   ```bash
   make test
   ```

5. **Verifique a qualidade do código**:
   ```bash
   make lint
   make type-check
   ```

6. **Formate o código**:
   ```bash
   make format
   ```

7. **Faça commit com mensagens claras**:
   ```bash
   git commit -m "feat: descrição clara da mudança"
   ```

8. **Push para seu fork**:
   ```bash
   git push origin feature/sua-feature
   ```

9. **Abra um Pull Request** com descrição clara das mudanças

## Convenções de Commit

Usamos o formato Conventional Commits:

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `style:` - Formatação, missing semi colons, etc
- `refactor:` - Refatoração de código
- `perf:` - Melhorias de performance
- `test:` - Adição ou atualização de testes
- `chore:` - Tarefas de build, dependências, etc

Exemplo:
```bash
git commit -m "feat: add pagination to list_rows endpoint"
```

## Padrões de Código

- **Python Version**: 3.11+
- **Formatação**: Black (100 caracteres por linha)
- **Linting**: Ruff
- **Type Hints**: Obrigatório para novas funcionalidades
- **Testes**: Cobertura mínima de 80%

### Exemplo de Função Bem Formatada

```python
def list_tables(self) -> list[TableInfo]:
    """List all tables in the database.
    
    Returns:
        List of TableInfo objects containing table names.
    """
    query = (
        "SELECT name FROM sqlite_master "
        "WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    )
    with get_connection() as connection:
        rows = connection.execute(query).fetchall()
    return [TableInfo(name=row[0]) for row in rows]
```

## Processo de Review

- Todos os PRs serão revisados antes de serem merged
- Feedback será fornecido se necessárias mudanças
- Após aprovação, seu PR será merged para `main`

## Dúvidas?

Sinta-se livre para abrir uma Issue com a tag `question` ou entrar em contato através das issues.

Obrigado por contribuir! 🚀

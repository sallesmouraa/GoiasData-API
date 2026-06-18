.PHONY: help install install-dev run test test-cov lint format type-check pre-commit clean

.DEFAULT_GOAL := help

help: ## Show this help message
	@echo 'GoiasData-API - Development Commands'
	@echo ''
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -e ".[dev]"
	pre-commit install

run: ## Run the API server
	uvicorn app.main:app --reload

run-prod: ## Run the API server in production mode
	uvicorn app.main:app --host 0.0.0.0 --port 8000

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage report
	pytest --cov=app --cov-report=html --cov-report=term-missing

lint: ## Run linters (ruff)
	ruff check app tests

format: ## Format code with black and ruff
	ruff format app tests
	ruff check --fix app tests

type-check: ## Run type checker (mypy)
	mypy app

pre-commit: ## Run pre-commit hooks
	pre-commit run --all-files

clean: ## Clean up cache and build artifacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name htmlcov -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name .coverage -delete

dev-setup: install-dev ## Complete development setup
	@echo "✓ Development environment ready!"

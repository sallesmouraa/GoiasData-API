from fastapi import FastAPI

from app.api.routes import dados, health
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "API para consulta de dados socioeconômicos, demográficos e de trabalho "
        "do estado de Goiás a partir de um banco SQLite."
    ),
)

app.include_router(health.router)
app.include_router(dados.router, prefix=settings.api_v1_prefix)


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    return {
        "message": "GoiasData-API em execução.",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }

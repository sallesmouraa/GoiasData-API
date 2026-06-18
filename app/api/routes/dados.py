from fastapi import APIRouter, HTTPException, Query

from app.schemas.database import ColumnInfo, QueryResult, TableInfo
from app.services.database_service import DatabaseService

router = APIRouter(prefix="/dados", tags=["dados"])
service = DatabaseService()


@router.get("/tabelas", response_model=list[TableInfo])
def listar_tabelas() -> list[TableInfo]:
    return service.list_tables()


@router.get("/tabelas/{table_name}/colunas", response_model=list[ColumnInfo])
def listar_colunas(table_name: str) -> list[ColumnInfo]:
    try:
        return service.list_columns(table_name)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/tabelas/{table_name}/registros", response_model=QueryResult)
def listar_registros(
    table_name: str,
    limit: int = Query(default=10, ge=1, le=100),
) -> QueryResult:
    try:
        return service.get_rows(table_name, limit)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

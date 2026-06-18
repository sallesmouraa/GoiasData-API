from sqlite3 import Row

from app.db.connection import get_connection
from app.schemas.database import ColumnInfo, QueryResult, TableInfo


class DatabaseService:
    @staticmethod
    def _table_exists(table_name: str) -> bool:
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name = ?"
        with next(get_connection()) as connection:
            result = connection.execute(query, (table_name,)).fetchone()
        return result is not None

    def list_tables(self) -> list[TableInfo]:
        query = (
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        )
        with next(get_connection()) as connection:
            rows = connection.execute(query).fetchall()
        return [TableInfo(name=row[0]) for row in rows]

    def list_columns(self, table_name: str) -> list[ColumnInfo]:
        if not self._table_exists(table_name):
            raise ValueError(f"Tabela '{table_name}' não encontrada.")

        query = f"PRAGMA table_info('{table_name}')"
        with next(get_connection()) as connection:
            rows = connection.execute(query).fetchall()
        return [
            ColumnInfo(
                cid=row[0],
                name=row[1],
                type=row[2],
                notnull=row[3],
                default_value=row[4],
                pk=row[5],
            )
            for row in rows
        ]

    def get_rows(self, table_name: str, limit: int) -> QueryResult:
        if not self._table_exists(table_name):
            raise ValueError(f"Tabela '{table_name}' não encontrada.")

        query = f'SELECT * FROM "{table_name}" LIMIT ?'
        with next(get_connection()) as connection:
            rows = connection.execute(query, (limit,)).fetchall()

        normalized_rows = [self._row_to_dict(row) for row in rows]
        return QueryResult(
            table=table_name,
            total_returned=len(normalized_rows),
            rows=normalized_rows,
        )

    @staticmethod
    def _row_to_dict(row: Row) -> dict[str, object]:
        return {key: row[key] for key in row.keys()}

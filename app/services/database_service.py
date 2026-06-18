from sqlite3 import Row

from app.db.connection import get_connection
from app.schemas.database import ColumnInfo, QueryResult, TableInfo


class DatabaseService:
    def list_tables(self) -> list[TableInfo]:
        query = (
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        )
        with get_connection() as connection:
            rows = connection.execute(query).fetchall()
        return [TableInfo(name=row[0]) for row in rows]

    def list_columns(self, table_name: str) -> list[ColumnInfo]:
        validated_table_name = self._validate_table_name(table_name)

        query = f'PRAGMA table_info("{validated_table_name}")'
        with get_connection() as connection:
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
        validated_table_name = self._validate_table_name(table_name)

        query = f'SELECT * FROM "{validated_table_name}" LIMIT ?'
        with get_connection() as connection:
            rows = connection.execute(query, (limit,)).fetchall()

        normalized_rows = [self._row_to_dict(row) for row in rows]
        return QueryResult(
            table=validated_table_name,
            total_returned=len(normalized_rows),
            rows=normalized_rows,
        )

    def _validate_table_name(self, table_name: str) -> str:
        existing_tables = {table.name for table in self.list_tables()}
        if table_name not in existing_tables:
            raise ValueError(f"Tabela '{table_name}' não encontrada.")
        return table_name

    @staticmethod
    def _row_to_dict(row: Row) -> dict[str, object]:
        return {key: row[key] for key in row.keys()}

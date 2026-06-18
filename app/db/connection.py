from contextlib import contextmanager
import sqlite3
from collections.abc import Iterator

from app.core.config import settings


class DatabaseConnectionError(RuntimeError):
    pass


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    connection: sqlite3.Connection | None = None
    try:
        connection = sqlite3.connect(settings.database_path)
        connection.row_factory = sqlite3.Row
        yield connection
    except sqlite3.Error as exc:
        raise DatabaseConnectionError(f"Erro ao conectar ao banco SQLite: {exc}") from exc
    finally:
        if connection is not None:
            connection.close()

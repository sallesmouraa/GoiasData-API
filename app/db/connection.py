from collections.abc import Generator
import sqlite3

from app.core.config import settings


class DatabaseConnectionError(RuntimeError):
    pass


def get_connection() -> Generator[sqlite3.Connection, None, None]:
    try:
        connection = sqlite3.connect(settings.database_path)
        connection.row_factory = sqlite3.Row
        yield connection
    except sqlite3.Error as exc:
        raise DatabaseConnectionError(f"Erro ao conectar ao banco SQLite: {exc}") from exc
    finally:
        try:
            connection.close()
        except UnboundLocalError:
            pass

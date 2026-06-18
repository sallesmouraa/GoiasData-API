from pydantic import BaseModel


class TableInfo(BaseModel):
    name: str


class ColumnInfo(BaseModel):
    cid: int
    name: str
    type: str
    notnull: int
    default_value: str | None = None
    pk: int


class QueryResult(BaseModel):
    table: str
    total_returned: int
    rows: list[dict[str, object]]

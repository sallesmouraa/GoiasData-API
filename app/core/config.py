from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "GoiasData-API"
    app_version: str = "0.1.0"
    api_v1_prefix: str = "/api/v1"
    database_path: str = str(Path(__file__).resolve().parents[2] / "GoiasData_Database.sqlite")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

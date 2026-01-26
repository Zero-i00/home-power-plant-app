from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent

class PostgresSettings(BaseSettings):
    postgres_host: str = 'localhost'
    postgres_port: int = 5432
    postgres_db: str = 'power_plant_db'
    postgres_user: str = 'postgres'
    postgres_password: str = '12345678'

    @property
    def DATABASE_URL(self):
        return f'postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}'


    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore"
    )


class Settings(BaseSettings):
    app_port: int = 8000
    app_host: str = 'localhost'
    app_name: str = 'Home Power Plant'
    app_mode: str = 'DEVELOPING'

    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=False,
        extra="ignore"
    )


settings = Settings()
database_settings = PostgresSettings()

IS_DEBUG = settings.app_mode == 'DEVELOPING'

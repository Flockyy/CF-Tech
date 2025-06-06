from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or a .env file.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./app.db"

    FIRST_SUPERUSER: str = "admin@example.com"


settings = Settings()  # type: ignore

import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or a .env file.
    """

    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")
    DB_ADMIN_EMAIL = os.getenv("DB_ADMIN_EMAIL")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    SQLALCHEMY_DATABASE_URI: str = DATABASE_URL
    FIRST_SUPERUSER: str = DB_ADMIN_EMAIL


settings = Settings()  # type: ignore

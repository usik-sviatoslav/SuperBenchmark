import os

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True

    DEBUG: bool = os.getenv("SUPERBENCHMARK_DEBUG", "False") == "True"
    APP_NAME: str = "SuperBenchmark"
    PORT: int = 8000


settings = Settings()

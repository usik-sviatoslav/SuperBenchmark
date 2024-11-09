from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True

    SUPERBENCHMARK_DEBUG: bool = True
    DEBUG: bool = SUPERBENCHMARK_DEBUG
    APP_NAME: str = "SuperBenchmark"
    PORT: int = 8000


settings = Settings()

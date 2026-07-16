from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Verbum Core"
    APP_VERSION: str = "0.1.0"
    API_V1_STR: str = "/v1"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

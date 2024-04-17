from pydantic_settings import BaseSettings
from pydantic import RedisDsn


class Settings(BaseSettings):
    dev_mode: bool = False
    encoding: str = "utf-8"
    port: int = 80
    redis_db: RedisDsn


    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
from pydantic import BaseSettings
from pydantic.networks import PostgresDsn
from pydantic.networks import PostgresDsn

DEFAULT_PREFIX = "api"


class AsyncPostgresDsn(PostgresDsn):
    default_scheme = "postgresql+asyncpg"
    allowed_schemes = {"postgresql+asyncpg", "postgres+asyncpg"}


class Config(BaseSettings):
    DATABASE_URL: PostgresDsn
    API_PREFIX: str = DEFAULT_PREFIX

    @property
    def ASYNC_DATABASE_URL(self) -> AsyncPostgresDsn:
        ASYNC_DATABASE_URL = self.DATABASE_URL.replace(
            "postgres://", "postgresql+asyncpg://"
        )
        return ASYNC_DATABASE_URL


config = Config()

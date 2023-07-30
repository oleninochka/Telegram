from __future__ import annotations

import os
from dataclasses import dataclass

from peewee import MySQLDatabase
from playhouse.db_url import connect


@dataclass
class DatabaseConfig:
    host: str
    port: str
    user: str
    password: str
    database: str

    @staticmethod
    def load() -> DatabaseConfig:
        return DatabaseConfig(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
        )

    def __str__(self) -> str:
        return "mysql://{user}:{password}@{host}:{port}/{database}".format(**self.__dict__)

    @property
    def connection(self) -> MySQLDatabase:
        return connect(str(self))

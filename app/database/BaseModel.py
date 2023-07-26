from peewee import Model

from app.config import DatabaseConfig

db = DatabaseConfig.load().connection


class BaseModel(Model):
    class Meta:
        database = db

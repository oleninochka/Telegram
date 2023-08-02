from peewee import CharField, BigIntegerField

from app.database.BaseModel import BaseModel


class User(BaseModel):
    id = CharField(null=False, index=True)
    chat_id = BigIntegerField(null=False, index=True)
    telegram_id = BigIntegerField(null=False)

    class Meta:
        table_name = "User"

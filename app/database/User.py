from peewee import CharField, IntegerField

from app.database.BaseModel import BaseModel


class User(BaseModel):
    id = CharField(null=False, index=True)
    chat_id = IntegerField(null=False, index=True)
    telegram_id = IntegerField(null=False)

    class Meta:
        table_name = "User"

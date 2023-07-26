from dataclasses import dataclass

from aiogram.types import Message

from app.database.entity import User


@dataclass
class SubmitRequest:
    userId: str
    flag: str

    @staticmethod
    def build(message: Message):
        user: User = User.get_or_none(User.chat_id == message.chat.id)
        return SubmitRequest(
            userId=str(user.id),
            flag=message.text,
        )

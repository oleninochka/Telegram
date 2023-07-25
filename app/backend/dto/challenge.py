from dataclasses import dataclass

from aiogram.types import Message

from app.backend.dto.base import BaseEntity
from app.database.entity import User


@dataclass
class ChallengeResponse(BaseEntity):
    id: str
    name: str
    description: str
    weight: float
    team: bool
    visible: bool


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

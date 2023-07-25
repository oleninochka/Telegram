from dataclasses import dataclass
from typing import Optional

from aiogram.types import Message

from app.backend.dto.base import BaseEntity
from app.backend.dto.team import TeamResponse


@dataclass
class UserResponse(BaseEntity):
    id: str
    name: str
    team: Optional[TeamResponse] = None


@dataclass
class LinkTelegramRequest:
    token: str
    telegramId: str
    chatId: str

    @staticmethod
    def build(message: Message):
        return LinkTelegramRequest(
            token=message.text,
            telegramId=str(message.from_user.id),
            chatId=str(message.chat.id),
        )

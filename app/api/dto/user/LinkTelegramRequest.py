from dataclasses import dataclass

from app.api.dto.base import Serializable


@dataclass
class LinkTelegramRequest(Serializable):
    token: str
    telegramId: str
    chatId: str

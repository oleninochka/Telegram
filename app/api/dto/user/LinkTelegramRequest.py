from dataclasses import dataclass


@dataclass
class LinkTelegramRequest:
    token: str
    telegramId: str
    chatId: str

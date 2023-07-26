from dataclasses import dataclass

from aiogram.types import Message


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

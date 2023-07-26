from aiogram.types import Message

from app.api.service import UserService
from app.database.entity.User import User


class UserRepository:
    @staticmethod
    async def save_user(message: Message):
        response = await UserService.find_by_chat_id(message.chat.id)
        user = User(
            id=response.data.id,
            telegram_id=message.from_user.id,
            chat_id=message.chat.id,
        )
        user.save(force_insert=True)

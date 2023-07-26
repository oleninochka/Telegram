from aiogram.types import Message

from app.database.User import User


async def authenticated(message: Message) -> bool:
    user = User.get_or_none(User.telegram_id == message.from_user.id)
    return user is not None


async def unauthenticated(message: Message) -> bool:
    user = User.get_or_none(User.telegram_id == message.from_user.id)
    return user is None

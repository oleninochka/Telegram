from aiogram.methods import DeleteMessage
from aiogram.types import Message


async def delete_message_input(message: Message):
    await DeleteMessage(chat_id=message.chat.id, message_id=message.message_id - 1)
    await DeleteMessage(chat_id=message.chat.id, message_id=message.message_id)

import asyncio

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app import bot
from app.database import User
from app.view.state.admin import AdminStateGroup


class AdminHandler:
    @staticmethod
    async def broadcast(message: Message, _: MessageInput, dialog_manager: DialogManager):
        tasks = [bot.send_message(user.chat_id, message.text) for user in User.select()]
        await asyncio.gather(*tasks)
        await message.reply("Рассылка отправлена")
        await dialog_manager.switch_to(AdminStateGroup.menu)

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
        for user in User.select():
            await bot.send_message(user.chat_id, message.text)
            await asyncio.sleep(0.5)
        await message.reply("Рассылка отправлена")
        await dialog_manager.switch_to(AdminStateGroup.menu)

from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import html_decoration as hd
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app import bot
from app.api.dto.support import SupportChannel
from app.config import BotConfig


class SupportHandler:
    @staticmethod
    async def submit(message: Message, input: MessageInput, dialog_manager: DialogManager):
        text = '@{username}\n\n{text}\n\n#{channel}'.format(
            username=message.from_user.username,
            text=hd.bold(message.text),
            channel=dialog_manager.dialog_data['channel']
        )
        await bot.send_message(BotConfig.support, text)
        await message.reply('Запрос отправлен')

    @staticmethod
    async def set_channel(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
        manager.dialog_data['channel'] = item_id

    @staticmethod
    async def set_default_channel(_: Any, manager: DialogManager, **kwargs):
        await manager.dialog().find('tags').set_checked(manager.event, 'other', manager)

from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import html_decoration as hd
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app import bot
from app.config import BotConfig
from app.view.state.common import MenuStateGroup


class SupportHandler:
    @staticmethod
    async def submit(message: Message, _: MessageInput, dialog_manager: DialogManager):
        text = "@{username}\n\n{text}\n\n#{channel}".format(
            username=message.from_user.username,
            text=hd.bold(message.text),
            channel=dialog_manager.dialog_data["channel"],
        )
        await bot.send_message(BotConfig.load().support, text)
        await message.reply("Запрос отправлен")
        await dialog_manager.switch_to(MenuStateGroup.menu)

    @staticmethod
    async def set_channel(_: CallbackQuery, __: Any, manager: DialogManager, item_id: str):
        manager.dialog_data["channel"] = item_id

    @staticmethod
    async def set_default_channel(_: Any, manager: DialogManager, **kwargs):
        await manager.dialog().find("tags").set_checked(manager.event, "other", manager)

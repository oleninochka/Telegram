import re

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app import dp, authenticated
from app.dialog import MenuDialog


async def menu_dialog(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MenuDialog.StateGroup.menu, mode=StartMode.RESET_STACK)


def menu_handlers():
    router = Router(name=__name__)
    router.message.filter(authenticated)
    any_command = re.compile(r'.*')
    router.message.register(menu_dialog, Command(any_command))
    dp.include_router(router)

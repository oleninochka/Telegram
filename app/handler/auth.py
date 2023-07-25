import re

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app import dp
from app.dialog import AuthDialog
from app.filter.auth import unauthenticated


async def auth_dialog(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(AuthDialog.StateGroup.auth, mode=StartMode.RESET_STACK)


def auth_handlers():
    router = Router(name=__name__)
    router.message.filter(unauthenticated)
    any_command = re.compile(r'.*')
    router.message.register(auth_dialog, Command(any_command))
    dp.include_router(router)

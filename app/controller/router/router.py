from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app import dp
from app.controller.filter import authenticated, unauthenticated
from app.view.state import AuthStateGroup, MenuStateGroup


async def start_auth_dialog(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(AuthStateGroup.auth, mode=StartMode.NORMAL)


async def start_menu_dialog(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MenuStateGroup.menu, mode=StartMode.NORMAL)


def auth_router():
    router = Router(name=__name__)
    router.message.filter(unauthenticated)
    router.message.register(start_auth_dialog, Command('start'))
    dp.include_router(router)


def menu_router():
    router = Router(name=__name__)
    router.message.filter(authenticated)
    router.message.register(start_menu_dialog, Command('menu'))
    dp.include_router(router)

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app import dp
from app.controller.filter import authenticated, unauthenticated
from app.controller.handler.user import UserHandler
from app.view.state.common import AuthStateGroup, MenuStateGroup


async def start_auth_dialog(_: Message, dialog_manager: DialogManager):
    await dialog_manager.start(AuthStateGroup.auth, mode=StartMode.NORMAL)


async def start_menu_dialog(_: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MenuStateGroup.menu, mode=StartMode.NORMAL)


def auth_router():
    router = Router(name=__name__)
    router.message.filter(unauthenticated)
    router.message.register(start_auth_dialog, Command("start"))
    dp.include_router(router)


def menu_router():
    router = Router(name=__name__)
    router.message.filter(authenticated)
    router.message.register(start_menu_dialog, Command("menu"))
    dp.include_router(router)


@dp.message(Command("start"))
async def handler(message: Message, dialog_manager: DialogManager):
    if message.text != "/start":
        await UserHandler.link_telegram_on_start(message, dialog_manager)
    else:
        await start_auth_dialog(message, dialog_manager)

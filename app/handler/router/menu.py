from aiogram import Router
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app import dp
from app.handler.filter import authenticated
from app.handler.state import MenuStateGroup
from app.utils import AnyCommand


async def start_menu_dialog(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MenuStateGroup.menu, mode=StartMode.RESET_STACK)


def menu_router():
    router = Router(name=__name__)
    router.message.filter(authenticated)
    router.message.register(start_menu_dialog, AnyCommand)
    dp.include_router(router)

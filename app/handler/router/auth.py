from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app import dp
from app.handler.filter import unauthenticated
from app.handler.state import AuthStateGroup
from app.utils import AnyCommand


async def start_auth_dialog(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(AuthStateGroup.auth, mode=StartMode.RESET_STACK)


def auth_router():
    router = Router(name=__name__)
    router.message.filter(unauthenticated)
    router.message.register(start_auth_dialog, AnyCommand)
    dp.include_router(router)

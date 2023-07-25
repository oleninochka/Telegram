from aiogram.filters.state import State, StatesGroup
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const

from app.service.UserService import UserService


class AuthDialog:
    class StateGroup(StatesGroup):
        auth = State()

    link_telegram = Window(
        Const('Введите токен авторизации:'),
        MessageInput(UserService.link_telegram),
        state=StateGroup.auth,
    )

    dialog = Dialog(link_telegram)

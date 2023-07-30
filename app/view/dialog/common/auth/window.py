from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const

from app.controller.handler.user import UserHandler
from app.view.state.common import AuthStateGroup

link_telegram = Window(
    Const("Введите токен авторизации:"),
    MessageInput(UserHandler.link_telegram),
    state=AuthStateGroup.auth,
)

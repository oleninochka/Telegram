from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const

from app.handler.state import AuthStateGroup
from app.service import UserService

link_telegram = Window(
    Const('Введите токен авторизации:'),
    MessageInput(UserService.link_telegram),
    state=AuthStateGroup.auth,
)

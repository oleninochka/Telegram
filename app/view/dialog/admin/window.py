from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, SwitchTo, Cancel, Button
from aiogram_dialog.widgets.text import Const

from app.controller.handler import AdminHandler
from app.utils import back
from app.view.state import AdminStateGroup

menu = Window(
    Const("Панель администратора, будьте осторожны"),
    SwitchTo(Const('📤 Отправить рассылку'), id='broadcast', state=AdminStateGroup.broadcast),
    Cancel(back, id='back'),
    state=AdminStateGroup.menu,
)

broadcast = Window(
    Const("Введите текст рассылки:"),
    MessageInput(AdminHandler.broadcast),
    SwitchTo(back, id='back', state=AdminStateGroup.menu),
    state=AdminStateGroup.broadcast,
)

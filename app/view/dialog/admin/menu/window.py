from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import SwitchTo, Cancel
from aiogram_dialog.widgets.text import Const

from app.controller.handler.admin import AdminHandler
from app.widgets import back
from app.view.state.admin import AdminStateGroup

menu = Window(
    Const("Панель администратора, будьте осторожны"),
    SwitchTo(Const("📤 Отправить рассылку"), id="broadcast", state=AdminStateGroup.broadcast),
    Cancel(back, id="back"),
    state=AdminStateGroup.menu,
)

broadcast = Window(
    Const("Введите текст рассылки:"),
    MessageInput(AdminHandler.broadcast),
    SwitchTo(back, id="back", state=AdminStateGroup.menu),
    state=AdminStateGroup.broadcast,
)

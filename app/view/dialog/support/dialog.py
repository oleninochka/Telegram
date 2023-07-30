from aiogram_dialog import Dialog

from app import dp
from app.controller.handler import SupportHandler
from app.view.dialog.support import window


def support_dialog():
    dialog = Dialog(window.menu, on_start=SupportHandler.set_default_channel)
    dp.include_router(dialog)

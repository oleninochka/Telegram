from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.menu import window


def menu_dialog():
    dialog = Dialog(window.menu)
    dp.include_router(dialog)

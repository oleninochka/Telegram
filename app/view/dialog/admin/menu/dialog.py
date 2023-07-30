from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.admin.menu import window


def admin_dialog():
    dialog = Dialog(window.menu, window.broadcast)
    dp.include_router(dialog)

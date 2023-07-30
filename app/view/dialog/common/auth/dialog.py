from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.common.auth import window


def auth_dialog():
    dialog = Dialog(window.link_telegram)
    dp.include_router(dialog)

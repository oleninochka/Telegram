from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.user.event import window


def event_dialog():
    dialog = Dialog(window.menu, window.select)
    dp.include_router(dialog)

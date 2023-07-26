from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.challenge import window


def challenge_dialog():
    dialog = Dialog(window.menu, window.challenge, window.submit)
    dp.include_router(dialog)

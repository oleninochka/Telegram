from aiogram_dialog import Dialog

from app import dp
from app.handler.dialog.challenge import window


def challenge_dialog():
    dialog = Dialog(window.menu, window.select, window.challenge, window.submit)
    dp.include_router(dialog)

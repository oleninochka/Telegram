from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.user.team import window


def team_dialog():
    dialog = Dialog(window.menu, window.select, window.participate)
    dp.include_router(dialog)

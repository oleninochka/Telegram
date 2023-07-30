from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.user.score import window


def score_dialog():
    dialog = Dialog(window.user_scoreboard, window.team_scoreboard)
    dp.include_router(dialog)

from aiogram_dialog import setup_dialogs

from .AuthDialog import AuthDialog
from .ChallengeDialog import ChallengeDialog
from .MenuDialog import MenuDialog


def register_dialogs():
    from app import dp

    dp.include_router(AuthDialog.dialog)
    dp.include_router(MenuDialog.dialog)
    dp.include_router(ChallengeDialog.dialog)
    setup_dialogs(dp)

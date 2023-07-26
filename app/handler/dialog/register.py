from app.handler.dialog.auth.dialog import auth_dialog
from app.handler.dialog.challenge.dialog import challenge_dialog
from app.handler.dialog.menu.dialog import menu_dialog


def register_dialogs():
    auth_dialog()
    menu_dialog()
    challenge_dialog()

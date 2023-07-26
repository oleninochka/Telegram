from app.view.dialog.auth.dialog import auth_dialog
from app.view.dialog.challenge.dialog import challenge_dialog
from app.view.dialog.menu.dialog import menu_dialog
from app.view.dialog.team.dialog import team_dialog


def register_dialogs():
    auth_dialog()
    menu_dialog()
    team_dialog()
    challenge_dialog()

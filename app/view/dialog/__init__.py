from app.view.dialog.admin.dialog import admin_dialog
from app.view.dialog.auth.dialog import auth_dialog
from app.view.dialog.challenge.dialog import challenge_dialog
from app.view.dialog.event.dialog import event_dialog
from app.view.dialog.menu.dialog import menu_dialog
from app.view.dialog.score.dialog import score_dialog
from app.view.dialog.team.dialog import team_dialog


def register_dialogs():
    auth_dialog()
    menu_dialog()
    team_dialog()
    challenge_dialog()
    score_dialog()
    event_dialog()
    admin_dialog()

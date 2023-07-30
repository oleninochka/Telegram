from app.view.dialog.admin.menu.dialog import admin_dialog
from app.view.dialog.user.challenge.dialog import challenge_dialog
from app.view.dialog.user.event.dialog import event_dialog
from app.view.dialog.user.score.dialog import score_dialog
from app.view.dialog.user.support.dialog import support_dialog
from app.view.dialog.user.team.dialog import team_dialog


def user_dialogs():
    team_dialog()
    challenge_dialog()
    score_dialog()
    event_dialog()
    admin_dialog()
    support_dialog()

from app.view.dialog.admin import admin_dialogs
from app.view.dialog.common import common_dialogs
from app.view.dialog.user import user_dialogs


def register_dialogs():
    common_dialogs()
    user_dialogs()
    admin_dialogs()

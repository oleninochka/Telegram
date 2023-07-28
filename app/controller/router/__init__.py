from aiogram_dialog import setup_dialogs

from app import dp
from app.controller.router.router import auth_router, menu_router


def register_routes():
    auth_router()
    menu_router()
    setup_dialogs(dp)

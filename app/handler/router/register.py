from aiogram_dialog import setup_dialogs

from app import dp
from app.handler.router.auth import auth_router
from app.handler.router.menu import menu_router


def register_routes():
    auth_router()
    menu_router()
    setup_dialogs(dp)

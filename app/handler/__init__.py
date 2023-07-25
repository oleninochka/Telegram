from app.handler.auth import auth_handlers
from app.handler.menu import menu_handlers


def register_handlers():
    auth_handlers()
    menu_handlers()

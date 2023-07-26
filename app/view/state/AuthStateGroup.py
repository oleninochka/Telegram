from aiogram.fsm.state import StatesGroup, State


class AuthStateGroup(StatesGroup):
    auth = State()

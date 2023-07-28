from aiogram.fsm.state import StatesGroup, State


class AdminStateGroup(StatesGroup):
    menu = State()
    broadcast = State()

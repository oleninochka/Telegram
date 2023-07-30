from aiogram.fsm.state import StatesGroup, State


class EventStateGroup(StatesGroup):
    menu = State()
    select = State()

from aiogram.fsm.state import StatesGroup, State


class TeamStateGroup(StatesGroup):
    menu = State()
    select = State()
    participate = State()

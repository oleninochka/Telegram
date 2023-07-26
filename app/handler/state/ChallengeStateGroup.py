from aiogram.fsm.state import StatesGroup, State


class ChallengeStateGroup(StatesGroup):
    menu = State()
    select = State()
    challenge = State()
    submit = State()

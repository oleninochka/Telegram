from aiogram.fsm.state import StatesGroup, State


class ScoreStateGroup(StatesGroup):
    user_scoreboard = State()
    team_scoreboard = State()

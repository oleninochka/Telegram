from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel

from app.controller.handler import ScoreHandler
from app.utils import back
from app.view.state import ScoreStateGroup
from app.view.static import StaticLoader

user_scoreboard = Window(
    StaticLoader.template('scoreboard/user'),
    Cancel(back, id='back'),
    state=ScoreStateGroup.user_scoreboard,
    getter=ScoreHandler.user_scoreboard,
)

team_scoreboard = Window(
    StaticLoader.template('scoreboard/team'),
    Cancel(back, id='back'),
    state=ScoreStateGroup.team_scoreboard,
    getter=ScoreHandler.team_scoreboard,
)

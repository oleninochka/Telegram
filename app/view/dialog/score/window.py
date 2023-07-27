from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const

from app.controller.handler import ScoreHandler
from app.view.state import ScoreStateGroup
from app.view.template import TemplateLoader

user_scoreboard = Window(
    TemplateLoader.load('scoreboard/user'),
    Cancel(Const('Назад'), id='back'),
    state=ScoreStateGroup.user_scoreboard,
    getter=ScoreHandler.user_scoreboard,
)

team_scoreboard = Window(
    TemplateLoader.load('scoreboard/team'),
    Cancel(Const('Назад'), id='back'),
    state=ScoreStateGroup.team_scoreboard,
    getter=ScoreHandler.team_scoreboard,
)

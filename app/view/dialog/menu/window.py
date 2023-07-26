from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row, Start
from aiogram_dialog.widgets.text import Const

from app.controller.handler import UserHandler, ScoreHandler
from app.utils import TemplateLoader
from app.view.state import ChallengeStateGroup, MenuStateGroup, TeamStateGroup, ScoreStateGroup

menu = Window(
    TemplateLoader.load('profile'),
    Start(Const('Задачи'), id='challenges', state=ChallengeStateGroup.menu),
    Button(Const('Мероприятия'), id='events'),
    Start(Const('Команды'), id='teams', state=TeamStateGroup.menu, when=UserHandler.not_in_team),
    Row(
        Start(Const('Личный рейтинг'), id='personal_rating', state=ScoreStateGroup.user_scoreboard),
        Start(Const('Командный рейтинг'), id='team_rating', state=ScoreStateGroup.team_scoreboard),
    ),
    state=MenuStateGroup.menu,
    getter=ScoreHandler.profile_score,
)

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row, Start
from aiogram_dialog.widgets.text import Const

from app.controller.handler import UserHandler, ScoreHandler
from app.view.state import ChallengeStateGroup, MenuStateGroup, TeamStateGroup, ScoreStateGroup, EventStateGroup
from app.view.template import TemplateLoader

menu = Window(
    TemplateLoader.load('profile'),
    Start(Const('Задачи'), id='challenges', state=ChallengeStateGroup.menu),
    Start(Const('Мероприятия'), id='events', state=EventStateGroup.menu),
    Start(Const('Присоединиться к команде'), id='teams', state=TeamStateGroup.menu, when=UserHandler.not_in_team),
    Row(
        Start(Const('Личный рейтинг'), id='personal_rating', state=ScoreStateGroup.user_scoreboard),
        Start(Const('Командный рейтинг'), id='team_rating', state=ScoreStateGroup.team_scoreboard),
    ),
    state=MenuStateGroup.menu,
    getter=ScoreHandler.profile_score,
)

from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row, Start
from aiogram_dialog.widgets.text import Const

from app.controller.handler import UserHandler, ScoreHandler
from app.view.state import (
    ChallengeStateGroup,
    MenuStateGroup,
    TeamStateGroup,
    ScoreStateGroup,
    EventStateGroup,
    AdminStateGroup,
)
from app.view.static import StaticLoader

menu = Window(
    StaticLoader.template('profile'),
    StaticLoader.media('logo.png', ContentType.PHOTO),
    Start(Const('🦾 Задачи'), id='challenges', state=ChallengeStateGroup.menu),
    Start(Const('📆 Мероприятия'), id='events', state=EventStateGroup.menu),
    Start(Const('🤝 Присоединиться к команде'), id='teams', state=TeamStateGroup.menu, when=UserHandler.not_in_team),
    Start(Const('🛠️ Администрирование'), id='admin', state=AdminStateGroup.menu, when=UserHandler.is_admin),
    Row(
        Start(Const('📈 Личный рейтинг'), id='personal_rating', state=ScoreStateGroup.user_scoreboard),
        Start(Const('📊 Командный рейтинг'), id='team_rating', state=ScoreStateGroup.team_scoreboard),
    ),
    state=MenuStateGroup.menu,
    getter=ScoreHandler.profile_score,
)

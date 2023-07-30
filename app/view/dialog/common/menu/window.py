from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row, Start, Url
from aiogram_dialog.widgets.text import Const

from app.controller.handler.user import UserHandler, ScoreHandler
from app.view.state.admin import AdminStateGroup
from app.view.state.common import MenuStateGroup
from app.view.state.user import (
    ChallengeStateGroup,
    TeamStateGroup,
    ScoreStateGroup,
    EventStateGroup,
    SupportStateGroup,
)
from app.view.static import StaticLoader

menu = Window(
    StaticLoader.media("logo.png", ContentType.PHOTO),
    StaticLoader.template("profile"),
    Start(Const("🤝 Присоединиться к команде"), id="teams", state=TeamStateGroup.menu, when=UserHandler.not_in_team),
    Row(
        Start(Const("🦾 Задачи"), id="challenges", state=ChallengeStateGroup.menu),
        Start(Const("📆 Мероприятия"), id="events", state=EventStateGroup.menu)
    ),
    Row(
        Start(Const("📈 Личный рейтинг"), id="personal_rating", state=ScoreStateGroup.user_scoreboard),
        Start(Const("📊 Командный рейтинг"), id="team_rating", state=ScoreStateGroup.team_scoreboard),
    ),
    Start(Const("🛠️ Администрирование"), id="menu", state=AdminStateGroup.menu, when=UserHandler.is_admin),
    Url(Const("✉️ Отправить анти-таск"), Const("https://www.youtube.com/watch?v=dQw4w9WgXcQ")),
    Start(Const("🆘 Поддержка"), id="support", state=SupportStateGroup.menu),
    state=MenuStateGroup.menu,
    getter=ScoreHandler.profile_score,
)

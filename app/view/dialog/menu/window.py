from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row, Start
from aiogram_dialog.widgets.text import Const

from app.controller.handler import UserHandler
from app.utils import TemplateLoader
from app.view.state import ChallengeStateGroup, MenuStateGroup

menu = Window(
    TemplateLoader.load('profile'),
    Start(Const('Задачи'), id='challenges', state=ChallengeStateGroup.menu),
    Button(Const('Мероприятия'), id='events'),
    Button(Const('Участники'), id='menu'),
    Row(
        Button(Const('Личный рейтинг'), id='personal_rating'),
        Button(Const('Командный рейтинг'), id='team_rating'),
    ),
    state=MenuStateGroup.menu,
    getter=UserHandler.find_by_id,
)

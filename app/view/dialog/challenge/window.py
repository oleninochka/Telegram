from operator import attrgetter

from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, SwitchTo, ScrollingGroup, Select, Cancel
from aiogram_dialog.widgets.text import Const, Format

from app.controller.handler import ChallengeHandler
from app.utils import back
from app.view.state import ChallengeStateGroup
from app.view.template import TemplateLoader

menu = Window(
    TemplateLoader.load('challenge/list'),
    ScrollingGroup(
        Select(
            Format('{item.weight} | {item.name}'),
            item_id_getter=attrgetter('id'),
            items='challenges',
            id='challenge_select',
            on_click=ChallengeHandler.select,
        ),
        width=1,
        height=5,
        id='challenge_group',
    ),
    Cancel(back, id='back'),
    getter=ChallengeHandler.list_challenges,
    state=ChallengeStateGroup.menu,
)

select = Window(
    TemplateLoader.load('challenge/challenge'),
    Row(
        SwitchTo(back, id='back', state=ChallengeStateGroup.menu),
        SwitchTo(Const('🚩 Сдать флаг'), id='submit', state=ChallengeStateGroup.submit),
    ),
    getter=ChallengeHandler.render,
    state=ChallengeStateGroup.select,
)

submit = Window(
    Const('Введите флаг:'),
    SwitchTo(back, id='back', state=ChallengeStateGroup.select),
    MessageInput(ChallengeHandler.submit),
    state=ChallengeStateGroup.submit,
)

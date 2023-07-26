from operator import attrgetter

from aiogram.types import CallbackQuery
from aiogram.utils.markdown import html_decoration as hd
from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, SwitchTo, ScrollingGroup, Select
from aiogram_dialog.widgets.text import Const, Format

from app.controller.handler import ChallengeHandler
from app.utils import TemplateLoader
from app.view.state import MenuStateGroup, ChallengeStateGroup


async def open_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.done()
    await dialog_manager.start(state=MenuStateGroup.menu)


menu = Window(
    Const(hd.bold('Доступные задачи:')),
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
    getter=ChallengeHandler.list_challenges,
    state=ChallengeStateGroup.menu,
)

challenge = Window(
    TemplateLoader.load('challenge'),
    Row(
        SwitchTo(Const('Назад'), id='back', state=ChallengeStateGroup.menu),
        SwitchTo(Const('Сдать флаг'), id='submit', state=ChallengeStateGroup.submit),
    ),
    getter=ChallengeHandler.render_challenge,
    state=ChallengeStateGroup.challenge,
)

submit = Window(
    Const('Введите флаг:'),
    MessageInput(ChallengeHandler.submit),
    state=ChallengeStateGroup.submit,
)

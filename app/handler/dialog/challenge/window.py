from aiogram.types import CallbackQuery
from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, SwitchTo
from aiogram_dialog.widgets.text import Const

from app.handler.state import MenuStateGroup, ChallengeStateGroup
from app.service import ChallengeService
from app.utils import TemplateLoader


async def open_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.done()
    await dialog_manager.start(state=MenuStateGroup.menu)


menu = Window(
    TemplateLoader.load('challenges'),
    Row(
        Button(Const('Назад'), id='back', on_click=open_menu),
        SwitchTo(Const('Выбрать'), id='select', state=ChallengeStateGroup.select),
    ),
    getter=ChallengeService.list_challenges,
    state=ChallengeStateGroup.menu,
)

select = Window(
    Const('Введите ID задачи:'),
    MessageInput(ChallengeService.select),
    SwitchTo(Const('Назад'), id='back', state=ChallengeStateGroup.menu),
    state=ChallengeStateGroup.select,
)

challenge = Window(
    TemplateLoader.load('challenge'),
    Row(
        SwitchTo(Const('Назад'), id='back', state=ChallengeStateGroup.menu),
        SwitchTo(Const('Сдать флаг'), id='submit', state=ChallengeStateGroup.submit),
    ),
    getter=ChallengeService.render_challenge,
    state=ChallengeStateGroup.challenge
)

submit = Window(
    Const('Введите флаг:'),
    MessageInput(ChallengeService.submit),
    state=ChallengeStateGroup.submit
)

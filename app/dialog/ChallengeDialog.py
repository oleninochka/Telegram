from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode, Window, Dialog
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, SwitchTo
from aiogram_dialog.widgets.text import Const

from app.service import ChallengeService
from app.templates.TemplateLoader import TemplateLoader


async def open_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.done()
    from app.dialog import MenuDialog
    await dialog_manager.start(state=MenuDialog.StateGroup.menu)


class ChallengeDialog:
    class StateGroup(StatesGroup):
        menu = State()
        select = State()
        challenge = State()
        submit = State()

    menu = Window(
        TemplateLoader.load('challenges'),
        Row(
            Button(Const('Назад'), id='back', on_click=open_menu),
            SwitchTo(Const('Выбрать'), id='select', state=StateGroup.select),
        ),
        getter=ChallengeService.list_challenges,
        state=StateGroup.menu,
    )

    select = Window(
        Const('Введите ID задачи:'),
        MessageInput(ChallengeService.select),
        SwitchTo(Const('Назад'), id='back', state=StateGroup.menu),
        state=StateGroup.select,
    )

    challenge = Window(
        TemplateLoader.load('challenge'),
        Row(
            SwitchTo(Const('Назад'), id='back', state=StateGroup.menu),
            SwitchTo(Const('Сдать флаг'), id='submit', state=StateGroup.submit),
        ),
        getter=ChallengeService.render_challenge,
        state=StateGroup.challenge
    )

    submit = Window(
        Const('Введите флаг:'),
        MessageInput(ChallengeService.submit),
        state=StateGroup.submit
    )

    dialog = Dialog(menu, select, challenge, submit)

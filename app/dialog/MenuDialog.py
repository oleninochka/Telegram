from aiogram.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

from app.service.UserService import UserService
from app.templates.TemplateLoader import TemplateLoader


async def open_challenges(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.done()
    from app.dialog import ChallengeDialog
    await dialog_manager.start(state=ChallengeDialog.StateGroup.menu)


class MenuDialog:
    class StateGroup(StatesGroup):
        menu = State()
        list_users = State()

    menu = Window(
        TemplateLoader.load('profile'),
        Button(Const('Список задач'), id='challenges'),
        Button(Const('Мероприятия'), id='events'),
        Button(Const('Участники'), id='menu'),
        Row(
            Button(Const('Личный рейтинг'), id='personal_rating'),
            Button(Const('Командный рейтинг'), id='team_rating'),
        ),
        state=StateGroup.menu,
        getter=UserService.find_by_id,
    )

    dialog = Dialog(menu)

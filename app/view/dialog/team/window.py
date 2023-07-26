from operator import attrgetter

from aiogram.utils.markdown import html_decoration as hd
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, SwitchTo, ScrollingGroup, Select, Cancel
from aiogram_dialog.widgets.text import Const, Format

from app.controller.handler import TeamHandler
from app.view.state import TeamStateGroup

menu = Window(
    Const(hd.bold('Команды:')),
    ScrollingGroup(
        Select(
            Format('{item.name}'),
            item_id_getter=attrgetter('id'),
            items='teams',
            id='team_select',
            on_click=TeamHandler.select,
        ),
        width=1,
        height=5,
        id='team_group',
    ),
    Cancel(Const('Назад'), id='back'),
    getter=TeamHandler.list_teams,
    state=TeamStateGroup.menu,
)

select = Window(
    Format('{item.name}'),
    Row(
        SwitchTo(Const('Назад'), id='back', state=TeamStateGroup.menu),
        SwitchTo(Const('Присоединиться'), id='submit', state=TeamStateGroup.participate),
    ),
    getter=TeamHandler.render,
    state=TeamStateGroup.select,
)

participate = Window(
    Const('Введите инвайт-токен:'),
    MessageInput(TeamHandler.participate),
    state=TeamStateGroup.participate,
)
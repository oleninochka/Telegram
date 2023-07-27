from operator import attrgetter

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, ScrollingGroup, Select, SwitchTo
from aiogram_dialog.widgets.text import Const

from app.controller.handler import EventHandler
from app.view.state import EventStateGroup
from app.view.template import TemplateLoader

menu = Window(
    TemplateLoader.load('event/list'),
    ScrollingGroup(
        Select(
            TemplateLoader.load('event/preview'),
            item_id_getter=attrgetter('id'),
            items='events',
            id='event_select',
            on_click=EventHandler.select,
        ),
        width=1,
        height=5,
        id='event_group',
    ),
    Cancel(Const('Назад'), id='back'),
    getter=EventHandler.list_events,
    state=EventStateGroup.menu,
)

select = Window(
    TemplateLoader.load('event/event'),
    SwitchTo(Const('Назад'), id='back', state=EventStateGroup.menu),
    getter=EventHandler.render,
    state=EventStateGroup.select,
)

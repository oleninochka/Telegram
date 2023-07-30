from operator import attrgetter

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, ScrollingGroup, Select, SwitchTo

from app.controller.handler.user import EventHandler
from app.widgets import back
from app.view.state.user import EventStateGroup
from app.view.static import StaticLoader

menu = Window(
    StaticLoader.template("event/list"),
    ScrollingGroup(
        Select(
            StaticLoader.template("event/preview"),
            item_id_getter=attrgetter("id"),
            items="events",
            id="event_select",
            on_click=EventHandler.select,
        ),
        width=1,
        height=5,
        id="event_group",
    ),
    Cancel(back, id="back"),
    getter=EventHandler.list_events,
    state=EventStateGroup.menu,
)

select = Window(
    StaticLoader.template("event/event"),
    SwitchTo(back, id="back", state=EventStateGroup.menu),
    getter=EventHandler.render,
    state=EventStateGroup.select,
)

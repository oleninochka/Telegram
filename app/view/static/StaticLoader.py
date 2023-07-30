import os

from aiogram.types import ContentType
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Jinja


class StaticLoader:
    base_path = os.path.dirname(__file__)

    @staticmethod
    def template(name: str) -> Jinja:
        path = os.path.join(StaticLoader.base_path, "templates", f"{name}.j2")
        with open(path, encoding="utf-8") as template:
            return Jinja(template.read())

    @staticmethod
    def media(name: str, content: ContentType) -> StaticMedia:
        path = os.path.join(StaticLoader.base_path, "media", name)
        return StaticMedia(path=path, type=content)

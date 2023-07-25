import os

from aiogram_dialog.widgets.text import Jinja


class TemplateLoader:
    base_path = os.path.dirname(__file__)

    @staticmethod
    def load(name: str) -> Jinja:
        path = os.path.join(TemplateLoader.base_path, 'resources', f'{name}.j2')
        template = open(path, encoding='utf-8').read()
        return Jinja(template)

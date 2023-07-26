from typing import Dict

import dacite

from app.api.dto.base import BaseDto


class BaseEntity(BaseDto):
    @classmethod
    def parse(cls, data: Dict):
        return dacite.from_dict(cls, data)

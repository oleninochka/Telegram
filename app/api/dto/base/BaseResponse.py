from dataclasses import dataclass
from datetime import datetime
from typing import Dict

import dacite
from dacite import Config
from pytz import timezone

from app.api.dto.base.Serializable import Serializable


@dataclass
class BaseResponse(Serializable):
    @staticmethod
    def datetime_from_string(iso_string: str) -> datetime:
        time = datetime.fromisoformat(iso_string)
        if time.tzinfo is None:
            time = time.replace(tzinfo=timezone("UTC"))
        return time.astimezone(timezone("Europe/Moscow"))

    @classmethod
    def parse(cls, data: Dict):
        return dacite.from_dict(cls, data, Config({datetime: BaseResponse.datetime_from_string}))

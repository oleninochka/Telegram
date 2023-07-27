from dataclasses import dataclass
from datetime import datetime
from typing import Dict

import dacite
from dacite import Config

from app.api.dto.base.Serializable import Serializable


@dataclass
class BaseResponse(Serializable):
    @classmethod
    def parse(cls, data: Dict):
        return dacite.from_dict(cls, data, Config({datetime: datetime.fromisoformat}))

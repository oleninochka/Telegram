from typing import Dict

import dacite


class BaseResponse:
    @classmethod
    def parse(cls, data: Dict):
        return dacite.from_dict(cls, data)

from dataclasses import dataclass

from app.api.dto.base import Serializable


@dataclass
class SubmitRequest(Serializable):
    userId: str
    flag: str

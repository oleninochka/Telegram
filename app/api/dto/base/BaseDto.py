from abc import ABC, abstractmethod
from typing import Dict


class BaseDto(ABC):
    @classmethod
    @abstractmethod
    def parse(cls, data: Dict):
        pass

import json
from abc import ABC
from dataclasses import asdict, dataclass
from typing import Dict


@dataclass
class Serializable(ABC):
    def as_dict(self) -> Dict:
        return asdict(self)

    def as_json(self) -> Dict:
        return json.loads(json.dumps(asdict(self), default=str))

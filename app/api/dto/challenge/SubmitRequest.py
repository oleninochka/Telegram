from dataclasses import dataclass


@dataclass
class SubmitRequest:
    userId: str
    flag: str

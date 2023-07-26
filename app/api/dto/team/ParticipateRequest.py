from dataclasses import dataclass


@dataclass
class ParticipateRequest:
    userId: str
    invite: str

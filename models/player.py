from dataclasses import dataclass
from typing import List

@dataclass
class Player:
    id: int
    name: str
    season: str

    positions: List[str]

    rating: int  # overall rating (simple for now)

    attack: int
    defence: int
    passing: int
    physical: int
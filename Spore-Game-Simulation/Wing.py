from BodyParts import BodyParts
import Movement
from typing import Set


class Wing(BodyParts):
    def __init__(self, count):
        super().__init__(
            name="wing",
            attack_add=0,
            attack_mul=1.0,
            # speed_boost=0,
            movements_provided=None,
            count=count,
        )

    def given_movements(self) -> Set[Movement]:
        if self.count >= 2:
            return {Movement.FLY, Movement.CRAWL}
        else:
            return {Movement.CRAWL}

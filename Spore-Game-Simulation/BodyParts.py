from Movement import Movement
from typing import Set, Optional


class BodyParts:
    def __init__(
        self,
        name: str,
        attack_add: int = 0,
        attack_mul: float = 1.0,
        count: int = 0,
        movements_provided: Optional[Set[Movement]] = None,
    ):
        self.name = name
        self.attack_add = attack_add
        self.attack_mul = attack_mul
        self.count = count
        self.movements_provided = movements_provided or set()

    def given_movements(self) -> Set[Movement]:
        return set(self.movements_provided)

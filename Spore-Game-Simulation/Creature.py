from BodyParts import BodyParts
from dataclasses import dataclass


@dataclass
class Creature:
    health: int
    stamina: int
    attack_force: int
    position: int
    body_parts: set[BodyParts]

    def add_part(self, part: BodyParts):
        self.body_parts.add(part)

    def __str__(self):
        parts = ", ".join(
            f"{part.name}(count={getattr(part, 'count', '-')})"
            for part in self.body_parts
        )
        return (
            f"Creature("
            f"health={self.health}, stamina={self.stamina}, "
            f"attack_force={self.attack_force}, position={self.position}, "
            f"body_parts=[{parts}]"
            f")"
        )

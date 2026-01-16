from typing import Set
from Movement import Movement, CRAWL
from Creature import Creature


class BoostAbilities:
    @staticmethod
    def available_movements(creature: Creature) -> Set[Movement]:
        movements = set()
        for curr_part in creature.body_parts:
            movements.update(curr_part.given_movements())
        if not movements:
            movements.add(CRAWL)
        return movements

    @staticmethod
    def attack_boost(creature: Creature) -> int:
        add_attack = sum(part.attack_add for part in creature.body_parts)
        mul = 1
        for part in creature.body_parts:
            mul *= part.attack_mul
        final_attack = (creature.attack_force + add_attack) * mul
        creature.attack_force = final_attack
        return final_attack

    @staticmethod
    def can_use_movement(creature: Creature, movement: Movement) -> bool:
        return creature.stamina >= movement.required_stamina

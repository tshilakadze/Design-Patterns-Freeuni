from Claw import Claw
from Creature import Creature
from Leg import Leg
from Teeth import Teeth
from typing import List
from Wing import Wing

import random


class EvolutionPhase:
    @staticmethod
    def body_part_choices() -> List[List[int]]:
        return [[0, 1, 2], [0, 1, 2], [1, 2, 3, 4], [0, 3, 6, 9]]

    def random_creature(
        self, position: int, health: int, stamina: int, attack_force: int
    ) -> Creature:
        creature = Creature(
            health=health,
            stamina=stamina,
            attack_force=attack_force,
            position=position,
            body_parts=set(),
        )
        curr_id = 0
        for each_list in self.body_part_choices():
            number = random.choice(each_list)
            if curr_id == 0:
                leg = Leg(count=number)
                creature.add_part(leg)
            if curr_id == 1:
                wing = Wing(count=number)
                creature.add_part(wing)
            if curr_id == 2:
                claw = Claw(mul=number)
                creature.add_part(claw)
            if curr_id == 3:
                tooth = Teeth(boost=number)
                creature.add_part(tooth)
            curr_id += 1
        return creature

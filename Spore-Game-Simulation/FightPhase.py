from BoostAbilities import BoostAbilities
from Creature import Creature
from enum import Enum, auto


class FightResult(Enum):
    DRAW = auto()
    PREDATOR_WON = auto()
    PREY_WON = auto()


class FightPhase:
    def __init__(self, boosted_abilities=BoostAbilities):
        self.boosted_abilities = boosted_abilities

    def fight(
        self, predator: Creature, prey: Creature, boosted_abilities=BoostAbilities
    ):
        predator_attack = boosted_abilities.attack_boost(predator)
        prey_attack = boosted_abilities.attack_boost(prey)
        while True:
            prey.health -= predator_attack
            predator.health -= prey_attack
            if predator.health <= 0 and prey.health <= 0:
                return FightResult.DRAW
            if predator.health <= 0:
                return FightResult.PREY_WON
            if prey.health <= 0:
                return FightResult.PREDATOR_WON

from Creature import Creature
from Movement import Movement, CRAWL
from BoostAbilities import BoostAbilities
from enum import Enum, auto


class ChaseResult(Enum):
    CAUGHT = auto()
    ESCAPED = auto()


class ChasePhase:
    def __init__(self, boosted_abilities=BoostAbilities):
        self.boosted_abilities = boosted_abilities

    # @staticmethod
    def choose_movement(
        self, creature: Creature, boosted_abilities=BoostAbilities
    ) -> Movement:
        possible_movements = boosted_abilities.available_movements(creature)
        if not possible_movements:
            return CRAWL
        best_move = None
        number = 0
        for curr_move in possible_movements:
            if (
                number < curr_move.speed
                and creature.stamina >= curr_move.required_stamina
            ):
                number = curr_move.speed
                best_move = curr_move
        return best_move

    def chasing(
        self, predator: Creature, prey: Creature, boosted_abilities=BoostAbilities
    ):
        while True:
            predator_move = self.choose_movement(predator, boosted_abilities)
            prey_move = self.choose_movement(prey, boosted_abilities)
            if predator_move:
                predator.position += predator_move.speed
                predator.stamina -= predator_move.stamina_cost
            if prey_move:
                prey.position += prey_move.speed
                prey.stamina -= prey_move.stamina_cost
            if predator.position >= prey.position:
                return ChaseResult.CAUGHT
            if predator.stamina <= 0:
                return ChaseResult.ESCAPED

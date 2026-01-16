import random

from EvolutionPhase import EvolutionPhase
from ChasePhase import ChasePhase, ChaseResult
from FightPhase import FightPhase, FightResult

STARTING_HEALTH = 100
STARTING_ATTACK = 5
MINIMUM_STAMINA = 50
MAXIMUM_STAMINA = 150
PREDATOR_STAMINA_ADDITION = 100
MIN_LOCATION = 0
MAX_LOCATION = 1000
NUMBER_OF_SIMULATIONS = 100


class GameSimulation:
    def __init__(self):
        self.evolution = EvolutionPhase()
        self.chase_phase = ChasePhase()
        self.fight_phase = FightPhase()

    def launch_game(self):
        print("Launching game")
        health_prey = STARTING_HEALTH
        stamina_prey = random.randint(MINIMUM_STAMINA, MAXIMUM_STAMINA)
        attack_prey = STARTING_ATTACK
        prey_location = random.randint(MIN_LOCATION, MAX_LOCATION)

        health_predator = STARTING_HEALTH
        stamina_predator = random.randint(
            MINIMUM_STAMINA + PREDATOR_STAMINA_ADDITION,
            MAXIMUM_STAMINA + PREDATOR_STAMINA_ADDITION,
        )
        attack_predator = STARTING_ATTACK
        predator_location = 0

        predator = self.evolution.random_creature(
            predator_location,
            health_predator,
            stamina_predator,
            attack_predator,
        )
        prey = self.evolution.random_creature(
            prey_location, health_prey, stamina_prey, attack_prey
        )

        if prey and predator:
            print("Two creatures created:")
            print(predator)
            print(prey)
        chase_result = self.chase_phase.chasing(predator, prey)
        if chase_result == ChaseResult.ESCAPED:
            print("Prey ran into infinity")
        else:
            print("Predator has caught prey, fight begins")
            fight_result = self.fight_phase.fight(predator, prey)
            if fight_result == FightResult.PREDATOR_WON:
                print("Some R-rated things have happened")
            if fight_result == FightResult.PREY_WON:
                print("Prey ran into infinity")
            if fight_result == FightResult.DRAW:
                print("No winner")


if __name__ == "__main__":
    for i in range(NUMBER_OF_SIMULATIONS):
        sim = GameSimulation()
        sim.launch_game()

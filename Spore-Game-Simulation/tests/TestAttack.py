import unittest

from Claw import Claw
from Creature import Creature
from BoostAbilities import BoostAbilities
from Teeth import Teeth
import random


class TestingAttack(unittest.TestCase):
    def test_claws(self):
        base_attack = 5
        multiplier = random.randint(1, 9)
        creature_1 = Creature(
            100,
            100,
            base_attack,
            0,
            set(),
        )
        claw_small = Claw(multiplier)
        creature_1.add_part(claw_small)
        BoostAbilities.attack_boost(creature_1)

        expected_attack = base_attack * multiplier
        self.assertEqual(creature_1.attack_force, expected_attack)

    def test_teeth(self):
        base_attack = 5
        booster = random.randint(0, 9)
        creature_1 = Creature(
            100,
            100,
            base_attack,
            0,
            set(),
        )
        tooth = Teeth(booster)
        creature_1.add_part(tooth)
        BoostAbilities.attack_boost(creature_1)
        expected_attack = base_attack + booster
        self.assertEqual(creature_1.attack_force, expected_attack)

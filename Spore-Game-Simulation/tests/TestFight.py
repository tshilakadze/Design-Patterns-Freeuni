import unittest

from Creature import Creature
from FightPhase import FightPhase, FightResult
from BoostAbilities import BoostAbilities


class TestFight(unittest.TestCase):
    def test_fight_predator(self):
        base_attack = 1
        predator = Creature(100, 100, base_attack * 50, 0, set())
        prey = Creature(100, 100, base_attack, 0, set())
        boost_abilities = BoostAbilities()
        fight_obj = FightPhase(boost_abilities)
        result = fight_obj.fight(predator, prey)
        expected = FightResult.PREDATOR_WON
        self.assertEqual(expected, result)

    def test_fight_prey(self):
        base_attack = 1
        predator = Creature(100, 100, base_attack, 0, set())
        prey = Creature(100, 100, base_attack * 50, 0, set())
        boost_abilities = BoostAbilities()
        fight_obj = FightPhase(boost_abilities)
        result = fight_obj.fight(predator, prey)
        expected = FightResult.PREY_WON
        self.assertEqual(expected, result)

    def test_fight_draw(self):
        base_attack = 1
        predator = Creature(100, 100, base_attack, 0, set())
        prey = Creature(100, 100, base_attack, 0, set())
        boost_abilities = BoostAbilities()
        fight_obj = FightPhase(boost_abilities)
        result = fight_obj.fight(predator, prey)
        expected = FightResult.DRAW
        self.assertEqual(expected, result)

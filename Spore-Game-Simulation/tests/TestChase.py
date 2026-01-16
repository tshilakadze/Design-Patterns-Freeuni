import unittest

from Creature import Creature
from BoostAbilities import BoostAbilities
from ChasePhase import ChasePhase, ChaseResult
from Leg import Leg
from Wing import Wing
from Movement import HOP, RUN, CRAWL, FLY


class TestChase(unittest.TestCase):
    def test_no_leg(self):
        creature = Creature(100, 100, 0, 0, set())
        leg = Leg(0)
        creature.add_part(leg)
        boost_abilities = BoostAbilities()
        chase_obj = ChasePhase(boost_abilities)
        movement = chase_obj.choose_movement(creature)
        expected = CRAWL
        self.assertEqual(movement, expected)

    def test_one_leg(self):
        creature = Creature(100, 100, 0, 0, set())
        leg = Leg(1)
        creature.add_part(leg)
        boost_abilities = BoostAbilities()
        chase_obj = ChasePhase(boost_abilities)
        movement = chase_obj.choose_movement(creature)
        expected = HOP
        self.assertEqual(movement, expected)

    def test_two_leg(self):
        creature = Creature(100, 100, 0, 0, set())
        leg = Leg(2)
        creature.add_part(leg)
        boost_abilities = BoostAbilities()
        chase_obj = ChasePhase(boost_abilities)
        movement = chase_obj.choose_movement(creature)
        expected = RUN
        self.assertEqual(movement, expected)

    def test_one_wing(self):
        creature = Creature(100, 100, 0, 0, set())
        wings = Wing(1)
        creature.add_part(wings)
        boost_abilities = BoostAbilities()
        chase_obj = ChasePhase(boost_abilities)
        movement = chase_obj.choose_movement(creature)
        expected = CRAWL
        self.assertEqual(movement, expected)

    def test_two_wing(self):
        creature = Creature(100, 100, 0, 0, set())
        wings = Wing(2)
        creature.add_part(wings)
        boost_abilities = BoostAbilities()
        chase_obj = ChasePhase(boost_abilities)
        movement = chase_obj.choose_movement(creature)
        expected = FLY
        self.assertEqual(movement, expected)

    def test_chase_process(self):
        base_stamina = 1
        predator = Creature(100, base_stamina * 100, 0, 0, set())
        prey = Creature(100, base_stamina, 0, 1, set())
        boost_abilities = BoostAbilities()
        chase_obj = ChasePhase(boost_abilities)
        result = chase_obj.chasing(predator, prey)
        expected = ChaseResult.CAUGHT
        self.assertEqual(result, expected)

    def test_chase_process_prey(self):
        base_stamina = 1
        predator = Creature(100, base_stamina, 0, 0, set())
        prey = Creature(100, base_stamina * 100, 0, 1, set())
        boost_abilities = BoostAbilities()
        chase_obj = ChasePhase(boost_abilities)
        result = chase_obj.chasing(predator, prey)
        expected = ChaseResult.ESCAPED
        self.assertEqual(result, expected)

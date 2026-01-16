import unittest
from Leg import Leg
from Wing import Wing
from Creature import Creature
from BoostAbilities import BoostAbilities
from Movement import CRAWL, HOP, WALK, RUN, FLY


class TestParts(unittest.TestCase):
    def test_no_legs(self):
        leg = Leg(0)
        moves = leg.given_movements()
        expected = {CRAWL}
        self.assertEqual(moves, expected)

    def test_one_leg(self):
        leg = Leg(1)
        moves = leg.given_movements()
        expected = {CRAWL, HOP}
        self.assertEqual(moves, expected)

    def test_two_leg(self):
        leg = Leg(2)
        moves = leg.given_movements()
        expected = {CRAWL, HOP, WALK, RUN}
        self.assertEqual(moves, expected)

    def test_wings(self):
        wing_zero = Wing(0)
        moves = wing_zero.given_movements()
        expected = {CRAWL}
        wing_one = Wing(1)
        moves_one = wing_one.given_movements()
        wing_two = Wing(2)
        moves_two = wing_two.given_movements()
        expected_two = {CRAWL, FLY}
        self.assertEqual(moves, expected)
        self.assertEqual(moves_one, expected)
        self.assertEqual(moves_two, expected_two)

    def test_can_use_movement(self):
        creature = Creature(100, 10, 1, 0, set())
        self.assertTrue(BoostAbilities.can_use_movement(creature, CRAWL))
        self.assertFalse(BoostAbilities.can_use_movement(creature, HOP))
        self.assertFalse(BoostAbilities.can_use_movement(creature, WALK))

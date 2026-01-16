import unittest
from app.models.habit_types import HabitType
from app.models.group_habits import GroupHabit
from app.services.habit_service import HabitService


class TestHabitService(unittest.TestCase):
    def test_1(self):
        service = HabitService()
        habit_data = {
            "name": "Morning routine",
            "description": "Do some things",
            "category": "Everyday",
            "habit_type": HabitType.GROUP_TYPE,
            "goal": None,
            "parent_id": None,
        }
        habit_1 = service.create_habit(habit_data)
        self.assertEqual(1, len(service.habits))
        habit_1_id = habit_1.habit_id
        self.assertEqual(habit_data.get("name"), habit_1.name)
        self.assertEqual(1, habit_1_id)
        retrieved_habit_1 = service.get_single_habit(1)
        self.assertEqual(habit_data.get("name"), retrieved_habit_1.name)
        child_data = {
            "name": "Breakfast",
            "description": "Eat, don't starve",
            "category": "Health",
            "habit_type": HabitType.BOOLEAN_TYPE,
            "goal": None,
            "parent_id": None,
        }
        child_habit = service.add_sub_habit(habit_1_id, child_data)
        if isinstance(habit_1, GroupHabit):
            self.assertEqual(1, len(habit_1.sub_habit_ids))
        self.assertEqual(habit_1_id, child_habit.parent_id)
        self.assertEqual(2, len(service.habits))
        child_child_1_data = {
            "name": "Food",
            "description": "Eat food",
            "category": "Health",
            "habit_type": HabitType.BOOLEAN_TYPE,
            "goal": None,
            "parent_id": None,
        }
        child_child_2_data = {
            "name": "Food",
            "description": "Eat food",
            "category": "Health",
            "habit_type": HabitType.BOOLEAN_TYPE,
            "goal": None,
            "parent_id": None,
        }
        child_child_1 = service.add_sub_habit(child_habit.habit_id, child_child_1_data)
        child_child_2 = service.add_sub_habit(child_habit.habit_id, child_child_2_data)
        self.assertEqual(4, len(service.habits))
        if isinstance(child_habit, GroupHabit):
            self.assertEqual(2, len(child_habit.sub_habit_ids))
        service.delete_habit(child_habit.habit_id)
        if isinstance(habit_1, GroupHabit):
            self.assertEqual(0, len(habit_1.sub_habit_ids))
        self.assertEqual(1, len(service.habits))

    def test_2(self):
        service = HabitService()
        habit_data = {
            "name": "Morning routine",
            "description": "Do some things",
            "category": "Everyday",
            "habit_type": HabitType.BOOLEAN_TYPE,
        }
        habit_1 = service.create_habit(habit_data)
        update_data = {
            "name": "new name",
            "description": "new description",
            "category": "aaaaaaaaaaaaaaa",
        }
        self.assertEqual("Morning routine", habit_1.name)
        self.assertEqual(1, habit_1.goal)
        service.update_habit(habit_1.habit_id, update_data)
        self.assertEqual("new name", habit_1.name)
        update_data_1 = {"goal": 5.0}
        service.update_habit(habit_1.habit_id, update_data_1)
        self.assertEqual(5, habit_1.goal)

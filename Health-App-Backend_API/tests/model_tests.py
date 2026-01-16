import unittest

from datetime import date
from app.models.boolean_habit import BooleanHabit
from app.models.habit_types import HabitType
from app.models.logs import LogEntry
from app.models.numeric_habit import NumericHabit


class TestModels(unittest.TestCase):
    def test_boolean_habit(self):
        habit1 = BooleanHabit(
            habit_id=1,
            name="Habit1",
            description="Habit 1",
            category="General",
            habit_type=HabitType.BOOLEAN_TYPE,
        )
        user_log_str = LogEntry(1, 1, date.today(), "wer")
        self.assertEqual(habit1.habit_id, 1)
        self.assertEqual(habit1.habit_type.value, "boolean")
        self.assertEqual(habit1.completed(user_log_str.log_value), 0.0)
        user_log_zero = LogEntry(1, 1, date.today(), "0")
        self.assertEqual(habit1.completed(user_log_zero.log_value), 0.0)
        user_log_1 = LogEntry(2, 1, date.today(), "1")
        self.assertEqual(habit1.completed(user_log_1.log_value), 1.0)

    def test_numeric_habit(self):
        habit1 = NumericHabit(
            habit_id=1,
            name="Habit1",
            description="Habit 1",
            category="General",
            habit_type=HabitType.NUMERIC_TYPE,
            goal=10,
        )
        user_log_str = LogEntry(1, 1, date.today(), "wer")
        user_log_zero = LogEntry(1, 1, date.today(), "0")
        user_log_num = LogEntry(2, 1, date.today(), "3")
        self.assertEqual(habit1.completed(user_log_str.log_value), 0.0)
        self.assertEqual(habit1.completed(user_log_zero.log_value), 0.0)
        self.assertEqual(habit1.completed(user_log_num.log_value), 0.3)

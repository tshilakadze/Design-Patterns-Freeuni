import unittest
from app.models.habit_types import HabitType
from app.services.log_service import LogService


class TestLogService(unittest.TestCase):
    def test_1(self):
        log_service = LogService()
        habit_service = log_service.habit_service
        habit_data = {
            "name": "Morning routine",
            "description": "Do some things",
            "category": "Everyday",
            "habit_type": HabitType.BOOLEAN_TYPE,
        }
        habit_1 = habit_service.create_habit(habit_data)
        logs_for_habit_1 = log_service.logs_by_habit[habit_1.habit_id]
        self.assertEqual(
            0, log_service.calculate_total_progress(habit_1, logs_for_habit_1)
        )
        self.assertEqual(
            0, log_service.calculate_current_streak(habit_1, logs_for_habit_1)
        )
        self.assertEqual(
            0, log_service.calculate_maximum_streak(habit_1, logs_for_habit_1)
        )
        self.assertEqual(
            0, log_service.calculate_average_performance(habit_1, logs_for_habit_1)
        )
        log_data = {"value": 1}
        new_log = log_service.record_progress(habit_1.habit_id, log_data)
        self.assertEqual(1, new_log.id)
        self.assertEqual(1, len(log_service.list_logs(habit_1.habit_id)))
        self.assertEqual(
            1, log_service.calculate_total_progress(habit_1, logs_for_habit_1)
        )
        self.assertEqual(
            1, log_service.calculate_current_streak(habit_1, logs_for_habit_1)
        )
        self.assertEqual(
            1, log_service.calculate_maximum_streak(habit_1, logs_for_habit_1)
        )
        self.assertEqual(
            1, log_service.calculate_average_performance(habit_1, logs_for_habit_1)
        )
        self.assertEqual(
            1, log_service.calculate_completion_count(habit_1, logs_for_habit_1)
        )
        new_log_1 = log_service.record_progress(habit_1.habit_id, log_data)
        logs_for_habit_1 = log_service.logs_by_habit[habit_1.habit_id]
        self.assertEqual(
            2, log_service.calculate_completion_count(habit_1, logs_for_habit_1)
        )

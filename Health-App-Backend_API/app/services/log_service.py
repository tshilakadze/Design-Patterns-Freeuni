from collections import defaultdict
from datetime import date, timedelta
from app.models.group_habits import GroupHabit
from app.models.logs import LogEntry
from typing import List, Dict, Any

from app.services.habit_service import HabitService
from app.some_exceptions import InvalidHabitOperationError


class LogService:
    def __init__(self):
        self.logs: Dict[int, LogEntry] = {}
        self.next_log_id: int = 1
        self.logs_by_habit: Dict[int, List[LogEntry]] = defaultdict(list)
        self.habit_service: HabitService = HabitService()

    def record_progress(self, habit_id: int, log_data: Dict[str, Any]) -> LogEntry:
        curr_habit = self.habit_service.get_single_habit(habit_id)
        if isinstance(curr_habit, GroupHabit):
            raise InvalidHabitOperationError(
                "Group habits cannot be logged directly, their progress is derived from sub-habits."
            )
        log_id = self.next_log_id
        self.next_log_id += 1
        new_log = LogEntry(
            id=log_id,
            habit_id=habit_id,
            log_value=log_data["value"],
        )
        self.logs[log_id] = new_log
        self.logs_by_habit[habit_id].append(new_log)
        return new_log

    def list_logs(self, habit_id: int) -> List[LogEntry]:
        return self.logs_by_habit[habit_id]

    def calculate_total_progress(self, habit, logs: List[LogEntry]) -> float:
        result = 0.0
        for log in logs:
            result += habit.completed(log.log_value)
        return result * habit.goal

    def calculate_current_streak(self, habit, logs: List[LogEntry]) -> int:
        if not logs:
            return 0
        daily_completion_status: Dict[date, float] = {
            log.log_date: habit.completed(log.log_value) for log in logs
        }
        current_date = date.today()
        streak = 0
        while True:
            completion = daily_completion_status.get(current_date)
            if completion is not None and completion >= 1.0:
                streak += 1
            else:
                break
            current_date -= timedelta(days=1)
            if current_date < min(daily_completion_status.keys()) - timedelta(days=1):
                break
        return streak

    def calculate_maximum_streak(self, habit, logs: List[LogEntry]) -> int:
        if not logs:
            return 0
        daily_completion_status: Dict[date, float] = {
            log.log_date: habit.completed(log.log_value) for log in logs
        }
        first_logged_date = min(daily_completion_status.keys())
        current_date = first_logged_date
        today = date.today()
        max_streak = 0
        current_streak = 0
        while current_date <= today:
            completion_ratio = daily_completion_status.get(current_date)
            if completion_ratio is not None and completion_ratio >= 1.0:
                current_streak += 1
                if current_streak > max_streak:
                    max_streak = current_streak
            else:
                current_streak = 0
            current_date += timedelta(days=1)
        return max_streak

    def calculate_average_performance(self, habit, logs: List[LogEntry]) -> float:
        today = date.today()
        number_of_days = habit.created_at - today
        return self.calculate_total_progress(habit, logs) / max(1, number_of_days.days)

    def calculate_completion_count(self, habit, logs_for_habit) -> float:
        result = 0.0
        for log in logs_for_habit:
            if habit.completed(log.log_value) >= 1.0:
                result += 1
        return result

    def get_habit_completion_ratio_on_date(
        self, habit_id: int, check_date: date
    ) -> float:
        habit = self.habit_service.get_single_habit(habit_id)
        if isinstance(habit, GroupHabit):
            if not habit.sub_habit_ids:
                return 0.0
            total_ratio = 0.0
            for sub_id in habit.sub_habit_ids:
                child_ratio = self.get_habit_completion_ratio_on_date(
                    sub_id, check_date
                )
                if child_ratio >= 1.0:
                    total_ratio += 1.0
            return total_ratio / len(habit.sub_habit_ids)
        else:
            logs = self.logs_by_habit.get(habit_id, [])
            daily_value = 0.0
            for log in logs:
                if log.log_date == check_date:
                    try:
                        daily_value += float(log.log_value)
                    except (ValueError, TypeError):
                        pass

            return habit.completed(daily_value)

    def calculate_for_group(self, habit: GroupHabit) -> Dict[str, Any]:
        today = date.today()
        today_ratio = self.get_habit_completion_ratio_on_date(habit.habit_id, today)
        sub_habits_count = len(habit.sub_habit_ids)
        count_completed_today = (
            round(today_ratio * sub_habits_count) if sub_habits_count > 0 else 0
        )
        current_date = habit.created_at

        max_streak = 0
        current_streak_counter = 0
        total_daily_ratios = 0.0
        days_counted = 0
        historical_completions_count = 0

        while current_date <= today:
            daily_ratio = self.get_habit_completion_ratio_on_date(
                habit.habit_id, current_date
            )
            total_daily_ratios += daily_ratio
            days_counted += 1
            if daily_ratio >= 1.0:
                historical_completions_count += 1
                current_streak_counter += 1
                if current_streak_counter > max_streak:
                    max_streak = current_streak_counter
            else:
                if current_date != today:
                    current_streak_counter = 0

            current_date += timedelta(days=1)
        final_current_streak = current_streak_counter

        average_perf = (total_daily_ratios / days_counted) if days_counted > 0 else 0.0

        return {
            "habit_id": habit.habit_id,
            "habit_name": habit.name,
            "total_progress": float(count_completed_today),
            "times_habit_was_completed": historical_completions_count,
            "current_streak": final_current_streak,
            "maximum_streak": max_streak,
            "average_performance": average_perf,
        }

    def get_statistics(self, habit_id: int) -> Dict[str, Any]:
        habit = self.habit_service.get_single_habit(habit_id)
        logs_for_habit = self.logs_by_habit[habit_id]
        if isinstance(habit, GroupHabit):
            return self.calculate_for_group(habit)
        return {
            "habit_id": habit_id,
            "habit_name": habit.name,
            "total_progress": self.calculate_total_progress(habit, logs_for_habit),
            "times_habit_was_completed": self.calculate_completion_count(
                habit, logs_for_habit
            ),
            "current_streak": self.calculate_current_streak(habit, logs_for_habit),
            "maximum_streak": self.calculate_maximum_streak(habit, logs_for_habit),
            "average_performance": self.calculate_average_performance(
                habit, logs_for_habit
            ),
        }

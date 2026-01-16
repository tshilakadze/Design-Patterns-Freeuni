from app.models.base_habit import BaseHabit
from app.models.boolean_habit import BooleanHabit
from app.models.group_habits import GroupHabit
from app.models.habit_types import HabitType
from app.models.numeric_habit import NumericHabit
from typing import List, Dict, Any

from app.some_exceptions import HabitNotFoundError, InvalidHabitOperationError


class HabitService:
    def __init__(self):
        self.habits = {}
        self.next_habit_id = 1
        self.HABIT_CLASS_MAP = {
            HabitType.BOOLEAN_TYPE: BooleanHabit,
            HabitType.NUMERIC_TYPE: NumericHabit,
            HabitType.GROUP_TYPE: GroupHabit,
        }

    def create_habit(self, habit_data: dict) -> BaseHabit:
        habit_type = habit_data.pop("habit_type")
        HabitClass = self.HABIT_CLASS_MAP.get(habit_type)
        if not HabitClass:
            raise ValueError(f"Invalid habit type: {habit_type}")
        curr_habit_id = self.next_habit_id
        goal = habit_data.get("goal", 1)
        parent_id = habit_data.get("parent_id")
        new_habit = HabitClass(
            habit_id=curr_habit_id,
            name=habit_data["name"],
            description=habit_data["description"],
            category=habit_data["category"],
            habit_type=habit_type,
            goal=goal,
            parent_id=parent_id,
        )
        self.habits[curr_habit_id] = new_habit
        self.next_habit_id += 1
        return new_habit

    def list_habits(self) -> List[BaseHabit]:
        return list(self.habits.values())

    def get_single_habit(self, habit_id: int) -> BaseHabit:
        if habit_id not in self.habits:
            raise HabitNotFoundError(f"Habit with ID {habit_id} not found.")
        return self.habits[habit_id]

    def update_habit(self, habit_id: int, update_data: Dict[str, Any]) -> BaseHabit:
        curr_habit = self.get_single_habit(habit_id)
        immutable_fields = ["habit_id", "created_at", "habit_type", "parent_id"]
        for field in immutable_fields:
            if field in update_data:
                raise InvalidHabitOperationError(
                    f"Cannot update immutable field: {field}"
                )
        for key, value in update_data.items():
            if hasattr(curr_habit, key):
                setattr(curr_habit, key, value)
            else:
                print(
                    f"Warning: Attempted to set unknown field '{key}' on habit {habit_id}"
                )
        self.habits[habit_id] = curr_habit
        return curr_habit

    def delete_habit(self, habit_id: int):
        habit_to_delete = self.get_single_habit(habit_id)
        if habit_to_delete.parent_id is not None:
            parent_habit = self.get_single_habit(habit_to_delete.parent_id)
            if isinstance(parent_habit, GroupHabit):
                if habit_id in parent_habit.sub_habit_ids:
                    parent_habit.sub_habit_ids.remove(habit_id)
        if isinstance(habit_to_delete, GroupHabit):
            for child_id in list(habit_to_delete.sub_habit_ids):
                self.delete_habit(child_id)
        del self.habits[habit_id]

    def convert_to_group_habit(self, habit_id: int) -> GroupHabit:
        old_habit = self.get_single_habit(habit_id)
        if isinstance(old_habit, GroupHabit):
            return old_habit
        new_group_habit = GroupHabit(
            habit_id=old_habit.habit_id,
            name=old_habit.name,
            description=old_habit.description,
            category=old_habit.category,
            habit_type=HabitType.GROUP_TYPE,
            goal=None,
            parent_id=old_habit.parent_id,
            created_at=old_habit.created_at,
            sub_habit_ids=[],
        )
        self.habits[habit_id] = new_group_habit
        return new_group_habit

    def add_sub_habit(self, parent_id: int, sub_habit_data: dict) -> BaseHabit:
        parent_habit = self.convert_to_group_habit(parent_id)
        sub_habit_data["parent_id"] = parent_id
        sub_habit = self.create_habit(sub_habit_data)
        parent_habit.sub_habit_ids.append(sub_habit.habit_id)
        return sub_habit

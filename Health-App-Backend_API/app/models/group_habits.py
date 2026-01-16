from dataclasses import dataclass, field
from typing import Any

from app.models.base_habit import BaseHabit


@dataclass
class GroupHabit(BaseHabit):
    sub_habit_ids: list[int] = field(default_factory=list)

    def completed(self, log_value: Any) -> float:
        return 0.0

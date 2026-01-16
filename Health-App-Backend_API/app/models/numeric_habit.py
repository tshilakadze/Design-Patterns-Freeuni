from dataclasses import dataclass
from typing import Any

from app.models.base_habit import BaseHabit


@dataclass
class NumericHabit(BaseHabit):
    def completed(self, log_value: Any) -> float:
        if self.goal <= 0:
            return 0.0
        try:
            progress = float(log_value)
            return progress / self.goal
        except (ValueError, TypeError):
            return 0.0

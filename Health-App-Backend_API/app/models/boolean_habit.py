from dataclasses import dataclass
from typing import Any

from app.models.base_habit import BaseHabit


@dataclass
class BooleanHabit(BaseHabit):
    def completed(self, log_value: Any) -> float:
        try:
            value = int(log_value)
            return 1.0 if value == 1 else 0.0
        except ValueError:
            return 0.0

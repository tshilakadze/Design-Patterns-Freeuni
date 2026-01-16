from datetime import date
from abc import ABC, abstractmethod
from typing import Optional, Any
from app.models.habit_types import HabitType
from dataclasses import dataclass, field


@dataclass
class BaseHabit(ABC):
    habit_id: int
    name: str
    description: str
    category: str
    habit_type: HabitType
    goal: Optional[float] = 1
    parent_id: Optional[int] = None
    created_at: date = field(default_factory=date.today)

    @abstractmethod
    def completed(self, log_value: Any) -> float:
        pass

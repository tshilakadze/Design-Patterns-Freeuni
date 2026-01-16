from dataclasses import dataclass, field
from datetime import date
from typing import Any


@dataclass
class LogEntry:
    id: int
    habit_id: int
    log_value: Any
    log_date: date = field(default_factory=date.today)

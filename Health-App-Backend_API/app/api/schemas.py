from pydantic import BaseModel, Field, conint
from typing import Optional, List, Any
from datetime import date
from app.models.habit_types import HabitType


class HabitBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = None
    category: str = Field(..., max_length=50)


class HabitCreate(HabitBase):
    habit_type: HabitType
    goal: Optional[float] = 1
    parent_id: Optional[conint(gt=0)] = None


class HabitUpdate(HabitBase):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    goal: Optional[float] = 1


class HabitResponse(HabitBase):
    habit_id: int
    habit_type: HabitType
    goal: Optional[float] = 1
    parent_id: Optional[int] = None
    created_at: Optional[date]

    class Config:
        from_attributes = True


class GroupHabitResponse(HabitResponse):
    sub_habit_ids: List[int] = []


class LogCreate(BaseModel):
    value: Any = Field(
        ...,
        description="The progress recorded (e.g., 0/1 for boolean, 6.0 for numeric)",
    )


class LogResponse(BaseModel):
    id: int
    habit_id: int
    log_date: date
    raw_value: Any = Field(..., alias="log_value")

    class Config:
        from_attributes = True


class HabitStatsResponse(BaseModel):
    habit_id: int
    habit_name: str
    total_progress: float = Field(..., description="Sum of all raw input values.")
    times_habit_was_completed: int = Field(
        ..., description="Count of days achieving 100% completion."
    )
    current_streak: int
    maximum_streak: int
    average_performance: float = Field(
        ..., description="Average daily performance ratio (0.0 to 1.0)."
    )

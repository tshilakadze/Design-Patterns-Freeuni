from fastapi import FastAPI, APIRouter, HTTPException, Depends, status
from typing import List, Union
from app.api.schemas import (
    HabitCreate,
    HabitResponse,
    GroupHabitResponse,
    HabitUpdate,
    LogCreate,
    LogResponse,
    HabitStatsResponse,
)
from app.services.habit_service import HabitService
from app.services.log_service import LogService
from app.models.group_habits import GroupHabit
from app.some_exceptions import HabitNotFoundError, InvalidHabitOperationError

app = FastAPI(title="Habit Tracker API")

global_habit_service = HabitService()
global_log_service = LogService()
global_log_service.habit_service = global_habit_service


def get_habit_service():
    return global_habit_service


def get_log_service():
    return global_log_service


router = APIRouter(prefix="/habits", tags=["Habits"])


@router.post("", response_model=HabitResponse, status_code=status.HTTP_201_CREATED)
def create_habit(
    req: HabitCreate, habit_service: HabitService = Depends(get_habit_service)
):
    try:
        new_habit_data = req.model_dump()
        new_habit = habit_service.create_habit(new_habit_data)
        if isinstance(new_habit, GroupHabit):
            return GroupHabitResponse.model_validate(new_habit)
        return HabitResponse.model_validate(new_habit)

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("", response_model=List[HabitResponse])
def list_habits(habit_service: HabitService = Depends(get_habit_service)):
    habits = habit_service.list_habits()
    response_list = []
    for habit in habits:
        if isinstance(habit, GroupHabit):
            response_list.append(GroupHabitResponse.model_validate(habit).model_dump())
        else:
            response_list.append(HabitResponse.model_validate(habit).model_dump())

    return response_list


@router.get("/{id}", response_model=HabitResponse)
def get_single_habit(id: int, habit_service: HabitService = Depends(get_habit_service)):
    try:
        habit = habit_service.get_single_habit(id)
        if isinstance(habit, GroupHabit):
            return GroupHabitResponse.model_validate(habit)
        return HabitResponse.model_validate(habit)
    except HabitNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{id}", response_model=HabitResponse)
def update_habit(
    habit_id: int,
    req: HabitUpdate,
    habit_service: HabitService = Depends(get_habit_service),
):
    try:
        update_data = req.model_dump(exclude_unset=True)
        updated_habit = habit_service.update_habit(habit_id, update_data)

        if isinstance(updated_habit, GroupHabit):
            return GroupHabitResponse.model_validate(updated_habit)
        return HabitResponse.model_validate(updated_habit)

    except HabitNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except InvalidHabitOperationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_habit(
    habit_id: int, habit_service: HabitService = Depends(get_habit_service)
):
    try:
        habit_service.delete_habit(habit_id)
        return None
    except HabitNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post(
    "/{id}/subhabits",
    response_model=HabitResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_sub_habit(
    habit_id: int,
    req: HabitCreate,
    habit_service: HabitService = Depends(get_habit_service),
):
    try:
        sub_habit_data = req.model_dump()
        new_sub_habit = habit_service.add_sub_habit(habit_id, sub_habit_data)

        if isinstance(new_sub_habit, GroupHabit):
            return GroupHabitResponse.model_validate(new_sub_habit)
        return HabitResponse.model_validate(new_sub_habit)

    except HabitNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:  # Catching Invalid Habit Type
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post(
    "/{id}/logs", response_model=LogResponse, status_code=status.HTTP_201_CREATED
)
def record_progress(
    habit_id: int, req: LogCreate, log_service: LogService = Depends(get_log_service)
):
    try:
        new_log = log_service.record_progress(habit_id, req.model_dump())
        return LogResponse.model_validate(new_log)
    except HabitNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except InvalidHabitOperationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{id}/logs", response_model=List[LogResponse])
def list_logs(habit_id: int, log_service: LogService = Depends(get_log_service)):
    try:
        logs = log_service.list_logs(habit_id)
        return [LogResponse.model_validate(log) for log in logs]
    except HabitNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{id}/stats", response_model=HabitStatsResponse)
def get_statistics(habit_id: int, log_service: LogService = Depends(get_log_service)):
    try:
        stats = log_service.get_statistics(habit_id)
        return stats
    except HabitNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


app.include_router(router)

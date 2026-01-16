class HabitTrackerError(Exception):
    pass


class HabitNotFoundError(HabitTrackerError):
    pass


class InvalidHabitOperationError(HabitTrackerError):
    pass

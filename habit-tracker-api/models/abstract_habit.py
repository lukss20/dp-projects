from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class AbstractHabit(ABC):
    type_ = ""

    def __init__(self, habit_id: int, name: str, description: str, category: str):
        self.id = habit_id
        self.name = name
        self.description = description
        self.category = category
        self.created_at = datetime.utcnow()
        self.goal = None
        self.logs = []
        self.sub_habits = []

    @property
    def type(self) -> str:
        return self.type_

    def add_sub_habit(self, habit: "AbstractHabit") -> None:
        self.sub_habits.append(habit)

    def add_log(self, value):
        self.logs.append({"date": datetime.utcnow().date(), "value": value})

    @abstractmethod
    def get_total_progress(self) -> int:
        pass

    @abstractmethod
    def get_average(self) -> float:
        pass

    def get_current_streak(self) -> int:
        if not self.logs:
            return 0
        done_dates = {log["date"] for log in self.logs if log["value"]}
        streak = 0
        today = datetime.utcnow().date()
        while today in done_dates:
            streak += 1
            today -= timedelta(days=1)
        return streak

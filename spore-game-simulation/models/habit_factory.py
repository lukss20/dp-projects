from .bool_habit import BoolHabit
from .num_habit import NumHabit


class HabitFactory:
    _id_counter = 1

    @classmethod
    def create(cls, type_: str, name: str, description: str, category: str, goal=None):
        habit_id = cls._id_counter
        cls._id_counter += 1

        if type_ == "boolean":
            h = BoolHabit(habit_id, name, description, category)
            h.goal = goal
            return h
        elif type_ == "numeric":
            h = NumHabit(habit_id, name, description, category)
            h.goal = goal
            return h
        return None

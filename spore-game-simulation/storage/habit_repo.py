class HabitRepo:
    def __init__(self) -> None:
        self.habits = {}

    def add(self, habit):
        self.habits[habit.id] = habit
        return habit

    def get(self, habit_id):
        return self.habits.get(habit_id)

    def list_all(self):
        return list(self.habits.values())

    def delete(self, habit_id):
        self.habits.pop(habit_id, None)

    def add_sub_habit(self, parent_id, child_id):
        parent = self.get(parent_id)
        child = self.get(child_id)
        parent.add_sub_habit(child)

    def add_log(self, habit_id, value):
        habit = self.get(habit_id)
        habit.add_log(value)
        return habit.logs[-1]

from models.habit_factory import HabitFactory


class HabitService:
    def __init__(self, repo):
        self.repo = repo

    def create_habit(self, name, description, category, type_, goal=None):
        habit = HabitFactory.create(type_, name, description, category, goal)
        self.repo.add(habit)
        return habit

    def list_habits(self):
        return self.repo.list_all()

    def add_log(self, habit_id, value):
        return self.repo.add_log(habit_id, value)

    def add_sub_habit(self, parent_id, child_id):
        return self.repo.add_sub_habit(parent_id, child_id)

    def get_stats(self, habit_id):
        habit = self.repo.get(habit_id)
        return {
            "total": habit.get_total_progress(),
            "current_streak": habit.get_current_streak(),
            "average": habit.get_average(),
        }

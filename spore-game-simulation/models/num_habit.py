from .abstract_habit import AbstractHabit


class NumHabit(AbstractHabit):
    type = "numeric"

    def get_total_progress(self) -> int:
        return sum(int(log["value"]) for log in self.logs)

    def get_average(self) -> float:
        total = 0
        for log in self.logs:
            val = log["value"]
            val = int(val)
            total += val
        return total / len(self.logs)

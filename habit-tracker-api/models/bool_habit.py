from .abstract_habit import AbstractHabit


class BoolHabit(AbstractHabit):
    type = "boolean"

    def get_total_progress(self) -> int:
        return sum(1 for log in self.logs if log["value"].lower() == "true")

    def get_average(self) -> float:
        total = 0
        for log in self.logs:
            val = log["value"]
            if val.lower() == "true":
                val = 1
            elif val.lower() == "false":
                val = 0
            total += val
        return total / len(self.logs)

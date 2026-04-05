import pytest

from models.abstract_habit import AbstractHabit
from storage.habit_repo import HabitRepo


class TempHabit(AbstractHabit):
    type_ = "temp"

    def get_total_progress(self):
        return sum(int(log["value"]) for log in self.logs)

    def get_average(self):
        return sum(int(log["value"]) for log in self.logs) / len(self.logs) if self.logs else 0


@pytest.fixture
def repo():
    return HabitRepo()


@pytest.fixture
def habit():
    return TempHabit(1, "luka", "", "")


def test_add_and_get(repo, habit):
    repo.add(habit)
    assert repo.get(habit.id) == habit


def test_list_all(repo, habit):
    repo.add(habit)
    assert repo.list_all() == [habit]


def test_delete(repo, habit):
    repo.add(habit)
    repo.delete(habit.id)
    assert repo.get(habit.id) is None


def test_add_sub_habit(repo, habit):
    sub = TempHabit(2, "luka", "", "")
    repo.add(habit)
    repo.add(sub)
    repo.add_sub_habit(habit.id, sub.id)
    assert sub in habit.sub_habits


def test_add_log(repo, habit):
    repo.add(habit)
    repo.add_log(habit.id, 5)
    assert habit.logs[-1]["value"] == 5

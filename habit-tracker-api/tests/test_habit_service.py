import pytest

from services.habit_service import HabitService
from storage.habit_repo import HabitRepo


@pytest.fixture
def repo():
    return HabitRepo()


@pytest.fixture
def service(repo):
    return HabitService(repo)


def test_create_habit(service):
    habit = service.create_habit("luka", "", "", "boolean", goal=10)
    assert habit.name == "luka"
    assert habit.goal == 10


def test_list_habits(service):
    habit = service.create_habit("luka", "", "", "boolean")
    habits = service.list_habits()
    assert habit in habits


def test_add_log(service):
    habit = service.create_habit("luka", "", "", "numeric")
    log = service.add_log(habit.id, 5)
    assert log["value"] == 5


def test_add_sub_habit(service):
    parent = service.create_habit("luka", "", "", "boolean")
    child = service.create_habit("gio", "", "", "boolean")
    service.add_sub_habit(parent.id, child.id)
    assert child in parent.sub_habits


def test_get_stats(service):
    habit = service.create_habit("luka", "", "", "numeric")
    service.add_log(habit.id, 2)
    service.add_log(habit.id, 4)
    stats = service.get_stats(habit.id)
    assert stats["total"] == 6
    assert stats["average"] == 3

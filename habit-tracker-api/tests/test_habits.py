import pytest

from models.bool_habit import BoolHabit
from models.habit_factory import HabitFactory
from models.num_habit import NumHabit


def test_boolhabit_progress_and_average():
    habit = BoolHabit(1, "Bool", "", "")
    habit.add_log("true")
    habit.add_log("false")
    habit.add_log("true")
    assert habit.get_total_progress() == 2
    assert habit.get_average() == pytest.approx(2 / 3)


def test_numhabit_progress_and_average():
    habit = NumHabit(1, "Num", "", "")
    habit.add_log(3)
    habit.add_log(7)
    assert habit.get_total_progress() == 10
    assert habit.get_average() == 5


def test_create_boolean_habit():
    habit = HabitFactory.create("boolean", "Bool", "", "", goal=5)
    assert isinstance(habit, BoolHabit)
    assert habit.goal == 5


def test_create_numeric_habit():
    habit = HabitFactory.create("numeric", "Num", "", "", goal=10)
    assert isinstance(habit, NumHabit)
    assert habit.goal == 10

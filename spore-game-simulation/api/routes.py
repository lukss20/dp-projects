from fastapi import APIRouter

from services.habit_service import HabitService
from storage.habit_repo import HabitRepo

repo = HabitRepo()
service = HabitService(repo)
router = APIRouter()


@router.post("/habits")
def create_habit(
    name: str,
    description: str = "",
    category: str = "General",
    type_: str = "boolean",
    goal: int = None,
):
    return service.create_habit(name, description, category, type_, goal).__dict__


@router.get("/habits")
def list_habits():
    return [h.__dict__ for h in service.list_habits()]


@router.get("/habits/{habit_id}")
def get_habit(habit_id: int):
    habit = repo.get(habit_id)
    return habit.__dict__


@router.put("/habits/{habit_id}")
def update_habit(
    habit_id: int,
    name: str = None,
    description: str = None,
    category: str = None,
    goal: int = None,
):
    habit = repo.get(habit_id)
    if name:
        habit.name = name
    if description:
        habit.description = description
    if category:
        habit.category = category
    if goal is not None:
        habit.goal = goal
    return habit.__dict__


@router.delete("/habits/{habit_id}")
def delete_habit(habit_id: int):
    repo.delete(habit_id)
    return {"status": "deleted"}


@router.post("/habits/{habit_id}/subhabits")
def add_sub_habit(habit_id: int, sub_habit_id: int):
    service.add_sub_habit(habit_id, sub_habit_id)
    return {"status": "ok"}


@router.post("/habits/{habit_id}/logs")
def add_log(habit_id: int, value):
    return service.add_log(habit_id, value)


@router.get("/habits/{habit_id}/logs")
def list_logs(habit_id: int):
    habit = repo.get(habit_id)
    return habit.logs


@router.get("/habits/{habit_id}/stats")
def get_stats(habit_id: int):
    return service.get_stats(habit_id)

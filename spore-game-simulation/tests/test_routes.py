from types import SimpleNamespace
from unittest.mock import patch

from fastapi import FastAPI
from fastapi.testclient import TestClient

from api import routes

app = FastAPI()
app.include_router(routes.router)
client = TestClient(app)


def test_create_habit() -> None:
    fake_habit = SimpleNamespace(id=1, name="luka")
    with patch.object(routes, "service") as mock_service:
        mock_service.create_habit.return_value = fake_habit
        response = client.post("/habits", params={"name": "luka"})
        assert response.status_code == 200
        assert response.json()["name"] == "luka"


def test_list_habits() -> None:
    fake_habit = SimpleNamespace(id=1, name="luka")
    with patch.object(routes, "service") as mock_service:
        mock_service.list_habits.return_value = [fake_habit]
        response = client.get("/habits")
        assert response.status_code == 200
        assert response.json()[0]["name"] == "luka"


def test_get_habit() -> None:
    fake_habit = SimpleNamespace(id=1, name="luka")
    with patch.object(routes, "repo") as mock_repo:
        mock_repo.get.return_value = fake_habit
        response = client.get("/habits/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1


def test_update_habit() -> None:
    fake_habit = SimpleNamespace(id=1, name="luka", description="chitaia", category="design", goal=5)
    with patch.object(routes, "repo") as mock_repo:
        mock_repo.get.return_value = fake_habit
        response = client.put("/habits/1", params={"name": "gio", "goal": 10})
        assert response.status_code == 200
        assert fake_habit.name == "gio"
        assert fake_habit.goal == 10


def test_delete_habit() -> None:
    with patch.object(routes, "repo") as mock_repo:
        response = client.delete("/habits/1")
        assert response.status_code == 200
        mock_repo.delete.assert_called_with(1)
        assert response.json() == {"status": "deleted"}


def test_add_sub_habit() -> None:
    with patch.object(routes, "service") as mock_service:
        response = client.post("/habits/1/subhabits", params={"sub_habit_id": 2})
        assert response.status_code == 200
        mock_service.add_sub_habit.assert_called_with(1, 2)
        assert response.json() == {"status": "ok"}


def test_add_log() -> None:
    with patch.object(routes, "service") as mock_service:
        mock_service.add_log.return_value = {"date": "2025-12-03", "value": "5"}
        response = client.post("/habits/1/logs", params={"value": "5"})
        assert response.status_code == 200
        mock_service.add_log.assert_called_with(1, "5")


def test_list_logs() -> None:
    fake_habit = SimpleNamespace()
    fake_habit.logs = [{"date": "2025-12-03", "value": 5}]
    with patch.object(routes, "repo") as mock_repo:
        mock_repo.get.return_value = fake_habit
        response = client.get("/habits/1/logs")
        assert response.status_code == 200
        assert response.json() == fake_habit.logs


def test_get_stats() -> None:
    with patch.object(routes, "service") as mock_service:
        mock_service.get_stats.return_value = {
            "total": 10,
            "current_streak": 3,
            "average": 5,
        }
        response = client.get("/habits/1/stats")
        assert response.status_code == 200
        assert response.json()["total"] == 10

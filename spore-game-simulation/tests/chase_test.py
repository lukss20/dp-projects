import pytest
from chase_strategy import ChaseStrategy
from creature import Creature

def test_predator_catches_prey(monkeypatch):
    predator = Creature("predator", 0)
    predator.stamina = 5
    prey = Creature("prey", 10)
    prey.stamina = 5

    monkeypatch.setattr(predator, "move", lambda: setattr(predator, 'position', predator.position + 3) or setattr(predator, 'stamina', predator.stamina - 1))
    monkeypatch.setattr(prey, "move", lambda: setattr(prey, 'position', prey.position + 1) or setattr(prey, 'stamina', prey.stamina - 1))

    result = ChaseStrategy.greedy_chase(predator, prey)
    assert result is True
    assert predator.position >= prey.position

def test_prey_escapes(monkeypatch):
    predator = Creature("predator", 0)
    predator.stamina = 5
    prey = Creature("prey", 10)
    prey.stamina = 5

    monkeypatch.setattr(predator, "move", lambda: setattr(predator, 'position', predator.position + 1) or setattr(predator, 'stamina', predator.stamina - 1))
    monkeypatch.setattr(prey, "move", lambda: setattr(prey, 'position', prey.position + 2) or setattr(prey, 'stamina', prey.stamina - 1))

    result = ChaseStrategy.greedy_chase(predator, prey)
    assert result is False
    assert predator.position < prey.position

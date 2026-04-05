import pytest
from fight import Fight
from creature import Creature
from unittest.mock import MagicMock, patch

@pytest.fixture
def setup_creatures():
    predator = Creature("predator", 0)
    predator.health = 10
    predator.attack_power = 5

    prey = Creature("prey", 0)
    prey.health = 10
    prey.attack_power = 3

    predator.attack = MagicMock(side_effect=lambda other: setattr(other, 'health', other.health - predator.attack_power))
    prey.attack = MagicMock(side_effect=lambda other: setattr(other, 'health', other.health - prey.attack_power))
    return predator, prey

def test_prey_dies(setup_creatures):
    predator, prey = setup_creatures
    with patch("fight.random.choice", side_effect=lambda x: (predator, prey)):
        fight = Fight(predator, prey)
        result = fight.start()
        assert result == "prey_dead"
        assert prey.health <= 0

def test_predator_dies(setup_creatures):
    predator, prey = setup_creatures
    with patch("fight.random.choice", side_effect=lambda x: (prey, predator)):
        fight = Fight(predator, prey)
        result = fight.start()
        assert result == "predator_dead"
        assert predator.health <= 0

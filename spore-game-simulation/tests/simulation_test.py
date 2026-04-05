import pytest
from simulation import Simulation
from unittest.mock import MagicMock, patch

@patch("simulation.ChaseStrategy")
def test_run_prey_escaped(mockchase):
    mockchase.greedy_chase.return_value = False
    sim = Simulation(1)
    result = sim.run()
    assert result == "prey_escaped"

@patch("simulation.Fight")
@patch("simulation.ChaseStrategy")
def test_run_prey_dead(mockchase, mockfight):
    mockchase.greedy_chase.return_value = True
    fight_instance = mockfight.return_value
    fight_instance.start.return_value = "prey_dead"
    sim = Simulation(2)
    result = sim.run()
    assert result == "prey_dead"

@patch("simulation.Fight")
@patch("simulation.ChaseStrategy")
def test_run_predator_dead(mockchase, mockfight):
    mockchase.greedy_chase.return_value = True
    fight_instance = mockfight.return_value
    fight_instance.start.return_value = "predator_dead"
    sim = Simulation(3)
    result = sim.run()
    assert result == "predator_dead"

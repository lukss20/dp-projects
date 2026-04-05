import pytest
from movement import Crawl, Hop, Walk, Run, Fly
from movement_type import MovementType

def test_movement_can_move():
    crawl = Crawl()
    assert crawl.can_move(1)
    assert not crawl.can_move(0)

    hop = Hop()
    assert hop.can_move(20)
    assert not hop.can_move(1)

def test_movement_distance():
    assert Crawl().move_distance() == 1
    assert Hop().move_distance() == 3
    assert Walk().move_distance() == 4
    assert Run().move_distance() == 6
    assert Fly().move_distance() == 8

def test_choose_movement():
    assert isinstance(MovementType.choose_movement(0, 2, 80), Fly)
    assert isinstance(MovementType.choose_movement(2, 0, 60), Run)
    assert isinstance(MovementType.choose_movement(2, 0, 50), Walk)
    assert isinstance(MovementType.choose_movement(1, 0, 20), Hop)
    assert isinstance(MovementType.choose_movement(0, 0, 0), Crawl)

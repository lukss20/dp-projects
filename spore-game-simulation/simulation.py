import random

from chase_strategy import ChaseStrategy
from creature import Creature
from fight import Fight


class Simulation:

    def __init__(self, id: int):
        self.id = id
        self.predator: Creature | None = None
        self.prey: Creature | None = None

    def evolve_creatures(self) -> None:
        self.predator = Creature("Predator", 0)
        self.predator.evolve_randomly()
        prey_position = random.randint(1, 1000)
        self.prey = Creature("Prey", prey_position)
        self.prey.evolve_randomly()

    def chase_phase(self) -> bool:
        assert self.predator is not None and self.prey is not None
        return ChaseStrategy.greedy_chase(self.predator, self.prey)

    def fight_phase(self) -> str:
        assert self.predator is not None and self.prey is not None
        fight = Fight(self.predator, self.prey)
        return fight.start()

    def run(self) -> str:
        self.evolve_creatures()
        caught = self.chase_phase()
        if not caught:
            return "prey_escaped"
        return self.fight_phase()

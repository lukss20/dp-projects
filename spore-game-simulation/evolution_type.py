import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from creature import Creature


class EvolutionStrategy:

    def evolve(self, creature: "Creature") -> None:
        raise NotImplementedError


class PredatorEvolution(EvolutionStrategy):
    def evolve(self, creature: "Creature") -> None:
        creature.health = random.randint(100, 150)
        creature.stamina = random.randint(150, 200)
        creature.attack_power = random.randint(2, 5)
        creature.claws = random.choices([2, 3, 4], weights=[1, 2, 3])[0]
        creature.teeth = random.choices([3, 6, 9], weights=[1, 2, 3])[0]


class PrayEvolution(EvolutionStrategy):
    def evolve(self, creature: "Creature") -> None:
        creature.health = random.randint(80, 120)
        creature.stamina = random.randint(70, 120)
        creature.attack_power = random.randint(1, 3)
        creature.claws = random.choice([2, 3, 4])
        creature.teeth = random.choice([3, 6, 9])

import random

from evolution_type import PrayEvolution, PredatorEvolution
from movement import Movement
from movement_type import MovementType


class Creature:

    def __init__(self, name: str, position: int):
        self.name = name
        self.position = position
        self.health = 0
        self.stamina = 0
        self.legs = 0
        self.wings = 0
        self.claws = 0
        self.teeth = 0
        self.attack_power = 10
        self.movement_type: Movement | None = None

    def evolve_randomly(self) -> None:
        strategy = PredatorEvolution() if "predator" in self.name.lower()\
            else PrayEvolution()
        strategy.evolve(self)

        self.legs = random.randint(0, 2)
        self.wings = random.randint(0, 2)
        self.attack_power += self.teeth
        self.attack_power *= self.claws

        print(f"[EVOLVE] {self.name} evolved:")
        print(f"  Legs={self.legs}, Wings={self.wings}, Claws={self.claws},"
              f" Teeth={self.teeth}")
        print(f"  Attack Power={self.attack_power}")

    def move(self) -> None:
        self.movement_type = MovementType.choose_movement(self.legs, self.wings,
                                                          self.stamina)
        if self.movement_type.can_move(self.stamina):
            distance = self.movement_type.move_distance()
            self.position += distance
            self.stamina -= self.movement_type.stamina_cost
            print(f"[MOVE] {self.name} moved {distance} units via "
                  f"{self.movement_type.name}. "
                  f"Position={self.position}, Stamina={self.stamina}")
        else:
            print(f"[MOVE] {self.name} is too tired to move! Stamina={self.stamina}")

    def attack(self, other: "Creature") -> None:
        if not self.is_alive():
            return
        damage = self.attack_power
        other.health -= damage
        print(f"[ATTACK] {self.name} hits {other.name} for {damage} damage. "
              f"{other.name} health = {other.health}")

    def is_alive(self) -> bool:
        return self.health > 0

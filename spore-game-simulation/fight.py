import random

from creature import Creature


class Fight:

    def __init__(self, predator: Creature, prey: Creature):
        self.predator = predator
        self.prey = prey

    def start(self) -> str:
        print(f"[FIGHT] {self.predator.name} vs {self.prey.name}")
        while self.predator.is_alive() and self.prey.is_alive():
            attacker, defender = random.choice([(self.predator, self.prey),
                                                (self.prey, self.predator)])
            attacker.attack(defender)

        if self.prey.health <= 0:
            print("Some R-rated things have happened")
            return "prey_dead"
        else:
            print("Pray ran into infinity")
            return "predator_dead"

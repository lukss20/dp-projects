from creature import Creature


class ChaseStrategy:
    @staticmethod
    def greedy_chase(predator: Creature, prey: Creature) -> bool:
        print(f"[CHASE] Predator at {predator.position} | Prey at {prey.position}")
        steps = 0

        while predator.stamina > 0:
            steps += 1
            predator.move()
            prey.move()
            if predator.position >= prey.position:
                print("[CHASE] Predator caught the prey!")
                return True

        print("[CHASE] Prey escaped!")
        return False

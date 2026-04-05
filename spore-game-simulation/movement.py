class Movement:

    def __init__(self, name: str, required_stamina: int, stamina_cost: int, speed: int) -> None:
        self.name = name
        self.required_stamina = required_stamina
        self.stamina_cost = stamina_cost
        self.speed = speed

    def can_move(self, creature_stamina: int) -> bool:
        return creature_stamina >= self.stamina_cost

    def move_distance(self) -> int:
        return self.speed


class Crawl(Movement):
    def __init__(self) -> None:
        super().__init__("Crawl", 0, 1, 1)


class Hop(Movement):
    def __init__(self) -> None:
        super().__init__("Hop", 20, 2, 3)


class Walk(Movement):
    def __init__(self) -> None:
        super().__init__("Walk", 40, 2, 4)


class Run(Movement):
    def __init__(self) -> None:
        super().__init__("Run", 60, 4, 6)


class Fly(Movement):
    def __init__(self) -> None:
        super().__init__("Fly", 80, 4, 8)

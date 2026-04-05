from movement import Crawl, Fly, Hop, Movement, Run, Walk


class MovementType:

    @staticmethod
    def choose_movement(legs: int, wings: int, stamina: int) -> Movement:
        if wings == 2 and stamina >= 80:
            return Fly()
        if legs == 2 and stamina >= 60:
            return Run()
        if legs == 2 and stamina >= 40:
            return Walk()
        if legs >= 1 and stamina >= 20:
            return Hop()
        return Crawl()

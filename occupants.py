from utils import BColors, food


class Occupant:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, fish, result=None):
        return False


class Seaweed(Occupant):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    @food()
    def eat(self, fish, result=None):
        print("I'm alga, i'm eat only sun and oxygen")
        return False


class Herbivores(Occupant):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    @food(Seaweed)
    def eat(self, fish, result=None):
        return fish


class Predator(Occupant):
    DEFAULT_PREDATOR_WEIGHT = 10

    def __init__(self, name, weight):
        super().__init__(name, self.DEFAULT_PREDATOR_WEIGHT)
        self.count_victims = 0

    @food(Herbivores)
    def eat(self, fish, result=None):
        return fish


class Snail(Occupant):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    @food(Seaweed)
    def eat(self, fish, result=None):
        return fish

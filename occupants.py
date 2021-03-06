from utils import BColors, food
from abc import ABCMeta, abstractmethod
from exception import FoodError

class Occupant:
    __metaclass__ = ABCMeta

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.victims = 0

    @abstractmethod
    def eat(self, fish, result=False):
        if not result:
            raise FoodError("I`m doesn`t eat current occupant")

        self.victims += 1
        self.weight += fish.weight
        print(self.name, "say:", "\"" + fish.name + "\"", 'you\'re looking so tasty')

        return True


class Seaweed(Occupant):
    MAX_WEIGHT = 3

    def __init__(self, name, weight):
        super().__init__(name, weight)

    @food()
    def eat(self, fish, result=False):
        return super().eat(fish, result)


class Herbivores(Occupant):
    MAX_WEIGHT = 9

    def __init__(self, name, weight):
        super().__init__(name, weight)

    @food(Seaweed)
    def eat(self, fish, result=False):
        return super().eat(fish, result)


class Predator(Occupant):
    DEFAULT_PREDATOR_WEIGHT = 10

    def __init__(self, name, weight):
        super().__init__(name, self.DEFAULT_PREDATOR_WEIGHT)
        self.count_victims = 0

    @food(Herbivores)
    def eat(self, fish, result=False):
        return super().eat(fish, result)


class Snail(Occupant):
    MAX_WEIGHT = 5

    def __init__(self, name, weight):
        super().__init__(name, weight)

    @food(Seaweed)
    def eat(self, fish, result=False):
        return super().eat(fish, result)

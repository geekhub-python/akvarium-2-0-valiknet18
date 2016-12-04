from utils import BColors, food


class Occupant:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.victims = 0

    def eat(self, fish, result=False):
        if not result:
            return False

        self.victims += 1
        self.weight += fish.weight
        print(self.name, "say:", "\"" + fish.name + "\"", 'you\'re looking so tasty')

        return True


class Seaweed(Occupant):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    @food()
    def eat(self, fish, result=False):
        return super().eat(fish, result)


class Herbivores(Occupant):
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
    def __init__(self, name, weight):
        super().__init__(name, weight)

    @food(Seaweed)
    def eat(self, fish, result=False):
        return super().eat(fish, result)

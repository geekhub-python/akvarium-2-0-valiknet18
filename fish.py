from utils import BColors

class Fish:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, fish):
        print(BColors.OKGREEN, self.name, "say: I don't eat other fishes", BColors.ENDC)
        return False

class Predator(Fish):
    DEFAULT_PREDATOR_WEIGHT = 10

    def __init__(self, name, weight):
        super().__init__(name, self.DEFAULT_PREDATOR_WEIGHT)
        self.count_victims = 0

    def eat(self, fish):
        if (isinstance(fish, Predator)):
            print(BColors.OKBLUE, self.name, "say: I don't eat other predators", BColors.ENDC)
            return False

        self.weight += fish.weight
        self.count_victims += 1

        print(BColors.FAIL, self.name, "say:", "`" + fish.name + "`", "you're look very tasty", BColors.ENDC)

        return True

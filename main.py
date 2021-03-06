#!/usr/bin/env python3

from random import choice
from utils import BColors
from aquarium import Aquarium, AquariumFilter
from exception import FoodError


class Application:
    def __init__(self, aquarium):
        """
        :param aquarium: Aquarium
        """
        self.aquarium = aquarium
        self.filter = AquariumFilter(aquarium)

    def play(self):
        count_snails = len(self.filter.get_snails())
        count_predators = len(self.filter.get_predators())

        while len(self.aquarium.occupants) > (count_snails + count_predators):
            occupant1 = choice(self.aquarium.occupants)
            occupant2 = choice(self.aquarium.occupants)

            try:
                occupant1.eat(occupant2)
                index = self.aquarium.occupants.index(occupant2)
                del self.aquarium.occupants[index]
            except FoodError as e:
                print(e.message)

        print(" =RESULT= ")
        self.print_result(self.filter.get_snails())
        self.print_result(self.filter.get_predators())

    @staticmethod
    def print_result(occupants):
        occupants = sorted(occupants, key=lambda occupant: occupant.weight, reverse=True)

        for occupant in occupants:
            print(occupant.__class__.__name__ + " \"" + occupant.name + "\", weight: " + str(occupant.weight) + ", victims: " + str(occupant.victims))

if __name__ == '__main__':
    aquarium = Aquarium()

    print(BColors.BOLD, "Occupants in aquarium:", len(aquarium.occupants), BColors.ENDC)

    app = Application(aquarium)
    app.play()

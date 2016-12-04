#!/usr/bin/env python3

from random import choice
from utils import BColors
from aquarium import Aquarium, AquariumFilter


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
            if occupant1.eat(occupant2):
                index = self.aquarium.occupants.index(occupant2)
                del self.aquarium.occupants[index]

        print(" =RESULT= ")
        self.print_result()

    def print_result(self):
        pass

if __name__ == '__main__':
    aquarium = Aquarium()

    print(BColors.BOLD, "Occupants in aquarium:", len(aquarium.occupants), BColors.ENDC)

    app = Application(aquarium)
    app.play()

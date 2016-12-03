#!/usr/bin/env python3

from random import choice
from utils import BColors
from aquarium import Aquarium

class Application():
    def __init__(self, aquarium):
        self.aquarium = aquarium

    def play(self):
        while (len(self.aquarium.fishes) > 2):
            # Хищники едят случайных рыб до тех пор пока не съедят всех
            # а не случайные рыбы едят случайных рыб
            fish1 = choice(self.aquarium.fishes)
            fish2 = choice(self.aquarium.fishes)
            if (fish1.eat(fish2)):
                index = self.aquarium.fishes.index(fish2)
                del self.aquarium.fishes[index]

        print(" =RESULT OF CHASE= ")
        self.print_result()

    def print_result(self):
        winner = max(self.aquarium.fishes, key=lambda item: item.weight)
        looser = min(self.aquarium.fishes, key=lambda item: item.weight)

        print(BColors.OKGREEN, 'Winner fish name:', winner.name, ', his weight:', winner.weight, ', victims: ' + str(winner.count_victims), BColors.ENDC)
        print(BColors.FAIL, 'Looser fish name:', looser.name, ', his weight:', looser.weight, ', victims: ' + str(looser.count_victims), BColors.ENDC)

if __name__ == '__main__':
    aquarium = Aquarium()

    print(BColors.BOLD, "Fishes in aquarium:", len(aquarium.fishes), BColors.ENDC)

    app = Application(aquarium)
    app.play()

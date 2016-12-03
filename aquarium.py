from occupants import Predator, Herbivores, Snail, Alga
from random import randint
from utils import Names


class Aquarium:
    def __init__(self):
        self.fishes = FishCreator.get_fishes('fish')
        self.fishes += FishCreator.get_fishes('alga')
        self.fishes += FishCreator.get_fishes('snail')
        self.fishes += FishCreator.get_fishes('predator')


class FishCreator:
    PREDATOR_TYPE = 'predator'
    ALGA_TYPE = 'alga'
    SNAIL_TYPE = 'snail'

    @classmethod
    def get_fishes(cls, fish_type):
        """
        Fish factory
        :param fish_type: string
        :return: list[Fish]
        """
        if fish_type == cls.PREDATOR_TYPE:
            return cls.generate_predators()
        elif fish_type == cls.ALGA_TYPE:
            return cls.generate_algas()
        elif fish_type == cls.SNAIL_TYPE:
            return cls.generate_snails()
        else:
            return cls.generate_herbivores()

    @staticmethod
    def generate_algas():
        pass

    @staticmethod
    def generate_snails():
        pass

    @staticmethod
    def generate_herbivores():
        count_fishes = randint(10, 50)
        fishes = []

        for i in range(count_fishes):
            fish = Herbivores(Names.generate_name(), randint(1, 9))
            fishes.append(fish)

        return fishes

    @staticmethod
    def generate_predators():
        predators = []

        for i in range(2):
            predator = Predator(Names.generate_name(), 10)
            predators.append(predator)

        return predators

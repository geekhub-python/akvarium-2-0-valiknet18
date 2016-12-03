from fish import Fish, Predator
from random import randint
from utils import Names


class Aquarium():
    def __init__(self):
        self.fishes = FishCreator.get_fishes('fish') + FishCreator.get_fishes('predator')


class FishCreator():
    PREDATOR_TYPE = 'predator'

    @classmethod
    def get_fishes(cls, fish_type):
        """
        Fish factory
        :param fish_type: string
        :return: list[Fish]
        """
        if fish_type == cls.PREDATOR_TYPE:
            return cls.generate_predators()
        else:
            return cls.generate_normal_fishes()

    @staticmethod
    def generate_normal_fishes():
        count_fishes = randint(10, 50)
        fishes = []

        for i in range(count_fishes):
            fish = Fish(Names.generate_name(), randint(1, 9))
            fishes.append(fish)

        return fishes

    @staticmethod
    def generate_predators():
        predators = []

        for i in range(2):
            predator = Predator(Names.generate_name(), 10)
            predators.append(predator)

        return predators

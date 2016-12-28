from occupants import Predator, Herbivores, Snail, Seaweed
from random import randint
from utils import Names


class Aquarium:
    def __init__(self):
        self.occupants = FishCreator.get_occupants('fish')
        self.occupants += FishCreator.get_occupants('seaweed')
        self.occupants += FishCreator.get_occupants('snail')
        self.occupants += FishCreator.get_occupants('predator')


class FishCreator:
    PREDATOR_TYPE = 'predator'
    SEAWEED_TYPE = 'seaweed'
    SNAIL_TYPE = 'snail'
    HERBIVORES_TYPE = 'herbivores'

    MAX_SEAWEED_COUNT = 45
    MAX_SNAILS_COUNT = 3
    MAX_HERBIVORES_COUNT = 50
    MAX_PREDATORS_COUNT = 2

    @classmethod
    def get_occupants(cls, fish_type):
        """
        Fish factory
        :param fish_type: string
        :return: list[Fish]
        """
        if fish_type == cls.PREDATOR_TYPE:
            return cls.generate_predators()
        elif fish_type == cls.SEAWEED_TYPE:
            return cls.generate_seaweeds()
        elif fish_type == cls.SNAIL_TYPE:
            return cls.generate_snails()
        else:
            return cls.generate_herbivores()

    @classmethod
    def generate_seaweeds(cls):
        count_seaweeds = randint(7, cls.MAX_SEAWEED_COUNT)
        algas = []

        for i in range(count_seaweeds):
            alga = Seaweed(Names.generate_name(), randint(1, Seaweed.MAX_WEIGHT))
            algas.append(alga)

        return algas

    @classmethod
    def generate_snails(cls):
        count_snails = randint(1, cls.MAX_SNAILS_COUNT)
        snails = []

        for i in range(count_snails):
            snail = Snail(Names.generate_name(), randint(1, Snail.MAX_WEIGHT))
            snails.append(snail)

        return snails

    @classmethod
    def generate_herbivores(cls):
        count_fishes = randint(10, cls.MAX_HERBIVORES_COUNT)
        fishes = []

        for i in range(count_fishes):
            fish = Herbivores(Names.generate_name(), randint(1, Herbivores.MAX_WEIGHT))
            fishes.append(fish)

        return fishes

    @classmethod
    def generate_predators(cls):
        predators = []

        for i in range(cls.MAX_PREDATORS_COUNT):
            predator = Predator(Names.generate_name(), Predator.DEFAULT_PREDATOR_WEIGHT)
            predators.append(predator)

        return predators


class AquariumFilter:
    def __init__(self, aquarium):
        """

        :param aquarium: Aquarium
        :return:
        """
        self.aquarium = aquarium

    def filter_by_class_name(self, class_name):
        return [occupant for occupant in self.aquarium.occupants if isinstance(occupant, class_name)]

    def get_predators(self):
        return self.filter_by_class_name(Predator)

    def get_snails(self):
        return self.filter_by_class_name(Snail)

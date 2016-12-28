import unittest
import occupants
from random import choice
from aquarium import Aquarium, AquariumFilter, FishCreator


class TestAquarium(unittest.TestCase):
    OCCUPANTS_MAX_COUNT = 200
    OCCUPANTS_MIN_COUNT = 20

    def setUp(self):
        self.aquarium = Aquarium()

    def test_occupants_length(self):
        self.assertGreater(self.OCCUPANTS_MAX_COUNT, len(self.aquarium.occupants))
        self.assertLess(self.OCCUPANTS_MIN_COUNT, len(self.aquarium.occupants))


class TestFishCreator(unittest.TestCase):
    def test_create_predators(self):
        predators = FishCreator.get_occupants(FishCreator.PREDATOR_TYPE)

        self.assertGreaterEqual(FishCreator.MAX_PREDATORS_COUNT, len(predators))
        self.assertIsInstance(choice(predators), occupants.Predator)

    def test_create_seaweed(self):
        seaweeds = FishCreator.get_occupants(FishCreator.SEAWEED_TYPE)

        self.assertGreaterEqual(FishCreator.MAX_SEAWEED_COUNT, len(seaweeds))
        self.assertIsInstance(choice(seaweeds), occupants.Seaweed)

    def test_create_herbivores(self):
        herbivores = FishCreator.get_occupants(FishCreator.HERBIVORES_TYPE)

        self.assertGreaterEqual(FishCreator.MAX_HERBIVORES_COUNT, len(herbivores))
        self.assertIsInstance(choice(herbivores), occupants.Herbivores)

    def test_create_snail(self):
        snails = FishCreator.get_occupants(FishCreator.SNAIL_TYPE)

        self.assertGreaterEqual(FishCreator.MAX_SNAILS_COUNT, len(snails))
        self.assertIsInstance(choice(snails), occupants.Snail)


class TestAquariumFilter(unittest.TestCase):
    def setUp(self):
        self.aquarium = Aquarium()
        self.aquarium_filter = AquariumFilter(self.aquarium)

    def test_is_predator(self):
        predators = self.aquarium_filter.get_predators()

        self.assertLess(0, len(predators))
        self.assertIsInstance(choice(predators), occupants.Predator)

    def test_is_snail(self):
        snails = self.aquarium_filter.get_snails()

        self.assertLess(0, len(snails))
        self.assertIsInstance(choice(snails), occupants.Snail)

    def test_is_seaweed(self):
        seaweeds = self.aquarium_filter.filter_by_class_name(occupants.Seaweed)

        self.assertLess(0, len(seaweeds))
        self.assertIsInstance(choice(seaweeds), occupants.Seaweed)

    def test_is_herbivores(self):
        herbivores = self.aquarium_filter.filter_by_class_name(occupants.Herbivores)

        self.assertLess(0, len(herbivores))
        self.assertIsInstance(choice(herbivores), occupants.Herbivores)

if __name__ == '__main__':
    unittest.main()
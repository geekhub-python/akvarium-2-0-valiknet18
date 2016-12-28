import unittest
import occupants
from exception import FoodError


class TestOccupant(unittest.TestCase):
    def setUp(self):
        self.seaweed = occupants.Seaweed('Seaweed', occupants.Seaweed.MAX_WEIGHT)
        self.herbivores = occupants.Herbivores('Herbivores', occupants.Herbivores.MAX_WEIGHT)
        self.snail = occupants.Snail('Snail', occupants.Snail.MAX_WEIGHT)
        self.predator = occupants.Predator('Predator', occupants.Predator.DEFAULT_PREDATOR_WEIGHT)


class TestSeaweed(TestOccupant):
    def test_eat(self):
        with self.assertRaises(FoodError):
            self.seaweed.eat(self.herbivores)

        with self.assertRaises(FoodError):
            self.seaweed.eat(self.seaweed)

        with self.assertRaises(FoodError):
            self.seaweed.eat(self.snail)

        with self.assertRaises(FoodError):
            self.seaweed.eat(self.predator)


class TestHerbivores(TestOccupant):
    def test_eat(self):
        self.assertEqual(True, self.herbivores.eat(self.seaweed))

        with self.assertRaises(FoodError):
            self.herbivores.eat(self.snail)

        with self.assertRaises(FoodError):
            self.herbivores.eat(self.predator)

        with self.assertRaises(FoodError):
            self.herbivores.eat(self.herbivores)


class TestPredator(TestOccupant):
    def test_eat(self):
        self.assertEqual(True, self.predator.eat(self.herbivores))

        with self.assertRaises(FoodError):
            self.predator.eat(self.snail)

        with self.assertRaises(FoodError):
            self.predator.eat(self.seaweed)

        with self.assertRaises(FoodError):
            self.predator.eat(self.predator)


class TestSnail(TestOccupant):
    def test_eat(self):
        self.assertEqual(True, self.snail.eat(self.seaweed))

        with self.assertRaises(FoodError):
            self.snail.eat(self.snail)

        with self.assertRaises(FoodError):
            self.snail.eat(self.herbivores)

        with self.assertRaises(FoodError):
            self.snail.eat(self.predator)

if __name__ == '__main__':
    unittest.main()
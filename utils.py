from random import choice
from functools import wraps


def food(*args):
    def food_factory(func):
        @wraps(func)
        def wrapper(self, fish):
            result = type(fish) in args

            return func(self, fish, result)
        return wrapper
    return food_factory


class Names:
    NAMES = [
        'Sushi',
        'Bubbles',
        'Casper',
        'Sunny',
        'Shadow',
        'Comet',
        'flash',
        'McLovin',
        'Pile O\' Skulls',
        'Pumpkin',
        'Spot',
        'Ariel',
        'Blue',
        'Boo',
        'Charlie',
        'Crimsin',
        'Crimson',
        'fish',
        'Freckles',
        'Goldie',
        'Johnston',
        'Nemo',
        'Spike',
        'Yuki',
        'Ace',
        'Ai Kuai',
        'Air Marshall',
        'Ajax',
        'Alstin-Bae Jr',
        'An Kai',
        'Anarchy',
        'Andro Sostar',
        'Aphrodite',
        'Asa',
        'Azhdeha',
        'azzuri',
        'Babel',
        'Babies',
        'Baby Finley',
        'Baby guppies'
    ]

    @classmethod
    def generate_name(cls):
        return choice(cls.NAMES)


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

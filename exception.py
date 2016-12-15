from utils import BColors


class FoodError(Exception):
    def __init__(self, message):
        self.message = BColors.FAIL + message + BColors.ENDC

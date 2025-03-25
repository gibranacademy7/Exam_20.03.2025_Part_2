import random

class NumberArray:
    def __init__(self, size):
        self._numbers = [random.randint(1, 100) for _ in range(size)]
        self._average = None
        self._std_deviation = None

    @property
    def numbers(self):
        return self._numbers

    @property
    def average(self):
        return self._average

    @property
    def std_deviation(self):
        return self._std_deviation

    @numbers.setter
    def numbers(self, new_numbers):
        self._numbers = new_numbers

    @average.setter
    def average(self, value):
        self._average = value

    @std_deviation.setter
    def std_deviation(self, value):
        self._std_deviation = value

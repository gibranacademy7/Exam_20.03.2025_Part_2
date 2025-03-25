from enum import Enum

class CardSuit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __eq__(self, other):
        if not isinstance(other, CardSuit):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value
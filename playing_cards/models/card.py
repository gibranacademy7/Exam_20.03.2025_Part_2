from enums.card_suit import CardSuit
from enums.card_rank import CardRank

class Card:
    def __init__(self, suit: CardSuit, rank: CardRank, face_up=True):
        self._suit = suit
        self._rank = rank
        self._face_up = face_up

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    @property
    def face_up(self):
        return self._face_up

    def flip(self):
        self._face_up = not self._face_up
        return self._face_up

    def get_display_name(self):
        return f"{self._rank.name.capitalize()} of {self._suit.name.capitalize()}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return (self.rank, self.suit) < (other.rank, other.suit)

    def __gt__(self, other):
        return (self.rank, self.suit) > (other.rank, other.suit)

    def __hash__(self):
        return hash((self.rank, self.suit))

    def __str__(self):
        return "?" if not self.face_up else self.get_display_name()

    def __repr__(self):
        return f"Card({self.suit}, {self.rank}, face_up={self.face_up})"
import random
from models.card import Card
from enums.card_suit import CardSuit
from enums.card_rank import CardRank
from utils.decorators import fair_deck

class Deck:
    def __init__(self, shuffle=True):
        self._cards = [Card(suit, rank) for suit in CardSuit for rank in CardRank]
        self._index = 0
        if shuffle:
            self.shuffle()

    @property
    def cards(self):
        return list(self._cards)

    @fair_deck
    def shuffle(self):
        random.shuffle(self._cards)
        return self._cards[:]

    def draw(self):
        return self._cards.pop(0) if self._cards else None

    def add_card(self, card):
        if isinstance(card, Card):
            self._cards.append(card)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._cards):
            raise StopIteration
        card = self._cards[self._index]
        self._index += 1
        return card
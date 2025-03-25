import random
from exceptions.deck_cheating_error import DeckCheatingError

def fair_deck(func):
    def wrapper(*args, **kwargs):
        result1 = func(*args, **kwargs)
        result2 = func(*args, **kwargs)
        if result1 == result2:
            raise DeckCheatingError("Deck shuffle produced the same order twice!")
        return result1
    return wrapper
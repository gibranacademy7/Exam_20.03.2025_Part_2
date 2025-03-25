"""
................... Project Structure:

playing_cards/
│── __init__.py
│── main.py
│── enums/
│   ├── __init__.py
│   ├── card_suit.py
│   ├── card_rank.py
│── models/
│   ├── __init__.py
│   ├── card.py
│   ├── deck.py
│── utils/
│   ├── __init__.py
│   ├── decorators.py
│── exceptions/
│   ├── __init__.py
│   ├── deck_cheating_error.py
==========================================
==========================================

..................Code Structure Diagram

+----------------------------+
|        CardSuit (Enum)     |
|----------------------------|
| HEARTS = 3                |
| DIAMONDS = 2              |
| CLUBS = 1                 |
| SPADES = 4                |
|----------------------------|
| __eq__(other)             |
| __lt__(other)             |
| __gt__(other)             |
+----------------------------+

+----------------------------+
|        CardRank (Enum)     |
|----------------------------|
| TWO = 2   → ACE = 14       |
|----------------------------|
| __eq__(other)             |
| __lt__(other)             |
| __gt__(other)             |
+----------------------------+

+----------------------------+
|         Card Class         |
|----------------------------|
| _suit (CardSuit)          |
| _rank (CardRank)          |
| _face_up (bool)           |
|----------------------------|
| suit (property)           |
| rank (property)           |
| face_up (property)        |
| flip()                    |
| get_display_name()        |
|----------------------------|
| __eq__(other)             |
| __lt__(other)             |
| __gt__(other)             |
| __hash__()                |
| __str__()                 |
| __repr__()                |
+----------------------------+

+----------------------------+
|         Deck Class         |
|----------------------------|
| _cards (list[Card])       |
| _index (int)              |
|----------------------------|
| cards (property)          |
| shuffle()                 |
| draw()                    |
| add_card(card)            |
|----------------------------|
| __len__()                 |
| __getitem__(index)        |
| __iter__()                |
| __next__()                |
+----------------------------+

+----------------------------+
|    DeckCheatingError       |
|----------------------------|
| Custom exception class    |
+----------------------------+

+----------------------------+
|        fair_deck           |
|----------------------------|
| Decorator to enforce      |
| fair deck shuffling       |
+----------------------------+

+----------------------------+
|          main.py           |
|----------------------------|
| Initializes deck           |
| Demonstrates operations    |
+----------------------------+

"""
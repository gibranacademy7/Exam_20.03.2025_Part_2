from enums.card_suit import CardSuit
from enums.card_rank import CardRank
from models.card import Card
from models.deck import Deck
from exceptions.deck_cheating_error import DeckCheatingError

def main():
    try:
        # Create and shuffle deck
        deck = Deck()
        deck.shuffle()

        # Draw a few cards
        card1 = deck.draw()
        card2 = deck.draw()
        print(f"Drawn Cards: {card1}, {card2}")

        # Compare cards
        if card1 > card2:
            print(f"{card1} is greater than {card2}")
        elif card1 < card2:
            print(f"{card1} is less than {card2}")
        else:
            print(f"{card1} is equal to {card2}")

        # Iterate over the deck
        print("Remaining cards in deck:")
        for card in deck:
            print(card)
    except DeckCheatingError as e:
        print(f"Deck cheating detected: {e}")

if __name__ == "__main__":
    main()
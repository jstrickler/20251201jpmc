import random
from card import Card

CardList = list[Card]

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._cards: CardList = []
        self._make_deck()

    def _make_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def draw(self) -> Card:
        return self._cards.pop()
    
    def shuffle(self) -> None:
        random.shuffle(self._cards)

    @property
    def cards(self) -> CardList:
        return self._cards

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(d1, d2)
    print(f"{d1 = }")
    d1.shuffle()
    print(d1.cards)   # NOT d1._cards
    for _ in range(5):
        print(d1.draw())
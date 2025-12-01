from card import Card
from carddeck import CardDeck

class Game:
    pass

class JokerDeck(Game, CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            joker = Card(f"Joker-{joker_number}", "*** JOKER ***")
            self._cards.append(joker)

if __name__ == '__main__':
    j = JokerDeck()
    j.shuffle()
    print(j)
    print(j.cards)
    print(JokerDeck.mro())  # method resolution order

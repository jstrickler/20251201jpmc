"""
Provide Card class for use in decks of cards

Usage:
    c = Card('rank', 'suit')
"""
class Card:  # inherits from 'object'
    """
    One playing card
    """
    def __init__(self, rank: str, suit: str):  #  'self' ==> 'this' in Java/C++/C#
        self._rank: str = rank
        self._suit: str = suit

    @property  # attribute management
    def rank(self): # getter property
        """
        Rank (ordering value) of card
        """
        return self._rank
    
    @rank.setter
    def rank(self, value: str):  # setter property
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError(f"Rank must be str, not {type(value).__name__}")

    @property  # attribute management
    def suit(self): # getter property
        """
        Suit of the card
        """
        return self._suit
    
    @suit.setter
    def suit(self, value):  # setter property
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError(f"Suit must be str, not {type(value).__name__}")

    def __str__(self): # implements str(obj)  e.g. print(obj)
        return f"Card:{self.rank}/{self.suit}"

    def __repr__(self):  # implements repr(obj)  e.g. f"{obj = }"
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == '__main__':
    c1 = Card('8', 'Diamonds')
    print(c1)  #  print(str(c1))
    print(c1.rank, c1.suit)
    # c1.rank = 123

    c1.rank = 'K'
    c1.suit = "Hearts"
    print(c1.rank)

    print(c1)
    print(f"c1 = {c1}")
    print(f"{c1 = }")
    print(repr(c1))

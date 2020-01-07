from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

class IndoDeck:

    ranks = [str(x) for x in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position): # Possible indexing, slicing, and iteration
        return self._cards[position]

    def __repr__(self):
        print(self.ranks)
        print(self.suits)
        return self._cards

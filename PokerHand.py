"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        """ Builds a histogram of the ranks that appear in the hand.
            Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self, num=1):
        """ Returns True if the hand has n pairs, False otherwise.

            num: number of pairs, typically takes value 1 or 2.
        """
        self.rank_hist()
        i = 0
        for val in self.ranks.values():
            if val == 2:
                i += 1
        if i == num:
            return True
        else:
            return False

    def has_three_of_a_kind(self):
        self.rank_hist()
        i = 0
        for val in self.ranks.values():
            if val == 3:
                i += 1
        if i == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 5)
        hand.sort()
        print(hand)
        print("Has flush:", hand.has_flush())
        print("Has a pair:", hand.has_pair())
        print("Has two pairs:", hand.has_pair(num=2))
        print('')


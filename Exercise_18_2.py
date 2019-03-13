import random


class Card:
    """Represents a standard playing card.
    """

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __str__(self):
        return "{:s} of {:s}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = (self.suit, self.rank)
        t2 = (other.suit, other.rank)
        return t1 < t2


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def shuffle_card(self):
        return random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, n_hands, n_cards):
        list_hands = []
        for i in range(n_hands):
            hand = Hand()
            deck.move_cards(hand, n_cards)
            list_hands.append(hand)
        return list_hands


class Hand(Deck):
    """ Represents a hand of playing cards.
    """

    def __init__(self, label=""):
        self.cards = []
        self.label = label


def print_hands(list_hands):
    i = 1
    for hand in list_hands:
        print('')
        print("Hand {:d} have cards:\n".format(i), hand, sep='')
        i += 1


deck = Deck()
deck.shuffle_card()
print(deck)

hand = Hand("new hand")
deck.move_cards(hand, num=5)
print("New hand have cards:\n", hand, sep='')

print_hands(deck.deal_hands(4, 5))

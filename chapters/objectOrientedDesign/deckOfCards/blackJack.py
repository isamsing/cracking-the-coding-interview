"""
Deck of Cards: Design the data structures for a generic deck of cards.
Explain how you would subclass the data structures to implement blackjack.
"""

"""
Card
Deck
Suit
Hand
"""

from .deck import Deck
from .hand import Hand


class BlackJack:

    def __init__(self, totalHandsOnTable: int, deck: Deck):
        self.totalHandsOnTable = totalHandsOnTable
        self.hands = list()
        self.deck = deck

    def play(self):
        for hands in range(self.totalHandsOnTable):
            cards = list()
            cards.append(self.deck.draw())
            cards.append(self.deck.draw())
            self.hands.append(Hand(cards))

        while self.hands:
            hand = self.hands.pop()
            input("")

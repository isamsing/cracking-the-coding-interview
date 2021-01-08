from typing import List

from .card import Card


class Hand:
    SEPARATOR_SYMBOL = " | "

    def __init__(self, cards: List[Card]):
        self.cards = cards

    def add(self, card):
        self.cards.append(card)

    def show(self):
        for card in self.cards:
            print(card, end=self.SEPARATOR_SYMBOL)

from enum import Enum


class Suit(Enum):
    DIAMOND = 0
    SPADE = 1
    CLUB = 2
    HEART = 3


class Card:
    def __init__(self, faceValue: int, suit: Suit):
        self.faceValue = faceValue
        self.suit = suit

    def __str__(self):
        return "{}:{}".format(self.suit, self.faceValue)
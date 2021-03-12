from enum import Enum
from typing import Optional


class Suit(Enum):
    DIAMOND = 0
    SPADE = 1
    CLUB = 2
    HEART = 3


class Card:
    def __init__(self, faceValue: Optional[int], suit: Suit):
        self.faceValue = faceValue
        self.suit = suit

    def __str__(self):
        return "{}:{}".format(self.suit, self.faceValue)


class King(Card):
    FACE_VALUE = 13

    def __init__(self, suit: Suit):
        super(King, self).__init__(self.FACE_VALUE, suit)


class Queen(Card):
    FACE_VALUE = 12

    def __init__(self, suit: Suit):
        super(Queen, self).__init__(self.FACE_VALUE, suit)


class Jack(Card):
    FACE_VALUE = 11

    def __init__(self, suit: Suit):
        super(Jack, self).__init__(self.FACE_VALUE, suit)

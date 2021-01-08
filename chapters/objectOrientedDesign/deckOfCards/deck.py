from .card import Card, Suit


class Deck:
    MAX_FACE_VALUE = 14
    SUITS = [Suit.DIAMOND, Suit.CLUB, Suit.HEART, Suit.SPADE]

    def __build(self) -> None:
        self.cards = list()
        for faceValue in range(self.MAX_FACE_VALUE):
            for suit in self.SUITS:
                self.cards.append(Card(faceValue, suit))

    def __init__(self):
        self.__build()

    def draw(self):
        return self.cards.pop()

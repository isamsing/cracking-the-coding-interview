from unittest import TestCase
from chapters.linkedLists.sumLinkedLists import sumLinkedLists
from chapters.linkedLists.link import Link
from typing import List


class Test(TestCase):

    @staticmethod
    def linkedListToArray(marker: Link) -> List:
        arr = []
        while marker is not None:
            arr.append(marker.info)
            marker = marker.nextLink
        return arr

    def testBaseSumLinkedLists(self):
        firstNumberDigitOne = Link(7)
        firstNumberDigitSecond = Link(1)
        firstNumberDigitThree = Link(6)

        firstNumberDigitOne.nextLink = firstNumberDigitSecond
        firstNumberDigitSecond.nextLink = firstNumberDigitThree

        secondNumberDigitOne = Link(5)
        secondNumberDigitSecond = Link(9)
        secondNumberDigitThree = Link(2)

        secondNumberDigitOne.nextLink = secondNumberDigitSecond
        secondNumberDigitSecond.nextLink = secondNumberDigitThree

        self.assertEqual(self.linkedListToArray(sumLinkedLists(firstNumberDigitOne, secondNumberDigitOne)), [9, 1, 2])

    def testSumLinkedListWithLargeDigit(self):
        firstNumberDigitOne = Link(7)
        firstNumberDigitSecond = Link(1)
        firstNumberDigitThree = Link(1)
        firstNumberDigitFour = Link(6)
        firstNumberDigitFive = Link(6)
        firstNumberDigitSix = Link(6)

        firstNumberDigitOne.nextLink = firstNumberDigitSecond
        firstNumberDigitSecond.nextLink = firstNumberDigitThree
        firstNumberDigitThree.nextLink = firstNumberDigitFour
        firstNumberDigitFour.nextLink = firstNumberDigitFive
        firstNumberDigitFive.nextLink = firstNumberDigitSix

        secondNumberDigitOne = Link(5)
        secondNumberDigitSecond = Link(9)
        secondNumberDigitThree = Link(2)

        secondNumberDigitOne.nextLink = secondNumberDigitSecond
        secondNumberDigitSecond.nextLink = secondNumberDigitThree

        self.assertEqual(self.linkedListToArray(sumLinkedLists(firstNumberDigitOne, secondNumberDigitOne)),
                         [6, 6, 6, 4, 1, 2])

    def testSumLinkedListWithNoneValue(self):
        secondNumberDigitOne = Link(5)
        secondNumberDigitSecond = Link(9)
        secondNumberDigitThree = Link(2)

        secondNumberDigitOne.nextLink = secondNumberDigitSecond
        secondNumberDigitSecond.nextLink = secondNumberDigitThree

        self.assertEqual(self.linkedListToArray(sumLinkedLists(None, None)), [])

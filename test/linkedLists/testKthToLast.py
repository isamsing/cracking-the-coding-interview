from unittest import TestCase

from chapters.linkedLists.kthToLast import kthToLast
from chapters.linkedLists.link import Link


class Test(TestCase):
    def testKthToLast(self):
        testHead = Link(3)
        firstLink = Link(5)
        secondLink = Link(10)
        thirdLink = Link(11)
        fourthLink = Link(23)
        fifthLink = Link(1)
        sixthLink = Link(42)
        seventhLink = Link(9)

        testHead.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink
        fourthLink.nextLink = fifthLink
        fifthLink.nextLink = sixthLink
        sixthLink.nextLink = seventhLink

        expectedResult = kthToLast(testHead, 3)
        self.assertEqual(expectedResult, fifthLink)

    def testKthToLastWithSingleLink(self):
        testHead = Link(3)
        expectedResult = kthToLast(testHead, 3)
        self.assertEqual(expectedResult, testHead)

    def testKthToLastWithZeroIndex(self):
        testHead = Link(3)
        firstLink = Link(5)
        testHead.nextLink = firstLink
        expectedResult = kthToLast(testHead, 0)
        self.assertEqual(expectedResult, None)

    def testKthToLastWithTwoLinks(self):
        testHead = Link(3)
        firstLink = Link(5)
        testHead.nextLink = firstLink
        expectedResult = kthToLast(testHead, 1)
        self.assertEqual(expectedResult, firstLink)

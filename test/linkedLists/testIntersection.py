from unittest import TestCase
from chapters.linkedLists.link import Link
from chapters.linkedLists.intersection import intersection


class Test(TestCase):
    def testIntersectionWithValidCase(self):
        testHeadOne = Link(3)
        firstLink = Link(5)
        secondLink = Link(10)
        thirdLink = Link(11)
        fourthLink = Link(23)
        fifthLink = Link(1)
        sixthLink = Link(42)
        seventhLink = Link(9)

        testHeadOne.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink
        fourthLink.nextLink = fifthLink
        fifthLink.nextLink = sixthLink
        sixthLink.nextLink = seventhLink

        testHeadTwo = Link(2)
        testHeadTwo.nextLink = thirdLink

        self.assertTrue(intersection(testHeadOne, testHeadTwo))

    def testIntersectionWithInvalidCase(self):
        testHeadOne = Link(3)
        firstLink = Link(5)
        secondLink = Link(10)
        thirdLink = Link(11)
        fourthLink = Link(23)
        fifthLink = Link(1)
        sixthLink = Link(42)
        seventhLink = Link(9)

        testHeadOne.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink
        fourthLink.nextLink = fifthLink
        fifthLink.nextLink = sixthLink
        sixthLink.nextLink = seventhLink

        testHeadTwo = Link(3)
        firstLinkTwo = Link(3)
        testHeadTwo.nextLink = firstLinkTwo

        self.assertFalse(intersection(testHeadOne, testHeadTwo))

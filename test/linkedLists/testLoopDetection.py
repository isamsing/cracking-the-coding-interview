from unittest import TestCase

from chapters.linkedLists.link import Link
from chapters.linkedLists.loopDetection import loopDetection


class Test(TestCase):
    def testLoopDetectionWithValidCase(self):
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
        seventhLink.nextLink = testHead

        self.assertEqual(loopDetection(testHead), testHead)

    def testLoopDetectionWithInvalidCase(self):
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

        self.assertEqual(loopDetection(testHead), testHead)

from typing import List
from unittest import TestCase

from chapters.linkedLists.link import Link
from chapters.linkedLists.removeDuplicates import removeDuplicatedInUnSortedList, removeDuplicatesInSortedList


class Test(TestCase):

    @staticmethod
    def linkedListToArray(marker: Link) -> List:
        arr = []
        while marker is not None:
            arr.append(marker.info)
            marker = marker.nextLink
        return arr

    def testRemoveDuplicatedInUnsortedListWithSingleLink(self):
        testHead = Link(2)
        expectedHead = removeDuplicatedInUnSortedList(testHead)
        self.assertEqual(self.linkedListToArray(expectedHead), [2])

    def testRemoveDuplicatedInUnsortedListWithTwoDuplicateLinks(self):
        testHead = Link(2)
        firstLink = Link(2)
        testHead.nextLink = firstLink

        expectedHead = removeDuplicatedInUnSortedList(testHead)
        self.assertEqual(self.linkedListToArray(expectedHead), [2])

    def testRemoveDuplicatedInSortedListWithSingleLink(self):
        testHead = Link(2)
        expectedHead = removeDuplicatesInSortedList(testHead)
        self.assertEqual(self.linkedListToArray(expectedHead), [2])

    def testRemoveDuplicatedInSortedListWithTwoDuplicateLinks(self):
        testHead = Link(2)
        firstLink = Link(2)
        testHead.nextLink = firstLink

        expectedHead = removeDuplicatesInSortedList(testHead)
        self.assertEqual(self.linkedListToArray(expectedHead), [2])

    def testRemoveDuplicatesInUnsortedList(self):
        testHead = Link(2)
        firstLink = Link(2)
        secondLink = Link(3)
        thirdLink = Link(2)
        fourthLink = Link(3)
        fifthLink = Link(3)
        sixthLink = Link(2)
        seventhLink = Link(1)

        testHead.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink
        fourthLink.nextLink = fifthLink
        fifthLink.nextLink = sixthLink
        sixthLink.nextLink = seventhLink

        expectedHead = removeDuplicatedInUnSortedList(testHead)
        self.assertEqual(self.linkedListToArray(expectedHead), [1, 2, 3])

    def testRemoveDuplicatesInSortedList(self):
        testHead = Link(1)
        firstLink = Link(2)
        secondLink = Link(2)
        thirdLink = Link(2)
        fourthLink = Link(3)
        fifthLink = Link(3)
        sixthLink = Link(4)
        seventhLink = Link(4)

        testHead.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink
        fourthLink.nextLink = fifthLink
        fifthLink.nextLink = sixthLink
        sixthLink.nextLink = seventhLink

        expectedHead = removeDuplicatesInSortedList(testHead)
        self.assertEqual(self.linkedListToArray(expectedHead), [1, 2, 3, 4])

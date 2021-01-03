from typing import List
from unittest import TestCase

from chapters.linkedLists.link import Link
from chapters.linkedLists.partition import partition


class Test(TestCase):
    @staticmethod
    def linkedListToArray(marker: Link) -> List:
        arr = []
        while marker is not None:
            arr.append(marker.info)
            marker = marker.nextLink
        return arr

    def testPartition(self):
        testHead = Link(3)
        firstLink = Link(5)
        secondLink = Link(8)
        thirdLink = Link(5)
        fourthLink = Link(10)
        fifthLink = Link(2)
        sixthLink = Link(1)

        testHead.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink
        fourthLink.nextLink = fifthLink
        fifthLink.nextLink = sixthLink

        expectedHead = partition(testHead, 5)

        self.assertEqual(self.linkedListToArray(expectedHead), [1, 2, 3, 5, 8, 5, 10])

    def testPartitionWithNone(self):
        self.assertEqual(partition(None, 5), None)

    def testPartitionWithSingleNode(self):
        testHead = Link(5)
        expectedHead = partition(testHead, 5)
        self.assertEqual(self.linkedListToArray(expectedHead), [5])

    def testPartitionWithDoubleNode(self):
        testHead = Link(10)
        firstLink = Link(4)

        testHead.nextLink = firstLink

        expectedHead = partition(testHead, 5)
        self.assertEqual([4, 10], self.linkedListToArray(expectedHead))

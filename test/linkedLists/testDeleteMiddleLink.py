from typing import List
from unittest import TestCase

from chapters.linkedLists.deleteMiddleLink import deleteMiddleNode
from chapters.linkedLists.link import Link


class Test(TestCase):

    @staticmethod
    def linkedListToArray(marker: Link) -> List:
        arr = []
        while marker is not None:
            arr.append(marker.info)
            marker = marker.nextLink
        return arr

    def testDeleteMiddleLink(self):
        testHead = Link(2)
        firstLink = Link(4)
        secondLink = Link(5)
        thirdLink = Link(7)
        fourthLink = Link(9)

        testHead.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink

        deleteMiddleNode(secondLink)
        self.assertEqual([2, 4, 7, 9], self.linkedListToArray(testHead))

    def testDeleteMiddleWithSingleLink(self):
        testHead = Link(2)
        firstLink = Link(4)

        testHead.nextLink = firstLink

        deleteMiddleNode(firstLink)
        self.assertEqual([2, 4], self.linkedListToArray(testHead))

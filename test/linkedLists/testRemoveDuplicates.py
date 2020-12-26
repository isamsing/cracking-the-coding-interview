from unittest import TestCase

from chapters.linkedLists.link import Link
from chapters.linkedLists.removeDuplicates import printLinkedList, removeDuplicatesInSortedList, removeDuplicatedInUnSortedList


class Test(TestCase):
    def testRemoveDuplicates(self):
        testHead = Link(1)
        firstLink = Link(2)
        secondLink = Link(2)
        thirdLink = Link(2)
        fourthLink = Link(3)
        fifthLink = Link(3)
        sixthLink = Link(1)
        seventhLink = Link(1)

        testHead.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink
        fourthLink.nextLink = fifthLink
        fifthLink.nextLink = sixthLink
        sixthLink.nextLink = seventhLink

        printLinkedList(testHead)
        printLinkedList(removeDuplicatedInUnSortedList(testHead))

"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is,617 + 295. Output: 2 -> 1 -> 9.That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is,617 + 295. Output: 9 -> 1 -> 2.That is, 912.
"""
from chapters.linkedLists.link import Link


def sumLinkedLists(linkedListOneHead: Link, linkedListTwoHead: Link) -> Link:
    markerListOne = linkedListOneHead
    markerListTwo = linkedListTwoHead

    resultMarker = None

    carry = 0
    while markerListTwo is not None or markerListTwo is not None:
        addedSum = (markerListOne.info + markerListTwo.info + carry)
        carry, resultMarker = getCarry(addedSum, resultMarker)

        markerListOne = markerListOne.nextLink
        markerListTwo = markerListTwo.nextLink

    if markerListOne is not None:
        while markerListOne is not None:
            addedSum = (markerListOne.info + carry)
            carry, resultMarker = getCarry(addedSum, resultMarker)
            markerListOne = markerListOne.nextLink

    if markerListTwo is not None:
        while markerListTwo is not None:
            addedSum = (markerListOne.info + carry)
            carry, resultMarker = getCarry(addedSum, resultMarker)
            markerListTwo = markerListTwo.nextLink

    if carry > 0:
        carryLink = Link(carry)
        resultMarker.nextLink = carryLink

    return resultMarker


def getCarry(addedSum: int, resultMarker: Link) -> (int, Link):
    carry = addedSum // 10
    addedValue = addedSum % 10
    if resultMarker is None:
        resultMarker = Link(addedValue)
    else:
        newLink = Link(addedValue)
        newLink.nextLink = resultMarker
        resultMarker = newLink
    return carry, resultMarker

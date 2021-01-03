"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x
come before all nodes greater than or equal to x. lf x is contained within the list, the values of
x only need to be after the elements less than x (see below).The partition element x can appear
anywhere in the "right partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 ->10 -> 2 -> 1 [partition=5)
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from chapters.linkedLists.link import Link


def partition(head: Link, target: int) -> Link:
    leftMarker = rightMarker = None
    currentMarker = head
    while currentMarker is not None:
        nextMarker = currentMarker.nextLink
        currentMarker.nextLink = None

        if currentMarker.info < target:
            if leftMarker is None:
                leftMarker = rightMarker = currentMarker
            else:
                currentMarker.nextLink = leftMarker
                leftMarker = currentMarker
        else:
            if rightMarker is None:
                leftMarker = rightMarker = currentMarker
            else:
                rightMarker.nextLink = currentMarker
                rightMarker = currentMarker

        currentMarker = nextMarker

    return leftMarker

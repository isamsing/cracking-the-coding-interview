"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""

from chapters.linkedLists.link import Link


def getLastLink(head: Link) -> Link:
    marker = head
    while marker.nextLink is not None:
        marker = marker.nextLink
    return marker


def intersection(headOne: Link, headTwo: Link) -> bool:
    lastOne = getLastLink(headOne)
    lastTwo = getLastLink(headTwo)
    return True if lastOne == lastTwo else False

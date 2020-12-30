"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""

from .link import Link


def kthToLast(head: Link, kth: int) -> Link:
    nthMarker = head
    kthMarker = head
    while nthMarker is not None:
        if kth > 0:
            kth -= 1
        else:
            kthMarker = kthMarker.nextLink
        nthMarker = nthMarker.nextLink
    return kthMarker

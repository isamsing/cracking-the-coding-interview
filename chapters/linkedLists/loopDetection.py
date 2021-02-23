"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
"""

from chapters.linkedLists.link import Link


def loopDetection(head: Link):
    slowMarker = fastMarker = head

    while fastMarker is not None and fastMarker.nextLink is not None:
        slowMarker = slowMarker.nextLink
        fastMarker = fastMarker.nextLink.nextLink
        if slowMarker == fastMarker:
            return fastMarker

    return head

"""
Remove Duplicates: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
from .link import Link


def printLinkedList(head: Link) -> None:
    currentLink = head
    while currentLink.nextLink is not None:
        print(currentLink.info, end=" -> ")
        currentLink = currentLink.nextLink
    print(currentLink.info)


def removeDuplicatesInSortedList(head: Link) -> Link:
    currentLink = head
    while currentLink.nextLink is not None:
        if currentLink.info == currentLink.nextLink.info:
            currentLink.nextLink = currentLink.nextLink.nextLink
        else:
            currentLink = currentLink.nextLink
    return head


# def removeDuplicatedInUnSortedList(head: Link) -> Link:
#     distinctElements = set()
#     marker = head
#     while marker is not None:
#         distinctElements.add(marker.info)
#         marker = marker.nextLink
#
#     newHead = None
#     currentMarker = newHead
#     for element in distinctElements:
#         newLink = Link(element)
#         if currentMarker:
#             currentMarker.nextLink = newLink
#             currentMarker = newLink
#         else:
#             newHead = currentMarker = newLink
#
#     return newHead

def removeDuplicatedInUnSortedList(head: Link) -> Link:
    referenceMarker = head
    while referenceMarker is not None:
        currentMarker = referenceMarker
        while currentMarker.nextLink is not None:
            if currentMarker.nextLink.info == referenceMarker.info:
                currentMarker.nextLink = currentMarker.nextLink.nextLink
            else:
                currentMarker = currentMarker.nextLink
        referenceMarker = referenceMarker.nextLink
    return head

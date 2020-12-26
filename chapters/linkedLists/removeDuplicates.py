"""
Remove Duplicates: Write code to remove duplicates from an unsorted linked list. FOLLOW UP
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


def removeDuplicatedInUnSortedList(head: Link) -> Link:
    referenceMarker = head
    while referenceMarker is not None:
        previousMarker = referenceMarker
        nextMarker = referenceMarker.nextLink

        while previousMarker.nextLink is not None:
            if referenceMarker.info == previousMarker.nextLink.info:
                previousMarker.nextLink = previousMarker.nextLink.nextLink
            previousMarker = previousMarker.nextLink

        referenceMarker = referenceMarker.nextLink
    return head

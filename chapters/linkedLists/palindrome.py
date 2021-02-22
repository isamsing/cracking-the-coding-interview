"""
Palindrome: Implement a function to check if a linked list is a palindrome.

"""
from chapters.linkedLists.link import Link


def palindrome(head: Link) -> bool:
    characterLookup = {}
    marker = head
    while marker is not None:
        character = marker.info
        if character not in characterLookup:
            characterLookup[character] = False
        else:
            characterLookup[character] = True
        marker = marker.nextLink

    return False if list(characterLookup.values()).count(False) > 1 else True

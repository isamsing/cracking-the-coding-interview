"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""


def checkPermutation(source: str, target: str) -> bool:
    sortedSource = sorted(source)
    sorterTarget = sorted(target)
    return True if sortedSource == sorterTarget else False


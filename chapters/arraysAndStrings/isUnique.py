"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
Time Complexity: O(n)
Space Complexity: O(n)
"""


def isUnique(string: str) -> bool:
    uniqueSet = set(string)
    return False if len(uniqueSet) != len(string) else True

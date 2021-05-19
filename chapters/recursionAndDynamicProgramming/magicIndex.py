"""
Magic Index: A magic index in an array A[e... n-1] is defined to be an index such
that A[i] = i. Given a sorted array of distinct integers, write a method to find
a magic index, if one exists, in array A.

FOLLOW UP
What if the values are not distinct?
"""
from typing import Optional, List


def findMagicIndex(elements: List, firstIndex: int, lastIndex: int) -> Optional[int]:
    if firstIndex >= lastIndex:
        return None
    else:
        middleIndex = (firstIndex + lastIndex) // 2
        if elements[middleIndex] == middleIndex:
            return middleIndex
        elif elements[middleIndex] > middleIndex:
            return findMagicIndex(elements, firstIndex, middleIndex)
        else:
            return findMagicIndex(elements, middleIndex, lastIndex)


if __name__ == '__main__':
    testArray = [-1, 0, 1, 2, 4, 10]
    print(findMagicIndex(testArray, 0, len(testArray)))

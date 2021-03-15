"""
You are given an array which is sorted but has been rotated at a point. For example, if a sorted array has the following
elements: 1, 2, 3, 4, 5 then under rotation at position 3 it will become 4, 5, 1, 2, 3. Now, given a similar rotated
array with no prior knowledge of its point of rotation, your job is to return the index of a target element in this array.

Problem Understanding (4 min)

Example 1:
Input: [5, 6, 7, 8, 9, 10, 1, 2, 3] and target = 8
Output: 3

Example 2:
Input: [5, 6, 7, 8, 9, 10, 1, 2, 3] and target = 19
Output: -1

Example 3:
Input: [0, 1, 2, -2, -1] and target = -2
Output: 3
"""
from typing import List


def linearRotationIndexSearch(rotatedList: List) -> int:
    for index in range(len(rotatedList) - 1):
        if rotatedList[index] > rotatedList[index + 1]:
            return index + 1
    return 0


def binaryRotationIndexSearch(rotatedList: List) -> int:
    firstIndex = 0
    lastIndex = len(rotatedList) - 1
    lastElement = rotatedList[lastIndex]

    while firstIndex < lastIndex:
        middleIndex = (lastIndex + firstIndex) // 2
        if rotatedList[middleIndex] < rotatedList[middleIndex + 1]:
            if rotatedList[middleIndex] > lastElement:
                firstIndex = middleIndex
            else:
                lastIndex = middleIndex
        else:
            return middleIndex + 1
    return 0


def binarySearch(sortedList: List, firstIndex: int, lastIndex: int, target: int) -> int:
    while firstIndex < lastIndex:
        middleIndex = (lastIndex + firstIndex) // 2
        if sortedList[middleIndex] == target:
            return middleIndex
        elif sortedList[middleIndex] < target:
            firstIndex = middleIndex
        else:
            lastIndex = middleIndex
    return -1


def searchRotatedList(inputList: List, target: int, binary: bool = True) -> int:
    rotationIndex = binaryRotationIndexSearch(inputList) if binary else linearRotationIndexSearch(inputList)
    if inputList[rotationIndex] <= target <= inputList[-1]:
        return binarySearch(inputList, rotationIndex, len(inputList), target)
    elif inputList[0] <= target <= inputList[rotationIndex - 1]:
        return binarySearch(inputList, 0, rotationIndex, target)
    else:
        return -1


if __name__ == '__main__':
    # testListOne = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    # print(searchRotatedList(testListOne, 8))
    #
    # testListTwo = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    # print(searchRotatedList(testListTwo, 19))
    #
    # testListThree = [0, 1, 2, -2, -1]
    # print(searchRotatedList(testListThree,  -2))
    #
    # testListFour = [0, 1, 2, 3, 4]
    # print(searchRotatedList(testListFour,  2))

    print(searchRotatedList([2, 1], 2))

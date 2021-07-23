"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""
from typing import List


def sortedMerge(smallList: List, largeList: List):
    sortedList = []

    firstIndex = 0
    secondIndex = 0

    while firstIndex < len(smallList) and secondIndex < len(largeList):
        if smallList[firstIndex] <= largeList[secondIndex]:
            sortedList.append(smallList[firstIndex])
            firstIndex += 1
        else:
            sortedList.append(largeList[secondIndex])
            secondIndex += 1

    if firstIndex < len(smallList):
        sortedList += smallList[firstIndex:]
    elif secondIndex < len(largeList):
        sortedList += largeList[secondIndex:]

    return sortedList + largeList[secondIndex:]


if __name__ == '__main__':
    firstList = [4, 6, 7]
    secondList = [1, 2, 3, 5, 8, 9, 10]
    print(sortedMerge(secondList, firstList))

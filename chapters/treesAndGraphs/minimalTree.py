"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
"""
from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf
from typing import List, Optional
from math import floor


def minimalTree(sortedList: List) -> Optional[BinaryLeaf]:
    if len(sortedList) == 1:
        return BinaryLeaf(sortedList[0])
    elif not sortedList:
        return None
    else:
        middleIndex = floor(len(sortedList) / 2)
        root = BinaryLeaf(sortedList[middleIndex])
        root.leftChild = minimalTree(sortedList[:middleIndex])
        root.rightChild = minimalTree(sortedList[middleIndex + 1:])
        return root




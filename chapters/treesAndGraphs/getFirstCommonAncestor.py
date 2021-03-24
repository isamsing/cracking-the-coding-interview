"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""

from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf
from typing import List, Optional


def getPathToLeaf(root: BinaryLeaf, targetLeaf: BinaryLeaf) -> Optional[List]:
    if not root:
        return None
    elif root == targetLeaf:
        return []
    else:
        leftPath = getPathToLeaf(root.leftChild, targetLeaf)
        rightPath = getPathToLeaf(root.rightChild, targetLeaf)

        if leftPath is not None:
            return leftPath + [root.info]
        elif rightPath is not None:
            return rightPath + [root.info]
        else:
            return leftPath or rightPath


def getFirstCommonAncestor(root: BinaryLeaf, firstLeaf: BinaryLeaf, secondLeaf: BinaryLeaf) -> BinaryLeaf:
    pathToFirstLeaf = getPathToLeaf(root, firstLeaf)
    pathToSecondLeaf = getPathToLeaf(root, secondLeaf)

    firstCommonAncestor = None
    while pathToFirstLeaf and pathToSecondLeaf:
        firstAncestor = pathToFirstLeaf.pop()
        secondAncestor = pathToSecondLeaf.pop()
        if firstAncestor == secondAncestor:
            firstCommonAncestor = firstAncestor

    return firstCommonAncestor



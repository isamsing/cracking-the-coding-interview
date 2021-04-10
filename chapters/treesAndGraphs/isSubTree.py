"""
Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.

Hints: #4, #7 7, #78, #37, #37
"""
from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf
from typing import List


def getInOrderSequence(root: BinaryLeaf) -> List:
    if root is None:
        return []
    else:
        leftResult = getInOrderSequence(root.leftChild)
        rightResult = getInOrderSequence(root.rightChild)
        return leftResult + [root.info] + rightResult


def inOrderTraversal(root: BinaryLeaf, target: BinaryLeaf):
    if root is None:
        return None
    else:
        leftResult = inOrderTraversal(root.leftChild, target)
        rightResult = inOrderTraversal(root.rightChild, target)

        result = False
        if root.info == target.info:
            result = getInOrderSequence(root) == getInOrderSequence(target)
        return leftResult or result or rightResult


def isSubTree(firstRoot: BinaryLeaf, secondRoot: BinaryLeaf):
    return inOrderTraversal(firstRoot, secondRoot)

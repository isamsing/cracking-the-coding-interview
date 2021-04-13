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
        return ["X"]
    else:
        leftResult = getInOrderSequence(root.leftChild)
        rightResult = getInOrderSequence(root.rightChild)
        return leftResult + [root.info] + rightResult


def inSubTreeHelper(root: BinaryLeaf, target: BinaryLeaf):
    if root is None:
        return False
    else:
        leftResult = inSubTreeHelper(root.leftChild, target)
        rightResult = inSubTreeHelper(root.rightChild, target)
        return leftResult or (getInOrderSequence(root) == getInOrderSequence(target)) or rightResult


def getPreOrderString(root: BinaryLeaf):
    if root is None:
        return "X"
    else:
        leftString = getPreOrderString(root.leftChild)
        rightString = getPreOrderString(root.rightChild)
        return f"{root.info}{leftString}{rightString}"

def isSubString(firstRoot: BinaryLeaf, secondRoot: BinaryLeaf) -> bool:
    firstString = getPreOrderString(firstRoot)
    secondString = getPreOrderString(secondRoot)
    return secondString in firstString

def isSubTree(firstRoot: BinaryLeaf, secondRoot: BinaryLeaf, method: int = 0):
    functions = {
        0: isSubString,
        1: isSubTree
    }
    return functions[method](firstRoot, secondRoot)

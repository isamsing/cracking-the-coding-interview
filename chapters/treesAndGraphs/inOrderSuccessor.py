"""
Successor: Write an algorithm to find the "next" node (i .e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""

from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf
from typing import Optional

def findSmallestChild(leaf: BinaryLeaf) -> Optional[BinaryLeaf]:
    if leaf.leftChild:
        return findSmallestChild(leaf.leftChild)
    elif leaf.rightChild:
        return findSmallestChild(leaf.rightChild)
    else:
        return leaf

def inOrderSuccessor(leaf: BinaryLeaf) -> Optional[BinaryLeaf]:
    if leaf.rightChild or not leaf.parent:
        return findSmallestChild(leaf.rightChild)
    else:
        return leaf.parent if (leaf.info < leaf.parent.info) else leaf.parent.parent

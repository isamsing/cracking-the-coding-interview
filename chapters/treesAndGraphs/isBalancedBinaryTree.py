"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by
more than one.
"""
from chapters.dataStructures.binaryLeaf import BinaryLeaf


def isBalancedBinaryTree(root: BinaryLeaf):
    def calculateTreeHeight(root: BinaryLeaf, height: int) -> int:
        if not root:
            return height
        else:
            leftChildHeight = calculateTreeHeight(root.leftChild, height + 1)
            rightChildHeight = calculateTreeHeight(root.rightChild, height + 1)
            return leftChildHeight if (leftChildHeight > rightChildHeight) else rightChildHeight

    return abs(calculateTreeHeight(root.leftChild, 0) - calculateTreeHeight(root.rightChild, 0)) <= 1

"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""
from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf


def isBinarySearchTree(root: BinaryLeaf):
    def validateBinarySearchTree(root: BinaryLeaf, minValue, maxValue):
        if not root:
            return False
        else:
            leftChild = validateBinarySearchTree(root.leftChild, minValue, root.info) if root.leftChild else False
            rightChild = validateBinarySearchTree(root.rightChild, root.info, maxValue) if root.rightChild else False
            return leftChild or rightChild or not (minValue < root.info < maxValue)

    MIN_VALUE = float('-inf')
    MAX_VALUE = float('inf')
    return validateBinarySearchTree(root, MIN_VALUE, MAX_VALUE)

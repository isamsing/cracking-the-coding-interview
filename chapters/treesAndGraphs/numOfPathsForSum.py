"""
Paths with Sum: You are given a binary tree in which each node contains an integer value
(which might be positive or negative). Design an algorithm to count the number of paths
that sum to a given value. The path does not need to start or end at the root or a leaf,
but it must go downwards (traveling only from parent nodes to child nodes).
"""
from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf


def getSumOfPathsForNode(leaf: BinaryLeaf, targetSum: int, currentSum: int = 0) -> int:
    if not leaf:
        return 0
    else:
        currentSum += leaf.info
        result = 1 if currentSum == targetSum else 0
        result += getSumOfPathsForNode(leaf.leftChild, targetSum, currentSum)
        result += getSumOfPathsForNode(leaf.rightChild, targetSum, currentSum)
        return result


def getTotalSumOfPaths(leaf: BinaryLeaf, targetSum: int) -> int:
    if not leaf:
        return 0
    else:
        return getSumOfPathsForNode(leaf, targetSum) \
               + getTotalSumOfPaths(leaf.leftChild, targetSum) \
               + getTotalSumOfPaths(leaf.rightChild, targetSum)


if __name__ == '__main__':
    root = BinaryLeaf(5)
    leftChild = BinaryLeaf(3)
    leftLeftChild = BinaryLeaf(-1)
    leftRightChild = BinaryLeaf(7)

    rightChild = BinaryLeaf(0)
    rightLeftChild = BinaryLeaf(2)

    root.leftChild = leftChild
    root.rightChild = rightChild

    leftChild.leftChild = leftLeftChild
    leftChild.rightChild = leftRightChild

    rightChild.leftChild = rightLeftChild

    print(getTotalSumOfPaths(root, 7))

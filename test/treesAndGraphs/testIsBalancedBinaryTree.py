from unittest import TestCase
from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf
from chapters.treesAndGraphs.isBalancedBinaryTree import isBalancedBinaryTree


class Test(TestCase):
    def testImBalancedBinaryTree(self):
        root = BinaryLeaf(5)
        leftChild = BinaryLeaf(3)
        leftLeftChild = BinaryLeaf(1)
        leftRightChild = BinaryLeaf(7)

        root.leftChild = leftChild

        leftChild.leftChild = leftLeftChild
        leftChild.rightChild = leftRightChild

        self.assertFalse(isBalancedBinaryTree(root))

    def testBalancedBinaryTree(self):
        root = BinaryLeaf(5)
        leftChild = BinaryLeaf(3)
        leftLeftChild = BinaryLeaf(1)
        leftRightChild = BinaryLeaf(7)

        rightChild = BinaryLeaf(8)
        rightLeftChild = BinaryLeaf(6)

        root.leftChild = leftChild
        root.rightChild = rightChild

        leftChild.leftChild = leftLeftChild
        leftChild.rightChild = leftRightChild

        rightChild.leftChild = rightLeftChild

        self.assertTrue(isBalancedBinaryTree(root))

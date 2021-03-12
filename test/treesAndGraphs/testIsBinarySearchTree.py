from unittest import TestCase
from chapters.dataStructures.binaryLeaf import BinaryLeaf
from chapters.treesAndGraphs.isBinarySearchTree import isBinarySearchTree


class Test(TestCase):
    def testIsInvalidBinarySearchTree(self):
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

        self.assertTrue(isBinarySearchTree(root))

    def testIsValidBinarySearchTree(self):
        root = BinaryLeaf(5)
        leftChild = BinaryLeaf(3)
        leftLeftChild = BinaryLeaf(1)
        leftRightChild = BinaryLeaf(4)

        rightChild = BinaryLeaf(8)
        rightLeftChild = BinaryLeaf(6)

        root.leftChild = leftChild
        root.rightChild = rightChild

        leftChild.leftChild = leftLeftChild
        leftChild.rightChild = leftRightChild

        rightChild.leftChild = rightLeftChild

        self.assertFalse(isBinarySearchTree(root))

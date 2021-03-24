from unittest import TestCase
from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf
from chapters.treesAndGraphs.getFirstCommonAncestor import getFirstCommonAncestor

class Test(TestCase):
    def testGetFirstCommonAncestor(self):
        root = BinaryLeaf(8)
        leftChild = BinaryLeaf(5)
        leftLeftChild = BinaryLeaf(3)
        leftLeftLeftChild = BinaryLeaf(1)
        leftLeftRightChild = BinaryLeaf(4)
        leftRightChild = BinaryLeaf(7)

        rightChild = BinaryLeaf(12)
        rightLeftChild = BinaryLeaf(10)
        rightRightChild = BinaryLeaf(14)
        rightRightLeftChild = BinaryLeaf(13)

        root.leftChild = leftChild
        root.rightChild = rightChild

        leftChild.leftChild = leftLeftChild
        leftChild.rightChild = leftRightChild
        leftLeftChild.leftChild = leftLeftLeftChild
        leftLeftChild.rightChild = leftLeftRightChild

        rightChild.leftChild = rightLeftChild
        rightChild.rightChild = rightRightChild
        rightRightChild.leftChild = rightRightLeftChild

        self.assertEqual(getFirstCommonAncestor(root, rightLeftChild, rightChild), 8)

from unittest import TestCase

from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf
from chapters.treesAndGraphs.inOrderSuccessor import inOrderSuccessor

class Test(TestCase):
    def testInOrderSuccessorForRootNode(self):
        root = BinaryLeaf(5)
        leftChild = BinaryLeaf(3)
        leftLeftChild = BinaryLeaf(1)
        leftRightChild = BinaryLeaf(4)

        rightChild = BinaryLeaf(8)
        rightLeftChild = BinaryLeaf(6)

        root.leftChild = leftChild
        leftChild.parent = root
        root.rightChild = rightChild
        rightChild.parent = root

        leftChild.leftChild = leftLeftChild
        leftLeftChild.parent = leftChild
        leftChild.rightChild = leftRightChild
        leftRightChild.parent = leftChild

        rightChild.leftChild = rightLeftChild
        rightLeftChild.parent = rightChild

        self.assertEqual(inOrderSuccessor(root).info, 6)

    def testInOrderSuccessorForRightRootNode(self):
        root = BinaryLeaf(5)
        leftChild = BinaryLeaf(3)
        leftLeftChild = BinaryLeaf(1)
        leftRightChild = BinaryLeaf(4)

        rightChild = BinaryLeaf(8)
        rightLeftChild = BinaryLeaf(6)

        root.leftChild = leftChild
        leftChild.parent = root
        root.rightChild = rightChild
        rightChild.parent = root

        leftChild.leftChild = leftLeftChild
        leftLeftChild.parent = leftChild
        leftChild.rightChild = leftRightChild
        leftRightChild.parent = leftChild

        rightChild.leftChild = rightLeftChild
        rightLeftChild.parent = rightChild

        self.assertEqual(inOrderSuccessor(rightChild), None)

    def testInOrderSuccessorForLeftChildNode(self):
        root = BinaryLeaf(5)
        leftChild = BinaryLeaf(3)
        leftLeftChild = BinaryLeaf(1)
        leftRightChild = BinaryLeaf(4)

        rightChild = BinaryLeaf(8)
        rightLeftChild = BinaryLeaf(6)

        root.leftChild = leftChild
        leftChild.parent = root
        root.rightChild = rightChild
        rightChild.parent = root

        leftChild.leftChild = leftLeftChild
        leftLeftChild.parent = leftChild
        leftChild.rightChild = leftRightChild
        leftRightChild.parent = leftChild

        rightChild.leftChild = rightLeftChild
        rightLeftChild.parent = rightChild

        self.assertEqual(inOrderSuccessor(leftChild).info, 4)

    def testInOrderSuccessorForLeftChildLeftChildNode(self):
        root = BinaryLeaf(5)
        leftChild = BinaryLeaf(3)
        leftLeftChild = BinaryLeaf(1)
        leftRightChild = BinaryLeaf(4)

        rightChild = BinaryLeaf(8)
        rightLeftChild = BinaryLeaf(6)

        root.leftChild = leftChild
        leftChild.parent = root
        root.rightChild = rightChild
        rightChild.parent = root

        leftChild.leftChild = leftLeftChild
        leftLeftChild.parent = leftChild
        leftChild.rightChild = leftRightChild
        leftRightChild.parent = leftChild

        rightChild.leftChild = rightLeftChild
        rightLeftChild.parent = rightChild

        self.assertEqual(inOrderSuccessor(leftRightChild).info, 5)

    def testInOrderSuccessorForLeftNode(self):
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
        leftChild.parent = root
        root.rightChild = rightChild
        rightChild.parent = root

        leftChild.leftChild = leftLeftChild
        leftLeftChild.parent = leftChild
        leftChild.rightChild = leftRightChild
        leftRightChild.parent = leftChild
        leftLeftChild.leftChild = leftLeftLeftChild
        leftLeftLeftChild.parent = leftLeftChild
        leftLeftChild.rightChild = leftLeftRightChild
        leftLeftRightChild.parent = leftLeftChild

        rightChild.leftChild = rightLeftChild
        rightLeftChild.parent = rightChild
        rightChild.rightChild = rightRightChild
        rightRightChild.parent = rightChild
        rightRightChild.leftChild = rightRightLeftChild
        rightRightLeftChild.parent = rightRightChild

        self.assertEqual(inOrderSuccessor(leftLeftChild).info, 4)


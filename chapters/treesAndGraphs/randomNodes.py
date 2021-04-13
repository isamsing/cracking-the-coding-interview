"""
Random Node: You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
Hints: #42, #54, #62, #75, #89, #99, #7 72, #7 79
"""
from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf
from random import randint
from typing import Optional


class BinaryTree:
    leaves = []

    def __init__(self, info):
        self.leaves.append(info)

    def getRandomNode(self) -> BinaryLeaf:
        return self.leaves[randint(0, len(self.leaves))]

    def insert(self, info) -> None:
        self.leaves.append(info)

    def findHelper(self, index, info):
        if index >= len(self.leaves):
            return None
        else:
            leftResult = self.findHelper(2 * index + 1, info)
            rightResult = self.findHelper(2 * index + 2, info)

            result = index if self.leaves[index] == info else None
            return leftResult or result or rightResult

    def find(self, info) -> Optional[int]:
        return self.findHelper(0, info)

    def shiftLeft(self, fromIndex):
        for index in range(fromIndex, len(self.leaves) - 1):
            self.leaves[index] = self.leaves[index + 1]
        self.leaves = self.leaves[:-1]

    def delete(self, info) -> bool:
        infoIndex = self.find(info)
        if infoIndex:
            self.shiftLeft(infoIndex)
            return True
        else:
            return False

"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
(e.g., if you have a tree with depth 0, you'll have 0 linked lists).
"""

from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf
from queue import SimpleQueue


def listOfDepths(root: BinaryLeaf):
    depth = 0
    queue = SimpleQueue()
    queue.put((depth, root))
    # Use linkedList instead of lists
    linkedLists = {}

    while not queue.empty():
        depth, leaf = queue.get()

        if depth not in linkedLists:
            linkedLists[depth] = [leaf.info]
        else:
            linkedLists[depth].append(leaf.info)

        if leaf.leftChild:
            queue.put((depth + 1, leaf.leftChild))
        if leaf.rightChild:
            queue.put((depth + 1, leaf.rightChild))

    return linkedLists


if __name__ == '__main__':
    rootLeaf = BinaryLeaf(10)
    leftChild = BinaryLeaf(5)
    rightChild = BinaryLeaf(15)
    rootLeaf.leftChild = leftChild
    rootLeaf.rightChild = rightChild
    print(listOfDepths(rootLeaf))

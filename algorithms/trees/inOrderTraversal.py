from chapters.dataStructures.trees.binaryLeaf import BinaryLeaf


def inOrderTraversal(leaf: BinaryLeaf):
    if not leaf:
        return None
    else:
        inOrderTraversal(leaf.leftChild)
        print(leaf.info, end=", ")
        inOrderTraversal(leaf.rightChild)

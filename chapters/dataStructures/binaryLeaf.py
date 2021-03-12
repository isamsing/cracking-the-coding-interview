from typing import Any


class BinaryLeaf:

    def __init__(self, info: Any):
        self.info = info
        self.leftChild = None
        self.rightChild = None

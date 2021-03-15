"""
Three in One: Describe how you could use a single array to implement three stacks.
"""
from typing import Any


class ThreeInOneStack:
    MAX_NUMBER_OF_STACKS = 3

    class StackInfo:
        def __init__(self, startIndex: int, endIndex: int):
            self.startIndex = startIndex
            self.top = self.endIndex = endIndex

        def isEmpty(self):
            return True if (self.top != self.startIndex) else False

    def __init__(self, stackSize: int):
        self.storage = [None] * stackSize * self.MAX_NUMBER_OF_STACKS
        self.stackMetas = {}
        self.startIndex = 0
        self.endIndex = stackSize
        for i in range(self.MAX_NUMBER_OF_STACKS):
            self.stackMetas[i] = self.StackInfo(self.startIndex, self.endIndex)
            self.startIndex = self.endIndex
            self.endIndex = self.endIndex + stackSize

    def __str__(self):
        representation = ""
        for key, stackMeta in self.stackMetas.items():
            representation += f"Stack[{key}:({stackMeta.startIndex}:{stackMeta.endIndex})]:"
            representation += "|".join(
                [str(self.storage[i]) for i in range(stackMeta.top, stackMeta.endIndex)])
            representation += "\n"
        return representation

    def push(self, stackNumber: int, item: Any):
        stackMeta = self.stackMetas[stackNumber]
        if stackMeta.isEmpty():
            stackMeta.top -= 1
            self.storage[stackMeta.top] = item
        else:
            raise ValueError(f"Stack[{stackNumber}] is full")

    def pop(self, stackNumber: int) -> Any:
        stackMeta = self.stackMetas[stackNumber]
        if not stackMeta.isEmpty():
            item = self.storage[stackMeta.top]
            self.storage[stackMeta.top] = None
            stackMeta.top += 1
            return item
        else:
            raise ValueError(f"Stack[{stackNumber}] is empty")

    def peek(self, stackNumber: int) -> Any:
        stackMeta = self.stackMetas[stackNumber]
        if not stackMeta.isEmpty():
            return self.storage[stackMeta.top]
        else:
            raise ValueError(f"Stack[{stackNumber}] is empty")

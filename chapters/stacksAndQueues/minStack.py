"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""
from typing import Any


class MinStack:

    def __init__(self):
        self.items = []
        self.minState = []
        self.minItem = None

    def __updateMinItem(self, item: Any):
        if not self.minItem:
            self.minItem = item
        else:
            self.minItem = self.minItem if self.minItem < item else item
        self.minState.append(self.minItem)

    def push(self, item: Any):
        self.__updateMinItem(item)
        self.items.append(item)

    def pop(self):
        self.minState.pop()
        self.minItem = self.minState[-1]
        return self.items.pop()

    def min(self):
        return self.minItem


if __name__ == '__main__':
    stack = MinStack()
    stack.push(3)
    stack.push(4)
    print(stack.min())
    stack.push(2)
    print(stack.min())
    stack.push(4)
    stack.push(1)
    print(stack.min())
    stack.pop()
    print(stack.min())

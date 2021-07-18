"""
Stack of Boxes: You have a stack of n boxes, with widths Wi' heights hi' and depths di.
The boxes cannot be rotated and can only be stacked on top of one another if each box in
the stack is strictly larger than the box above it in width, height, and depth.
Implement a method to compute the height of the tallest possible stack.The height of a
stack is the sum of the heights of each box.

"""
from typing import List


class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def __repr__(self):
        return f"{self.length}:{self.width}:{self.height}"

    def __gt__(self, other):
        return all([
            self.height > other.height,
            self.width > other.width,
            self.length > other.length
        ])


def getMaxStackHeightHelper(boxes: List[Box]):
    if not boxes:
        return 0
    elif len(boxes) == 1:
        return boxes[0].height
    else:
        maxHeight = 0
        for bottomBox in boxes:
            biggerBoxes = list(filter(lambda box: box > bottomBox, boxes))
            if biggerBoxes:
                currentHeight = bottomBox.height + getMaxStackHeightHelper(biggerBoxes)
            else:
                currentHeight = bottomBox.height
            maxHeight = max(maxHeight, currentHeight)
        return maxHeight


if __name__ == '__main__':
    b1 = Box(1, 1, 1)
    b2 = Box(2, 2, 2)
    b3 = Box(3, 3, 3)
    boxesOne = [b1, b2, b3]
    print(getMaxStackHeightHelper(boxesOne))

    b4 = Box(1, 1, 1)
    b5 = Box(3, 2, 2)
    b6 = Box(3, 3, 3)
    boxesTwo = [b4, b5, b6]
    print(getMaxStackHeightHelper(boxesTwo))

    b7 = Box(6, 4, 4)
    b8 = Box(7, 5, 5)
    b9 = Box(7, 8, 2)
    boxesThree = [b7, b8, b9]
    print(getMaxStackHeightHelper(boxesThree))

    b10 = Box(5, 5, 5)
    boxesFour = [b10]
    print(getMaxStackHeightHelper(boxesFour))



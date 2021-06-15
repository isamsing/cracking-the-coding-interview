"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (Le., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using stacks.
"""
from typing import List
from queue import LifoQueue


class Disk:
    def __init__(self, size):
        self.size = size


def moveDisk(fromPole: LifoQueue, toPole: LifoQueue):
    toPole.put(fromPole.get())


def towerOfHanoi(numberOfDisks: int, firstPole: LifoQueue, middlePole: LifoQueue, lastPole: LifoQueue):
    if numberOfDisks == 1:
        return
    else:
        towerOfHanoi(numberOfDisks - 1, firstPole, middlePole, lastPole)
        moveDisk(firstPole, lastPole)
        towerOfHanoi(numberOfDisks - 1, firstPole, lastPole, middlePole)


if __name__ == '__main__':
    oneDisk = Disk(1)
    twoDisk = Disk(2)
    threeDisk = Disk(3)

    aPole = LifoQueue()
    aPole.put(oneDisk)
    aPole.put(twoDisk)
    aPole.put(threeDisk)
    bPole = LifoQueue()
    cPole = LifoQueue()
    towerOfHanoi(3, aPole, bPole, cPole)
    print(cPole)

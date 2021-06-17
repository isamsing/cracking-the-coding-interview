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


class Disk:
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return f"{self.size}"


class Pole(List):
    def __init__(self, name):
        super().__init__()
        self.name = name


def towerOfHanoi(numberOfDisks: int, firstPole: Pole, lastPole: Pole, middlePole: Pole):
    if numberOfDisks == 1:
        disk = firstPole.pop()
        lastPole.append(disk)
        print(f"Moved {disk.size} from {firstPole.name} to {lastPole.name}", end="\n")
        print(f"{firstPole}:{lastPole}:{middlePole}", end="\n")
    else:
        towerOfHanoi(numberOfDisks - 1, firstPole, middlePole, lastPole)
        towerOfHanoi(1, firstPole, lastPole, middlePole)
        towerOfHanoi(numberOfDisks - 1, middlePole, lastPole, firstPole)


if __name__ == '__main__':
    oneDisk = Disk(1)
    twoDisk = Disk(2)
    threeDisk = Disk(3)

    aPole = Pole("A")
    aPole.append(threeDisk)
    aPole.append(twoDisk)
    aPole.append(oneDisk)
    bPole = Pole("B")
    cPole = Pole("C")
    towerOfHanoi(3, aPole, bPole, cPole)

from collections import deque


def getTotalTimeToRot(storage):
    maxRow, maxCol = len(storage), len(storage[0])
    freshTomatoesCoordinates, rottenTomatoesCoordinates = getInventory(maxCol, maxRow, storage)
    rottenTomatoesCoordinates.append((-1, -1))
    minimum_cycles = -1
    while rottenTomatoesCoordinates:
        (row, col) = rottenTomatoesCoordinates.popleft()
        if row == -1 and col == -1:
            minimum_cycles += 1
            if rottenTomatoesCoordinates:
                rottenTomatoesCoordinates.append((-1, -1))
        else:
            # Rotting top Side
            if row > 0 and storage[row - 1][col] == 1:
                storage[row - 1][col] = 2
                rottenTomatoesCoordinates.append((row - 1, col))
                freshTomatoesCoordinates.remove((row - 1, col))
            # Rotting bottom Side
            if row < maxRow - 1 and storage[row + 1][col] == 1:
                storage[row + 1][col] = 2
                rottenTomatoesCoordinates.append((row + 1, col))
                freshTomatoesCoordinates.remove((row + 1, col))
            # Rotting Left Side
            if col > 0 and storage[row][col - 1] == 1:
                storage[row][col - 1] = 2
                rottenTomatoesCoordinates.append((row, col - 1))
                freshTomatoesCoordinates.remove((row, col - 1))
            # Rotting Right Side
            if col < maxCol - 1 and storage[row][col + 1] == 1:
                storage[row][col + 1] = 2
                rottenTomatoesCoordinates.append((row, col + 1))
                freshTomatoesCoordinates.remove((row, col + 1))

    return minimum_cycles if not freshTomatoesCoordinates else -1


def getInventory(maxCol, maxRow, storage):
    rottenTomatoesCoordinates = deque()
    freshTomatoesCoordinates = []
    for row in range(maxRow):
        for col in range(maxCol):
            if storage[row][col] == 2:
                rottenTomatoesCoordinates.append((row, col))
            if storage[row][col] == 1:
                freshTomatoesCoordinates.append((row, col))
    return freshTomatoesCoordinates, rottenTomatoesCoordinates


if __name__ == '__main__':
    testStorage = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    print(getTotalTimeToRot(testStorage))
    testStorageTwo = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]
    print(getTotalTimeToRot(testStorageTwo))
    testStorageThree = [
        [0, 2]
    ]
    print(getTotalTimeToRot(testStorageThree))

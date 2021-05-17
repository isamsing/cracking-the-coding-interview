"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such
that the robot cannot step on them. Design an algorithm to find a path for the robot from the top
left to the bottom right.
"""


def findWaysToTravelGrid(rowIndex: int, colIndex: int, memo={}) -> int:
    locationKey = f"{rowIndex}:{colIndex}"
    if locationKey in memo:
        return memo[locationKey]
    elif rowIndex == 0 or colIndex == 0:
        return 0
    elif rowIndex == 1 and colIndex == 1:
        return 1
    else:
        memo[locationKey] = findWaysToTravelGrid(rowIndex - 1, colIndex, memo) \
                            + findWaysToTravelGrid(rowIndex, colIndex - 1, memo)
        return memo[locationKey]


if __name__ == '__main__':
    print(findWaysToTravelGrid(6, 3))

"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, pIe -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""


def isOneEditAway(first: str, second: str) -> bool:
    OFFSET = 1
    first = " " + first
    second = " " + second
    rowLength = len(first)
    columnLength = len(second)

    editTable = [[-1 for i in range(columnLength)] for j in range(rowLength)]

    for index in range(columnLength):
        editTable[0][index] = index

    for index in range(rowLength):
        editTable[index][0] = index

    for rowIndex in range(OFFSET, rowLength):
        for colIndex in range(OFFSET, columnLength):
            if first[rowIndex - OFFSET] == second[colIndex - OFFSET]:
                editTable[rowIndex][colIndex] = editTable[rowIndex - 1][colIndex - 1]
            else:
                editTable[rowIndex][colIndex] = 1 + min(editTable[rowIndex - 1][colIndex],
                                                        editTable[rowIndex - 1][colIndex - 1],
                                                        editTable[rowIndex][colIndex - 1])
    return True if editTable[rowLength - 1][columnLength - 1] == 1 else False

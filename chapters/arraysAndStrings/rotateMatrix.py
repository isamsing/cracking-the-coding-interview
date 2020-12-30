"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List


def printMatrix(matrix: List[List]):
    for row in matrix:
        print(row)


def rotateMatrix(matrix: List[List]) -> List[List]:
    matrixLength = len(matrix)

    for layer in range(matrixLength // 2):
        startIndex = layer
        endIndex = matrixLength - 1 - layer
        for index in range(startIndex, endIndex):
            offset = index - layer

            top = matrix[startIndex][index]
            matrix[startIndex][index] = matrix[endIndex - offset][startIndex]
            matrix[endIndex - offset][startIndex] = matrix[endIndex][endIndex - offset]
            matrix[endIndex][endIndex - offset] = matrix[index][endIndex]
            matrix[index][endIndex] = top

    return matrix


if __name__ == '__main__':
    testMatrix = [
        [1, 2],
        [4, 3]
    ]

    printMatrix(rotateMatrix(testMatrix))

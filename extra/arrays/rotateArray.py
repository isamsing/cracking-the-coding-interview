from typing import List, Any


def rotateArray(A: List[Any], K: int) -> list:
    rotationIndex = K if len(A) >= K else K % len(A)
    return A[-rotationIndex:] + A[:-rotationIndex]


if __name__ == '__main__':
    print(rotateArray(["h", "e", "l", "l", "o"], 2))
    print(rotateArray([1, 2, 3, 4], 4))
    print(rotateArray([], 0))

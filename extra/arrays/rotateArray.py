from typing import List, Any


def rotateArray(arr: List[Any], num: int) -> None:
    for _ in range(num % len(arr)):
        arr = arr[1:] + arr[:1]
    return arr


if __name__ == '__main__':
    print(rotateArray(["h", "e", "l", "l", "o"], 62))

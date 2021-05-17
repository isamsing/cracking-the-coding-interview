from typing import List


def getNonContiguousLongestSubSequence(sequence: List) -> List:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    :param sequence: List
    :return: List
    """
    lookup = [1] * len(sequence)
    backtracking = dict()
    longestSubsequenceLength = 0
    largestIndex = 0
    for j in range(1, len(sequence)):
        currentLongestSubsequenceLength = lookup[j]
        for i in range(j):
            if sequence[i] < sequence[j]:
                if lookup[i] + 1 > currentLongestSubsequenceLength:
                    currentLongestSubsequenceLength = lookup[i] + 1
                    backtracking[j] = i
        lookup[j] = currentLongestSubsequenceLength
        if currentLongestSubsequenceLength > longestSubsequenceLength:
            longestSubsequenceLength = currentLongestSubsequenceLength
            largestIndex = j

    nextIndex = largestIndex
    elements = []
    while nextIndex in backtracking:
        element = sequence[nextIndex]
        elements.append(element)
        nextIndex = backtracking[nextIndex]
    elements.append(sequence[nextIndex])
    return elements[::-1]


if __name__ == '__main__':
    print(getNonContiguousLongestSubSequence([1, 2, 3, 1, 4, 5, 2, 9, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(getNonContiguousLongestSubSequence([5, 2, 10, 3, -1, 6, 8, 9, 3]))

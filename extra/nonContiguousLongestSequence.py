from typing import List


def getNonContiguousLongestSubSequence(sequence: List) -> List:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(n)
    :param sequence: List
    :return: List
    """
    longestSubSequence = []
    for firstIndex in range(len(sequence)):
        currentLongestSubSequence = []

        secondIndex = firstIndex + 1
        thirdIndex = len(sequence)
        while secondIndex < thirdIndex:
            currentLongestSubSequence.append(sequence[firstIndex])
            for fourthIndex in range(secondIndex, len(sequence)):
                if sequence[fourthIndex] >= currentLongestSubSequence[-1]:
                    currentLongestSubSequence.append(sequence[fourthIndex])
            if len(currentLongestSubSequence) > len(longestSubSequence):
                longestSubSequence = currentLongestSubSequence

            currentLongestSubSequence = []
            secondIndex += 1
    return longestSubSequence


if __name__ == '__main__':
    print(getNonContiguousLongestSubSequence([5, 2, 10, 3, -1, 6, 8, 9, 3]))

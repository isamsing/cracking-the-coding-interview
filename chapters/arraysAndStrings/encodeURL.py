"""
URLify: Write a method to replace all spaces in a string with '%20:
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string. (Note: If implementing in Java,
please use a character array so that you can perform this operation in place.)
EXAMPLE
Input: "Mr John Smith " J 13
Output: "Mr%20John%20Smith"

Time Complexity: O(n)
Space Complexity: O(n)
"""


def encodeURL(string: str, encodeSymbol="%20") -> str:
    words = string.strip().split(" ")
    encodedString = ""
    secondLastIndex = len(words) - 1
    lastIndex = -1
    for i in range(secondLastIndex):
        encodedString += words[i] + encodeSymbol
    return encodedString + words[lastIndex]

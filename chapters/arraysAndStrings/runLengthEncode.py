"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than
the original string, your method should return the original string. You can assume the string has only uppercase
and lowercase letters (a - z).

Time Complexity: O(n)
Space Complexity: O(n)
"""


def runLengthEncode(string: str) -> str:
    encodedString = ""
    stringWithOffset = string + " "

    count = 1
    for index in range(len(string)):
        if stringWithOffset[index] == stringWithOffset[index + 1]:
            count += 1
        else:
            encodedString += f"{stringWithOffset[index]}{count}"
            count = 1
    return encodedString

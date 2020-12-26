"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement
of letters.The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)

Time Complexity: O(n)
Space Complexity: O(n)
"""


def isPermutationPalindrome(string: str) -> bool:
    stringWithoutSpaces = string.replace(" ", "")
    characterFlagLookup = {}

    for char in stringWithoutSpaces:
        if char not in characterFlagLookup:
            characterFlagLookup[char] = False
        else:
            characterFlagLookup[char] = True

    return False if list(characterFlagLookup.values()).count(False) > 1 else True


if __name__ == '__main__':
    print(isPermutationPalindrome("racecar"))

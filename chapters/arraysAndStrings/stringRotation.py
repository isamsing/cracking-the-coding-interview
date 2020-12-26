"""
String Rotation: Assume you have amethod isSubstring which checks ifone word is asubstring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
(e.g.,"waterbottle" is a rotation of "erbottlewat").
"""


def isStringRotation(stringOne: str, stringTwo: str) -> bool:
    return stringTwo in stringOne + stringOne

"""
Group Anagrams: Write a method to sort an array of strings so that
all the anagrams are next to each other.
"""

from typing import List


def sortAnagrams(anagrams: List[str]):
    lookup = {}
    for anagram in anagrams:
        sortedAnagram = "".join(sorted(anagram))
        if sortedAnagram in lookup:
            lookup[sortedAnagram].append(anagram)
        else:
            lookup[sortedAnagram] = [anagram]
    result = []
    [result.extend(v) for v in lookup.values()]
    return result


if __name__ == '__main__':
    anagrams = [
        "hello",
        "yellow",
        "loleh",
        "blue",
        "llowye",
        "lube"
    ]
    print(sortAnagrams(anagrams))

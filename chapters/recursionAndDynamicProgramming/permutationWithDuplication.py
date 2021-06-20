"""
Permutations with Dups: Write a method to compute all permutations of a string whose
characters are not necessarily unique. The list of permutations should not have duplicates.
"""


def permutationWithDuplicates(uniqueString: str):
    if len(uniqueString) == 2:
        return [uniqueString, uniqueString[::-1]]
    else:
        first = uniqueString[:1]
        subsequencePermutation = permutationWithDuplicates(uniqueString[1:])
        permutation = set()
        for perm in subsequencePermutation:
            positions = len(perm) + 1
            for position in range(positions):
                temp = perm[:position] + first + perm[position:]
                if temp not in permutation:
                    permutation.add(temp)
        return permutation


if __name__ == '__main__':
    uniqueString = "122"

"""
Permutations with Dups: Write a method to compute all permutations of a string whose
characters are not necessarily unique. The list of permutations should not have duplicates.
"""


def permutationWithDuplicates(stringWithDuplicates: str):
    if len(stringWithDuplicates) == 2:
        return [stringWithDuplicates, stringWithDuplicates[::-1]]
    else:
        first = stringWithDuplicates[:1]
        subsequencePermutation = permutationWithDuplicates(stringWithDuplicates[1:])
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

"""
Permutations without Dups: Write a method to compute all permutations of a string of unique characters.
"""


def permutationWithoutDuplicates(uniqueString: str):
    if len(uniqueString) == 2:
        return [uniqueString, uniqueString[::-1]]
    else:
        first = uniqueString[:1]
        subsequencePermutation = permutationWithoutDuplicates(uniqueString[1:])
        permutation = []
        for perm in subsequencePermutation:
            positions = len(perm) + 1
            for position in range(positions):
                permutation.append(perm[:position] + first + perm[position:])
        return permutation


if __name__ == '__main__':
    uniqueString = "1234"
    print(len(permutationWithoutDuplicates(uniqueString)))

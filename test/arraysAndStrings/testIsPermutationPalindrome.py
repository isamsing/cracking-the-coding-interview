from unittest import TestCase

from chapters.arraysAndStrings.isPermutationPalindrome import isPermutationPalindrome


class Test(TestCase):
    def testWithEmptyString(self):
        self.assertTrue(isPermutationPalindrome(" "))

    def testWithPalindromeString(self):
        self.assertTrue(isPermutationPalindrome("taco cat"))

    def testWithNoPalindromeString(self):
        self.assertFalse(isPermutationPalindrome("asdf"))

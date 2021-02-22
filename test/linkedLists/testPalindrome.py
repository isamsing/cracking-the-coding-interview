from unittest import TestCase

from chapters.linkedLists.link import Link
from chapters.linkedLists.palindrome import palindrome


class Test(TestCase):
    def testPalindromeWithValidCase(self):
        testHead = Link("r")
        firstLink = Link("a")
        secondLink = Link("c")
        thirdLink = Link("e")
        fourthLink = Link("c")
        fifthLink = Link("a")
        sixthLink = Link("r")

        testHead.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink
        fourthLink.nextLink = fifthLink
        fifthLink.nextLink = sixthLink

        self.assertEqual(palindrome(testHead), True)

    def testPalindromeWithInvalidCase(self):
        testHead = Link("r")
        firstLink = Link("a")
        secondLink = Link("c")
        thirdLink = Link("e")
        fourthLink = Link("o")
        fifthLink = Link("a")
        sixthLink = Link("r")

        testHead.nextLink = firstLink
        firstLink.nextLink = secondLink
        secondLink.nextLink = thirdLink
        thirdLink.nextLink = fourthLink
        fourthLink.nextLink = fifthLink
        fifthLink.nextLink = sixthLink

        self.assertEqual(palindrome(testHead), False)

    def testPalindromeWithNone(self):
        self.assertEqual(palindrome(None), True)

    def testPalindromeWithSingleCharacter(self):
        self.assertEqual(palindrome(Link("a")), True)

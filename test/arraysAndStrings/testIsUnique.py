from unittest import TestCase

from chapters.arraysAndStrings.isUnique import isUnique


class Test(TestCase):
    def testEmptyString(self):
        self.assertTrue(isUnique(""))

    def testUniqueString(self):
        self.assertTrue(isUnique("qwerty"))

    def testNotUniqueString(self):
        self.assertFalse(isUnique("racecar"))

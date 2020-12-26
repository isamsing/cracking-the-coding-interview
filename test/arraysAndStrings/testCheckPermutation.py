from unittest import TestCase

from chapters.arraysAndStrings.checkPermutation import checkPermutation


class Test(TestCase):
    def testEmptySource(self):
        self.assertFalse(checkPermutation("", "rraceca"))

    def testEmptyTarget(self):
        self.assertFalse(checkPermutation("racecar", ""))

    def testValidPermutation(self):
        self.assertTrue(checkPermutation("racecar", "rraceca"))

    def testInvalidPermutation(self):
        self.assertFalse(checkPermutation("raceca", "rraceca"))

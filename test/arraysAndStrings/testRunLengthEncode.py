from unittest import TestCase

from chapters.arraysAndStrings.runLengthEncode import runLengthEncode


class Test(TestCase):
    def testWithValidString(self):
        self.assertEqual("a2b1c5a3", runLengthEncode("aabcccccaaa"))

    def testWithEmptyString(self):
        self.assertEqual("", runLengthEncode("  "))

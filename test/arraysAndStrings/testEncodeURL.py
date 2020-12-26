from unittest import TestCase

from chapters.arraysAndStrings.encodeURL import encodeURL


class Test(TestCase):

    def testEncodeValidURL(self):
        expectedOutput = "Mr%20John%20Smith"
        actualOutput = encodeURL("Mr John Smith ")
        self.assertEqual(expectedOutput, actualOutput)

    def testEncodeEmptyURL(self):
        self.assertEqual("", encodeURL(""))

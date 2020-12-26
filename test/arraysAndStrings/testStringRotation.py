from unittest import TestCase

from chapters.arraysAndStrings.stringRotation import isStringRotation


class Test(TestCase):
    def testValidIsStringRotation(self):
        stringOne = "erbottlewat"
        stringTwo = "waterbottle"
        self.assertTrue(isStringRotation(stringOne, stringTwo))

    def testInValidIsStringRotation(self):
        stringOne = "erbottlewat"
        stringTwo = "waterbdsfsottle"
        self.assertFalse(isStringRotation(stringOne, stringTwo))

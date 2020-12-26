from unittest import TestCase

from chapters.arraysAndStrings.isOneEditAway import isOneEditAway


class Test(TestCase):
    def testWithStringsOneEditAway(self):
        self.assertTrue(isOneEditAway("pale", "pae"))

    def testWithStringsMoreThatOneEditAway(self):
        self.assertFalse(isOneEditAway("pales", "papa"))

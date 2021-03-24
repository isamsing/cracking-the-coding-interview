from unittest import TestCase
from chapters.treesAndGraphs.buildOrder import buildOrder

class Test(TestCase):
    def testBuildOrder(self):
        projects = ["a", "b", "c", "d", "e", "f"]
        dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
        self.assertEqual(buildOrder(projects, dependencies), ["e", "f", "b", "a", "d", "c"])

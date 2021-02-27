from unittest import TestCase
from chapters.dataStructures.Node import Node
from chapters.treesAndGraphs.routeBetweenNodes import routeBetweenTwoNodes


class Test(TestCase):
    def testRouteBetweenTwoNodesWithExistingPath(self):
        source = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        target = Node(5)

        source.children = [two, three]
        two.children = [four]
        four.children = [target]

        self.assertTrue(routeBetweenTwoNodes(source, target))

    def testRouteBetweenTwoNodesWithoutExistingPath(self):
        source = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)

        source.children = [two, three]
        two.children = [four]
        four.children = [five]

        self.assertFalse(routeBetweenTwoNodes(source, Node(5)))

    def testRouteBetweenTwoNodesWithSourceNone(self):
        source = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)

        source.children = [two, three]
        two.children = [four]
        four.children = [five]

        self.assertFalse(routeBetweenTwoNodes(None, Node(5)))

"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""
from chapters.dataStructures.Node import Node
from functools import reduce


def routeBetweenTwoNodes(source: Node, target: Node) -> bool:
    if not source or not target or not source.children:
        return False
    elif source == target:
        return True
    else:
        results = []
        for child in source.children:
            results.append(routeBetweenTwoNodes(child, target))
        return reduce(lambda resultOne, resultTwo: resultOne or resultTwo, results)

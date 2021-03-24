from typing import List, Tuple
from queue import SimpleQueue


def kahnTopologicalSort(vertices: List, edges: List[Tuple]) -> List:
    independentVertices = SimpleQueue()
    dependentVertices = list()
    for fromVertex, toVertex in edges:
        dependentVertices.append(toVertex)

    for vertex in vertices:
        if vertex not in dependentVertices:
            independentVertices.put(vertex)

    sortedVertices = []
    while not independentVertices.empty():
        selectedVertex = independentVertices.get()
        sortedVertices.append(selectedVertex)

        selectedVertexEdges = [(fromVertex, toVertex) for (fromVertex, toVertex) in edges if
                               fromVertex == selectedVertex]
        for (fromVertex, toVertex) in selectedVertexEdges:
            edges.remove((fromVertex, toVertex))
            dependentVertices.remove(toVertex)
            if toVertex not in dependentVertices:
                independentVertices.put(toVertex)

    return sortedVertices


def dfs(vertex, edges, ):
    vertexDependents = [toVertex for (fromVertex, toVertex) in edges if fromVertex == vertex]
    if not vertexDependents:
        return vertex
    else:
        path = [vertex]
        for toVertex in vertexDependents:
            path += dfs(toVertex, edges)
        return path


def topologicalSortUsingDFS(vertices: List, edges: List[Tuple]) -> List:
    dependentVertices = list()
    independentVertices = list()
    for fromVertex, toVertex in edges:
        dependentVertices.append(toVertex)

    for vertex in vertices:
        if vertex not in dependentVertices:
            independentVertices.append(vertex)

    sortedVertices = list()
    for vertex in independentVertices:
        sortedVertices += dfs(vertex, edges)

    return sortedVertices



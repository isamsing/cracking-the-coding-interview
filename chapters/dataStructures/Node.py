from __future__ import annotations
from typing import Any


class Node(object):
    def __init__(self, info: Any) -> None:
        self.info = info
        self.children = []

    def __str__(self):
        children = ", ".join([f"{child}" for child in self.children])
        return f"({self.info}):[{children}]"

    def addChild(self, node: Node) -> None:
        self.children.append(node)

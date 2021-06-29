"""
Paint Fill: Implement the "paintFill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
"""
from pprint import pprint
from typing import Optional


class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getNeighbours(self):
        return [Point(self.row, self.col - 1),
                Point(self.row, self.col + 1),
                Point(self.row - 1, self.col),
                Point(self.row + 1, self.col)]


class Canvas:
    def __init__(self, rowLimit, colLimit, background: Optional[int] = -1):
        self.rowLimit = rowLimit
        self.colLimit = colLimit
        self.board = []
        for row in range(self.rowLimit):
            self.board.append([background] * self.colLimit)

    def __str__(self):
        return self.board

    def setColor(self, point: Point, color: int):
        if self.isValidPoint(point):
            self.board[point.row][point.col] = color

    def getColor(self, point: Point):
        if self.isValidPoint(point):
            return self.board[point.row][point.col]
        else:
            return None

    def isValidPoint(self, point: Point):
        return False if point.row < 0 or point.col < 0 or point.row >= self.rowLimit or point.col >= self.colLimit else True

    def fillHelper(self, point: Point, fromColor: int, toColor: int):
        if not self.isValidPoint(point):
            return
        elif self.getColor(point) != fromColor:
            return
        else:
            self.setColor(point, toColor)
            for neighbour in point.getNeighbours():
                if self.getColor(neighbour) == fromColor and self.isValidPoint(neighbour):
                    self.fillHelper(neighbour, fromColor, toColor)
            return

    def fill(self, point: Point, color: int):
        self.fillHelper(point, self.getColor(point), color)


if __name__ == '__main__':
    drawingBoard = Canvas(5, 5)
    drawingBoard.setColor(point=Point(0, 1), color=2)
    drawingBoard.setColor(point=Point(1, 1), color=2)
    drawingBoard.setColor(point=Point(2, 1), color=2)
    drawingBoard.setColor(point=Point(3, 1), color=2)
    drawingBoard.setColor(point=Point(3, 2), color=2)
    drawingBoard.setColor(point=Point(3, 3), color=2)
    drawingBoard.setColor(point=Point(2, 3), color=2)
    drawingBoard.setColor(point=Point(1, 3), color=2)
    drawingBoard.setColor(point=Point(0, 3), color=2)
    pprint(drawingBoard.board)
    drawingBoard.fill(point=Point(0, 0), color=3)
    pprint(drawingBoard.board)

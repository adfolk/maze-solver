# note- this will contain the Point, Line, and Cell classes.
from tkinter import Canvas

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.__a = point_a
        self.__b = point_b

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.__a.x, self.__a.y, self.__b.x, self.__b.y, fill=fill_color, width=2)


from tkinter import Canvas

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self._a = point_a
        self._b = point_b

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self._a.x, self._a.y, self._b.x, self._b.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, x1: int, x2: int, y1: int, y2: int, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._top_left = Point(self._x1, self._y1)
        self._top_right = Point(self._x2, self._y1)
        self._bottom_left = Point(self._x1, self._y2)
        self._bottom_right = Point(self._x2, self._y2)

        self._left_wall = Line(self._top_left, self._bottom_left)
        self._right_wall = Line(self._top_right, self._bottom_right)
        self._top_wall = Line(self._top_left, self._top_right)
        self._bottom_wall = Line(self._bottom_left, self._bottom_right)

        self._win = win
    
    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(self._left_wall, fill_color="black")

        if self.has_right_wall:
            self._win.draw_line(self._right_wall, fill_color="black")

        if self.has_top_wall:
            self._win.draw_line(self._top_wall, fill_color="black")

        if self.has_bottom_wall:
            self._win.draw_line(self._bottom_wall, fill_color="black")


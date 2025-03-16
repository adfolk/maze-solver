from tkinter import BOTTOM, Canvas
from enum import Enum
type CellType = "Cell"

class RelLocNeighbor(Enum):
    TOP = "top"
    DOWN = "bottom"
    LEFT = "left"
    RIGHT = "right"

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

        self.visited = False

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

        if self.has_left_wall == False:
            self._win.draw_line(self._left_wall, fill_color="white")

        if self.has_right_wall:
            self._win.draw_line(self._right_wall, fill_color="black")

        if self.has_right_wall == False:
            self._win.draw_line(self._right_wall, fill_color="white")

        if self.has_top_wall:
            self._win.draw_line(self._top_wall, fill_color="black")

        if self.has_top_wall == False:
            self._win.draw_line(self._top_wall, fill_color="white")

        if self.has_bottom_wall:
            self._win.draw_line(self._bottom_wall, fill_color="black")

        if self.has_bottom_wall == False:
            self._win.draw_line(self._bottom_wall, fill_color="white")

    def draw_move(self, to_cell: CellType, undo=False):
        line_color = "red"
        if undo == True:
            line_color = "white"

        x_start = self._x2 - (abs(self._x2 - self._x1)//2)
        y_start = self._y2 - (abs(self._y2 - self._y1)//2)

        end_x = to_cell._x2 - (abs(to_cell._x2 - to_cell._x1)//2)
        end_y = to_cell._y2 - (abs(to_cell._y2 - to_cell._y1)//2)

        start_pt = Point(x_start, y_start)
        stop_pt = Point(end_x, end_y)

        move_line = Line(start_pt, stop_pt)
        self._win.draw_line(move_line, fill_color=line_color)

    def get_neighbor_type(self, other: CellType):
        if self._y1 == other._y2:
            return RelLocNeighbor.TOP
        if self._y2 == other._y1:
            return RelLocNeighbor.DOWN
        if self._x1 == other._x2:
            return RelLocNeighbor.LEFT
        if self._x2 == other._x1:
            return RelLocNeighbor.RIGHT
    
    def attack_neighbor(self, other: CellType) -> None:
        other_type = self.get_neighbor_type(other)
        match other_type:
            case RelLocNeighbor.TOP:
                self.has_top_wall = False
                self.draw()
                other.has_bottom_wall = False
                other.draw()
            case RelLocNeighbor.DOWN:
                self.has_bottom_wall = False
                self.draw()
                other.has_top_wall = False
                other.draw()
            case RelLocNeighbor.LEFT:
                self.has_left_wall = False
                self.draw()
                other.has_right_wall = False
                other.draw()
            case RelLocNeighbor.RIGHT:
                self.has_right_wall = False
                self.draw()
                other.has_left_wall = False
                other.draw()


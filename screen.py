from tkinter import Tk, BOTH, Canvas
from geometry import Line
BLACK = "black"
RED = "red"

class Window:
    def __init__(self, width: int, height: int):
        self._root = Tk()
        self._root.title("What's in the booooooooox??????")
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._isRunning = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._isRunning = True

        while self._isRunning is True:
            self.redraw()

        print("Window closed...")

    def close(self):
        self._isRunning = False

    def draw_line(self, line: Line, fill_color):
        line.draw(self._canvas, fill_color)


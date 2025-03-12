from tkinter import Tk, BOTH, Canvas
from geometry import Line
BLACK = "black"
RED = "red"

class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("What's in the booooooooox??????")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isRunning = True

        while self.__isRunning is True:
            self.redraw()

        print("Window closed...")

    def close(self):
        self.__isRunning = False

    def draw_line(self, line: Line, fill_color):
        line.draw(self.__canvas, fill_color)


from screen import Window
from geometry import Point, Line, Cell

def main():
    win = Window(800, 600)

    top_left = Cell(x1=150, x2=200, y1=150, y2=200, win=win)
    top_right = Cell(x1=350, x2=400, y1=150, y2=200, win=win)

    bottom_right = Cell(x1=350, x2=400, y1=350, y2=400, win=win)
    bottom_left = Cell(x1=150, x2=200, y1=350, y2=400, win=win)

    top_left.draw()
    bottom_left.draw()
    top_right.draw()
    bottom_right.draw()

    bottom_left.draw_move(top_left, undo=True)
    bottom_right.draw_move(bottom_left, undo=True)
    bottom_right.draw_move(top_right, undo=True)
    top_right.draw_move(top_left, undo=True)
    bottom_right.draw_move(top_left, undo=True)
    bottom_left.draw_move(top_right, undo=True)

    win.wait_for_close()

main()


from screen import Window
from geometry import Point, Line, Cell

def main():
    win = Window(800, 600)
    #pt_a = Point(69, 420)
    #pt_b = Point(420, 69)
    #test_line = Line(pt_a, pt_b)
    #win.draw_line(test_line, "black")

    test_cell = Cell(x1=150, x2=200, y1=150, y2=200, win=win)
    test_cell.has_left_wall = False
    test_cell.has_right_wall = False
    test_cell.has_top_wall = False
    test_cell.has_bottom_wall = False
    test_cell.draw()

    win.wait_for_close()

main()


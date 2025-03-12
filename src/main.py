from window import Window
from geometry import Point, Line

def main():
    win = Window(800, 600)
    pt_a = Point(69, 420)
    pt_b = Point(420, 69)
    test_line = Line(pt_a, pt_b)
    win.draw_line(test_line, "black")
    win.wait_for_close()

main()


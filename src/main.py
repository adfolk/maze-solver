from screen import Window
#from geometry import Point, Line, Cell
from maze import Maze

def main():
    win = Window(800, 600)

    maz = Maze(
            x1=10,
            y1=10,
            num_rows=10,
            num_cols=10,
            x_cell_size=50,
            y_cell_size=50,
            win=win,
    )

    maz._create_cells()
    maz._draw_cells()

    win.wait_for_close()

main()


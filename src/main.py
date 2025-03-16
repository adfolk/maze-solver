from screen import Window
from maze import Maze

def main():
    win = Window(800, 800)

    maz = Maze(
            x1=10,
            y1=10,
            num_rows=10,
            num_cols=10,
            x_cell_size=50,
            y_cell_size=50,
            win=win,
            seed=None,
    )

    maz._draw_cells()
    maz._break_entrance_and_exit()
    maz._break_walls_r(0, 0)
    maz.solve()

    win.wait_for_close()

main()


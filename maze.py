import time
import random as rand
from geometry import Cell, RelLocNeighbor
from screen import Window

type CellRow = list[Cell]
type CellGrid = list[CellRow]
type CellRowCoord = list[int]
type CellGridCoords = list[CellRowCoord]

class Maze:
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            x_cell_size: int,
            y_cell_size: int,
            win: Window,
            seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._x_cell_size = x_cell_size
        self._y_cell_size = y_cell_size
        self._end_cell = None
        self._win = win
        self._cells: CellGrid = []
        if seed is not None:
            seed = rand.seed(seed)
        self._seed = seed

        self._create_cells()

    def _create_cells(self):
        def make_row(self, other: Cell) -> CellRow:
            cell_list = [other]
            for i in range(self._num_cols - 1):
                prev_cell = cell_list[i]
                next_cell = Cell(
                        x1=prev_cell._x2,
                        x2=prev_cell._x2 + self._x_cell_size,
                        y1=prev_cell._y1,
                        y2=prev_cell._y2,
                        win=self._win
                )
                cell_list.append(next_cell)
            return cell_list

        def make_grid(self, col_list: CellRow) -> CellGrid:
            grid = [col_list]
            for i in range(self._num_rows - 1):
                upper = grid[i]
                top_left = upper[0]
                seed_cell = Cell(
                        x1=top_left._x1,
                        x2=top_left._x2,
                        y1=top_left._y2,
                        y2=(top_left._y2 + self._y_cell_size),
                        win=self._win
                )
                next_row = make_row(self, seed_cell)
                grid.append(next_row)
            return grid

        first_cell = Cell(
                x1=self._x1,
                x2=(self._x1 + self._x_cell_size),
                y1=self._y1,
                y2=(self._y1 + self._y_cell_size),
                win=self._win
        )
        first_row = make_row(self, first_cell)
        self._cells = make_grid(self, first_row)
        self._end_cell = self._cells[self._num_rows-1][self._num_cols-1]

    def _animate(self, sleep_time=0.05):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(sleep_time)

    def _draw_cells(self):
        if self._win is None:
            return
        for row in self._cells:
            for cell_inst in row:
                cell_inst.draw()
                self._animate(sleep_time=0)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._animate(sleep_time=0)

        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()
        self._animate(sleep_time=0)


    def _get_neighbors(self, i: int, j: int) -> CellGridCoords:
    # NOTE: pass-through helper function, only to be used by _break_walls_r() below.
        neighbors: CellGridCoords = []
        if i > 0: #NOTE: if there is a row above, always append the top neighbor
            neighbors.append([i-1, j])
        if i < self._num_rows - 1:  #NOTE: if there is a row below, append bottom neighbor
            neighbors.append([i+1, j])
        if j > 0: #NOTE: if left neighbor exists
            neighbors.append([i, j-1])
        if j < self._num_cols - 1: #NOTE: if right neighbor exists
            neighbors.append([i, j+1])
        return neighbors

    def _break_walls_r(self, i: int, j: int) -> None:
        # NOTE: i accesses the CellRow
        # NOTE: j accesses a Cell inside a CellRow
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            unvisited_neighbors: CellGridCoords = []
            all_neighbors: CellGridCoords = self._get_neighbors(i, j)
            for neighbor in all_neighbors:
                if self._cells[neighbor[0]][neighbor[1]].visited == False:
                    unvisited_neighbors.append(neighbor)
            if len(unvisited_neighbors) == 0:
                current_cell.draw()
                return
            ind_rand = rand.randrange(len(unvisited_neighbors))
            vic = unvisited_neighbors[ind_rand]
            target_cell: Cell = self._cells[vic[0]][vic[1]]
            current_cell.attack_neighbor(target_cell)
            self._break_walls_r(vic[0], vic[1])

    def _reset_visited(self) -> None:
        for row in self._cells:
            for each in row:
                each.visited = False

    def solve(self):
        self._reset_visited()
        solutionExists = self._solve_r(0,0)
        return solutionExists
    
    def _solve_r(self, i, j) -> bool:
        self._animate(sleep_time=0.02)
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if current_cell == self._end_cell:
            return True
        neighbors = self._get_neighbors(i, j)
        for pair in neighbors:
            neighbor = self._cells[pair[0]][pair[1]]
            neighbor_type = current_cell.get_neighbor_type(neighbor)
            if neighbor.visited == False:
                path_exists = False
                match neighbor_type:
                    case RelLocNeighbor.TOP:
                        if current_cell.has_top_wall == False and neighbor.has_bottom_wall == False:
                            path_exists = True

                    case RelLocNeighbor.DOWN:
                        if current_cell.has_bottom_wall == False and neighbor.has_top_wall == False:
                            path_exists = True

                    case RelLocNeighbor.LEFT:
                        if current_cell.has_left_wall == False and neighbor.has_right_wall == False:
                            path_exists = True

                    case RelLocNeighbor.RIGHT:
                        if current_cell.has_right_wall == False and neighbor.has_left_wall == False:
                            path_exists = True
                    case _:
                        path_exists = False

                if path_exists == True:
                    current_cell.draw_move(neighbor)
                    next_path = self._solve_r(pair[0], pair[1])
                    if next_path == True:
                        return True
                    else:
                        current_cell.draw_move(neighbor, undo=True)
        return False


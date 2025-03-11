import random
import time
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.seed = random.seed(seed) if seed else seed

        self.cells = []
        self._create_cells()
        if self.window:
            self._break_entrance_and_exit()

    def _create_cells(self):
        for _ in range(self.num_rows):
            row = []
            for _ in range(self.num_cols):
                row.append(Cell(0, 0, 0, 0, self.window))
            self.cells.append(row)

        if self.window:
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell: Cell = self.cells[i][j]
        cell.x0 = self.x1 + j * self.cell_size_x
        cell.y0 = self.y1 + i * self.cell_size_y
        cell.x1 = (self.x1 + j * self.cell_size_x) + self.cell_size_x
        cell.y1 = (self.y1 + i * self.cell_size_y) + self.cell_size_y

        if self.window:
            cell.draw(width=2)
            self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)

        self.cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

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

        if seed:
            random.seed(seed)

        self.cells = []
        self.line_ids = []

    def draw(self):
        if self.line_ids:
            for id in self.line_ids:
                self.window.canvas.delete(id)

        self.cells = []
        self._create_cells()

        if self.window:
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
            self._reset_cells_visited()

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
            cell.draw()
            self._animate()

    def _animate(self, sleep=0.0005):
        self.window.redraw()
        time.sleep(sleep)

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)

        self.cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True

        while True:
            adjacent = self._get_adjacent_cells(i, j)
            possible_directions = self._get_possible_directions(adjacent)
            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return

            chosen_cell = random.choice(possible_directions)
            self._knock_walls_between(chosen_cell, (i, j))

            self._break_walls_r(chosen_cell[0], chosen_cell[1])

    def _reset_cells_visited(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False

    def _get_adjacent_cells(self, i, j):
        if i == 0 and j == 0:
            # bottom and right cells
            return [(i + 1, j), (i, j + 1)]

        if i == len(self.cells) - 1 and j == 0:
            # top and right cells
            return [(i - 1, j), (i, j + 1)]

        if i == len(self.cells) - 1 and j > 0 and j < len(self.cells[0]) - 1:
            # left, bottom and right cells
            return [(i, j - 1), (i - 1, j), (i, j + 1)]

        if i == 0 and j > 0 and j < len(self.cells[0]) - 1:
            # left, top and right cells
            return [(i, j - 1), (i + 1, j), (i, j + 1)]

        if i == 0 and j == len(self.cells[0]) - 1:
            # left and top cells
            return [(i, j - 1), (i + 1, j)]

        if i > 0 and j == 0:
            # bottom, top and right cells
            return [(i - 1, j), (i + 1, j), (i, j + 1)]

        if i > 0 and j > 0 and j < len(self.cells[0]) - 1:
            # left, bottom, top and right cells
            return [(i, j - 1), (i + 1, j), (i, j + 1), (i - 1, j)]

        return [(i, j)]

    def _get_possible_directions(self, cells):
        return list(
            filter(lambda cell: not self.cells[cell[0]][cell[1]].visited, cells)
        )

    def _knock_walls_between(self, cell, other):
        if cell[0] > other[0]:
            self._knock_top_bottom(cell, other)
        elif cell[0] < other[0]:
            self._knock_bottom_top(cell, other)
        elif cell[0] == other[0] and cell[1] < other[1]:
            self._knock_right_left(cell, other)
        elif cell[0] == other[0] and cell[1] > other[1]:
            self._knock_left_right(cell, other)

    def _knock_top_bottom(self, cell, other):
        self.cells[cell[0]][cell[1]].has_top_wall = False
        self._draw_cell(cell[0], cell[1])
        self.cells[other[0]][other[1]].has_bottom_wall = False
        self._draw_cell(other[0], other[1])

    def _knock_bottom_top(self, cell, other):
        self.cells[cell[0]][cell[1]].has_bottom_wall = False
        self._draw_cell(cell[0], cell[1])
        self.cells[other[0]][other[1]].has_top_wall = False
        self._draw_cell(other[0], other[1])

    def _knock_right_left(self, cell, other):
        self.cells[cell[0]][cell[1]].has_right_wall = False
        self._draw_cell(cell[0], cell[1])
        self.cells[other[0]][other[1]].has_left_wall = False
        self._draw_cell(other[0], other[1])

    def _knock_left_right(self, cell, other):
        self.cells[cell[0]][cell[1]].has_left_wall = False
        self._draw_cell(cell[0], cell[1])
        self.cells[other[0]][other[1]].has_right_wall = False
        self._draw_cell(other[0], other[1])

    def solve(self):
        if self.cells:
            return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate(0.015)
        self.cells[i][j].visited = True

        if self.cells[i][j] == self.cells[-1][-1]:
            return True

        adjacent_cells = self._get_adjacent_cells(i, j)
        possible_directions = self._get_possible_directions(adjacent_cells)

        for cell in possible_directions:
            if not self._is_blocking((i, j), cell):
                self.line_ids.append(
                    self.cells[i][j].draw_move(self.cells[cell[0]][cell[1]])
                )
                next_move = self._solve_r(cell[0], cell[1])
                if next_move:
                    return True
                else:
                    self.line_ids.append(
                        self.cells[i][j].draw_move(self.cells[cell[0]][cell[1]], True)
                    )

        return False

    def _is_blocking(self, cell, other):
        if cell[0] == other[0]:
            if cell[1] > other[1]:
                return self.cells[other[0]][other[1]].has_right_wall
            else:
                return self.cells[other[0]][other[1]].has_left_wall
        elif cell[0] > other[0]:
            return self.cells[other[0]][other[1]].has_bottom_wall
        else:
            return self.cells[other[0]][other[1]].has_top_wall

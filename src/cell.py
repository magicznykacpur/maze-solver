from tkinter import Canvas

from window import Window


class Cell:
    def __init__(self, x0: int, y0: int, x1: int, y1: int, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.window = window

        self.visited = False

    def draw(self, fill_color="black", width=1):
        canvas: Canvas = self.window.canvas
        fill_color = "black" if self.has_left_wall else "#d9d9d9"
        canvas.create_line(
            self.x0, self.y0, self.x0, self.y1, fill=fill_color, width=width
        )

        fill_color = "black" if self.has_right_wall else "#d9d9d9"
        canvas.create_line(
            self.x1, self.y0, self.x1, self.y1, fill=fill_color, width=width
        )

        fill_color = "black" if self.has_top_wall else "#d9d9d9"
        canvas.create_line(
            self.x0, self.y0, self.x1, self.y0, fill=fill_color, width=width
        )

        fill_color = "black" if self.has_bottom_wall else "#d9d9d9"
        canvas.create_line(
            self.x0, self.y1, self.x1, self.y1, fill=fill_color, width=width
        )

    def draw_move(self, to_cell, undo=False):
        fill_color = "red" if undo else "gray"

        self_center = (self.x0 + self.x1) / 2, (self.y0 + self.y1) / 2
        to_cell_center = (to_cell.x0 + to_cell.x1) / 2, (to_cell.y0 + to_cell.y1) / 2

        canvas = self.window.canvas
        canvas.create_line(
            self_center[0],
            self_center[1],
            to_cell_center[0],
            to_cell_center[1],
            fill=fill_color,
            width=4,
        )

    def __repr__(self):
        return f"Cell(x0:{self.x0}, y0:{self.y0}, x1:{self.x1}, y1:{self.y1}, left:{self.has_left_wall}, right:{self.has_right_wall}, top:{self.has_top_wall}, bottom:{self.has_bottom_wall})"

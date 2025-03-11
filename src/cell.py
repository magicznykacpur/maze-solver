from tkinter import Canvas

from window import Window


class Cell:
    def __init__(self, x0: int, y0: int, x1: int, y1: int, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.window = window

    def draw(self, fill_color="red"):
        canvas: Canvas = self.window.canvas
        if self.has_left_wall:
            canvas.create_line(self.x0, self.y0, self.x0, self.y1, fill=fill_color)
        if self.has_right_wall:
            canvas.create_line(self.x1, self.y0, self.x1, self.y1, fill=fill_color)
        if self.has_top_wall:
            canvas.create_line(self.x0, self.y0, self.x1, self.y0, fill=fill_color)
        if self.has_bottom_wall:
            canvas.create_line(self.x0, self.y1, self.x1, self.y1, fill=fill_color)

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
            width=4
        )

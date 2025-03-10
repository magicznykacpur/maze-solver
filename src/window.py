from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width=1440, height=900):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.protocol("Maze Solver", self.close)

        self.canvas = Canvas()
        self.canvas.pack()

        self.window_running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.window_running = True

        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False
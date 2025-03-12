from tkinter import Canvas


class Text:
    def __init__(self, x: int, y: int, text: str, size: int, canvas: Canvas):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.canvas = canvas

    def draw(self):
        self.canvas.create_text(
            self.x,
            self.y,
            text=self.text,
            fill="black",
            font=("Times", f"{self.size}", "bold"),
        )

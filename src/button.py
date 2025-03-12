from tkinter import Button as TkButton


class Button:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        callback,
        root,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.callback = callback
        self.root = root

    def draw(self):
        button = TkButton(
            master=self.root,
            text=self.text,
            width=self.width,
            height=self.height,
            command=self.callback,
        )

        button.place(x=self.x, y=self.y)

from window import Window
from line import Line
from point import Point

def main():
    window = Window(800, 600)
    line1 = Line(Point(50, 50), Point(50, 100))
    line2 = Line(Point(100, 50), Point(100, 100))
    window.draw_line(line1, "red")
    window.draw_line(line2, "red")

    window.wait_for_close()

if __name__ == "__main__":
    main()
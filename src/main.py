from cell import Cell
from maze import Maze
from window import Window


def main():
    window = Window(800, 600)
    maze = Maze(200, 100, 4, 7, 50, 50, window, seed=21.37)

    window.wait_for_close()


if __name__ == "__main__":
    main()

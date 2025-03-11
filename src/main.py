from cell import Cell
from maze import Maze
from window import Window


def main():
    window = Window(800, 600)
    print("drawing a maze...")
    maze = Maze(200, 100, 6, 9, 50, 50, window)
    print("maze drawn...")

    print("solving maze...")
    solved = maze.solve()
    print(solved)
    window.wait_for_close()


if __name__ == "__main__":
    main()

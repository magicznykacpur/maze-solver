from time import sleep
from button import Button
from maze import Maze
from window import Window
from text import Text

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


def main():
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

    title = Text(WINDOW_WIDTH / 2, 20, "Maze-Solver", 24, window.canvas)
    title.draw()

    maze = prepare_maze(window)
    prepare_buttons(maze, window)

    window.wait_for_close()

def prepare_buttons(maze: Maze, window: Window):
    draw_maze_button = Button(
        10, 50, 5, 2, "draw", maze.draw, window.root
    )
    draw_maze_button.draw()

    solve_maze_button = Button(
        10, 100, 5, 2, "solve", maze.solve, window.root
    )
    solve_maze_button.draw()
    
    exit_button = Button(10, 150, 5, 2, "exit", window.close, window.root)
    exit_button.draw()


def prepare_maze(window):
    maze_y_pos = 50
    maze_num_rows = 12
    maze_num_cols = 18
    maze_cell_size = 50
    maze_x_pos = (WINDOW_WIDTH / 2) - (maze_num_cols / 2) * maze_cell_size

    return Maze(
        maze_x_pos,
        maze_y_pos,
        maze_num_rows,
        maze_num_cols,
        maze_cell_size,
        maze_cell_size,
        window,
    )


if __name__ == "__main__":
    main()

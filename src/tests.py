import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(
            x1=0,
            y1=0,
            num_rows=num_rows,
            num_cols=num_cols,
            cell_size_x=10,
            cell_size_y=10,
        )
        
        self.assertEqual(len(maze.cells), num_rows)
        self.assertEqual(len(maze.cells[0]), num_cols)
    
    def test_maze_create_cells_small(self):
        num_cols = 6
        num_rows = 4
        maze = Maze(
            x1=0,
            y1=0,
            num_rows=num_rows,
            num_cols=num_cols,
            cell_size_x=10,
            cell_size_y=10,
        )

        self.assertEqual(len(maze.cells), num_rows)
        self.assertEqual(len(maze.cells[0]), num_cols)
    
    def test_maze_create_cells_big(self):
        num_cols = 24
        num_rows = 22
        maze = Maze(
            x1=0,
            y1=0,
            num_rows=num_rows,
            num_cols=num_cols,
            cell_size_x=10,
            cell_size_y=10,
        )

        self.assertEqual(len(maze.cells), num_rows)
        self.assertEqual(len(maze.cells[0]), num_cols)


if __name__ == "__main__":
    unittest.main()

import random

# DO NOT modify any code in this class!

class Maze():
    '''The actual grid of the maze that we are trying to solve.'''
    MINVAL = 0 # default
    MAXVAL = 9 # default
    WALL_CHAR = "*"

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._minval = Maze.MINVAL
        self._maxval = Maze.MAXVAL

    # Testing method - the 2D list representing the maze can be set externally to facilitate testing
    def _set_maze(self, lst):
        self._maze = lst

    def init_random(self, minval=MINVAL, maxval=MAXVAL):
        '''Initialize with random values. Optionally pass the min and max values for point values.'''
        # 2D array:  rows,cols
        self._maze = [[random.randrange(minval, maxval) for i in range(self._cols)] for j in range(self._rows)]
        self._minval = minval
        self._maxval = maxval

    def add_random_walls(self, percent_obstruction):
        '''Insert some random "walls" to make the maze non-trivial. The
        percent_obstruction (float in 0..1) determines the frequency of the walls in the
        maze. The more walls, the less winning paths and the less
        recursion will be needed for the solution. But it also means
        that some mazes will have no possible path from Start to Finish.'''

        threshold = int((self._maxval - self._minval) * percent_obstruction)
        for row in range(self._rows):
            for col in range(self._cols):
                if self._maze[row][col] < threshold:
                    # Add wall to this row,col
                    self._maze[row][col] = self.WALL_CHAR

    def __repr__(self):
        return self._print_maze()
    
    def _print_maze(self, winningpath=list()):
        '''Prints out the grid with values, walls, start and finish squares.
        Optionally pass the winning list/path of tuples if you want the winning route
        to be show as '@' characters.'''
        result = "    "
        for col in range(self._cols):
            # Add the column headers
            result += f" {col} "
        result += "\n"
        for row in range(self._rows):
            result += f"\n{row}   " # Add the row header
            for col in range(self._cols):
                if (row, col) == self._start:
                    result += " S "  # Start square
                elif (row, col) == self._finish:
                    result += " F "  # Finish square
                elif (row, col) in winningpath:
                    result += " @ "  # Square in winning path
                else:
                    result += f" {self._maze[row][col]} "  # Value square
        return result + "\n"

    def is_move_in_maze(self, row, col):
        '''Checks if the potential move is in the maze'''
        return row >= 0 and row < self._rows and col >= 0 and col < self._cols

    def is_wall(self, row, col):
        '''Is the given location a wall'''
        return self._maze[row][col] == self.WALL_CHAR

    def make_move(self, row, col, path):
        '''Make the given move. Add the row,col to the path and
        return the value.'''
        path.append((row,col))
        return self._maze[row][col]

    def set_start_finish(self, start, finish):
        '''Set the start and finish squares in the maze'''
        if not self.is_move_in_maze(start[0], start[1]) or not self.is_move_in_maze(start[0], start[1]):
            raise RuntimeError("Start and Finish must be in the maze")
        if start == finish:
            raise RuntimeError("Start and Finish must be different locations")
        self._start = start
        self._finish = finish
        # Set the start and finish to 0 values
        self._maze[start[0]][start[1]] = 0
        self._maze[finish[0]][finish[1]] = 0

    def get_start(self):
        '''Get the starting square as a tuple'''
        return self._start

    def get_finish(self):
        '''Get the finish square as a tuple'''
        return self._finish

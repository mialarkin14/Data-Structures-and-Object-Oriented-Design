import HWs.hw5starter.Maze.maze as maze

class Game():
    '''Holds the game solving logic. Initialize with a fully initialized maze'''

    def __init__(self, maze):
        self._maze = maze

    # Creating simple methods (like the next two) to abstract core parts 
    #   of your algorithm helps increase the readability of your code.
    #   You will find these two useful in your solution.

    def _is_move_available(self, row, col, path):
        '''If (row, col) is already in the solved path then it is not available'''
        return (row, col) not in path

    def _is_puzzle_solved(self, row, col):
        '''Is the given row,col the finish square?'''
        return self._maze.get_finish() == (row, col)


    ########################################################
    # TODO - Main recursive method. Add your algorithm here.
    def find_route(self, currow, curcol, curscore, curpath):
        '''
        This is a function that finds the best path of a maze.
        It outputs the highest score possible and the associated path with that score.
        It takes in the row, column, current score, and current path.
        It uses recursion to go through each various path and find the best path 
        '''
        
        # Define the maxscore to -1 and the optimal path to an empty list
        # Create a variable for quick access of the start 
        maxscore = -1
        optimalpath = []
        start = self._maze.get_start()

        # Base Case - Return the highest score value and the path if on the finish square
        if self._is_puzzle_solved(currow, curcol) == True:
            return (curscore, curpath)
        
        # Base Case - Check if the start is in the currentpath if it is not add it
        if start not in curpath:
            curpath.append(start) 

        # The only possible moves you can make are right, left, up and down
        # Find these possible moves and add them to a possible_moves list
        right = (currow, curcol + 1)
        left = (currow, curcol - 1)
        up = (currow - 1, curcol)
        down = (currow + 1, curcol)
        possible_moves = [right, left, up, down]
        

        # Loop through the possible moves 
        for move in possible_moves:
            # Make a temporary path that equals our current path. We need a temporary path since 
            # recursively calling with current path would roll over into the next recursive call we make
            temporary_path = curpath.copy()
            # Check if the move we are on is an actual move we can make
            # Is the move available? It's not already in current path
            if self._is_move_available(move[0],move[1],curpath) == True:
                # Is the move actually in the maze?
                if self._maze.is_move_in_maze(move[0], move[1]) == True:
                    # Is the move not a wall?
                    if self._maze.is_wall(move[0], move[1]) != True:
                        # Need a temporary value because if use current score, it will roll over into the next recursive call
                        # Use the currentscore and add the move we make
                        temporary_val = curscore + int(self._maze.make_move(move[0], move[1], temporary_path))
                        # Recursively call again to find another route
                        score, path = self.find_route(move[0], move[1], temporary_val, temporary_path)
                        # If this new route is greater than the maxscore, then set the maxscore to that new route's score
                        # and that new route's path
                        if score > maxscore:
                            maxscore = score
                            optimalpath = path
        
        #Return the maxscore and the optimal path
        return maxscore, optimalpath

# This block of code will be useful in debugging your algorithm. But you still need
#  to create unittests to thoroughly testing your code.
if __name__ == '__main__':
    # Here is how you create the maze. Pass the row,col size of the grid.
    grid = maze.Maze(3, 6)
    # You have TWO options for initializing the Value and Walls squares.
    # (1) init_random() and add_random_walls()
    #     * Useful when developing your algorithm without having to create 
    #         different grids
    #     * But not easy to use in testcases because you cannot preditably
    #         know what the winning score and path will be each run
    # (2) _set_maze()
    #     * You have to create the grid manually, but very useful in testing
    #       (Please see the test_game.py file for an example of _set_maze())
    grid.init_random(0,9) # Initialze to a random board
    grid.add_random_walls(0.2)   # Make a certian percentage of the maze contain walls

    # AFTER you have used one of the two above methods of initializing 
    #   the Values and Walls, you must set the Start Finish locations. 
    start = (0,2)
    finish = (1,1)
    grid.set_start_finish(start, finish)

    # Printing the starting grid for reference will help you in debugging.
    print(grid)           # Print the maze for visual starting reference

    # Now instatiate your Game algorithm class
    game = Game(grid)     # Pass in the fully initialize maze grid

    # Now initiate your recursize solution to solve the game!
    # Start from the start row, col... zero score and empty winning path
    #score, path = game.find_route(start[0], start[1], 0, list())
    #print(f"The winning score is {score} with a path of {path}")
    print(game.find_route(start[0], start[1], 0, list()))


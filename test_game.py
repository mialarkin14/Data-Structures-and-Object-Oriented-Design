import unittest
import HWs.hw5starter.Maze.game as game
import HWs.hw5starter.Maze.maze as maze

class TestGame(unittest.TestCase):

    #Example test case
    def test1_example_test(self):
        '''An example test that shows all the steps to initialize and invoke the solution algorithm'''
        print("Testing example grid")
        # Create the maze grid to whatever size you want. But make it 2x2 or greater.
        grid = maze.Maze(5, 5)
        # Use this method to create test mazes
        grid._set_maze([["*", 1,  "*",  1,  1],
                        [2,   5,  "*", "*", 2],
                        [3,  "*", "*", "*", 8],
                        [9,  "*",  4,   7,  3],
                        [1,   3,   1,  "*", 2] ])
        start = (0,1)
        end = (0,3)
        # You need to set the start and end squares this way
        grid.set_start_finish(start, end)
        # Attach the maze to game instance
        testgame = game.Game(grid)
        # Initiate your recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1], 0, list())

        # If you need to debug a given test case, it might be helpful to use one or more of these print statements
        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        # Each test should assert the correct wining score and the correct winning path
        self.assertEqual(score, 49)
        self.assertEqual(path, [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), 
                                (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3)])

    #############################################
    # TODO - add the rest of your test cases here
    
    #Testing a small maze
    def test_small_maze(self):
        '''
        A test that tests a small 2x2 maze that asserts the score and path are as expected
        '''
        print("Testing a small maze")
        # Setting up the grid
        grid = maze.Maze(2,2)
        grid._set_maze([[0, 2],
                        [3, 4]])
        start = (0,0)
        finish = (1,0)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        # Asserting the score and path are as expected
        self.assertEqual(score, 6)
        self.assertEqual(path, [(0,0), (0,1), (1,1), (1,0)])

    #Testing a large maze
    def test_large_maze(self):
        '''
        A test that tests a large 5x7 maze that asserts the score and path are as expected
        '''
        print("Testing a large maze")
        # Setting up the gird
        grid = maze.Maze(5, 7)
        grid._set_maze([[0,  "*", 2, "*", 7,  9,  10],
                        [9,   4,  2,  8,  1,  4, "*"],
                        [8,   3,  1,  0, "*", 7,  3],
                        ["*", 2, "*", 6,  2,  5,  8],
                        [11,  6,  2,  6, "*", 7,  3]])
        start = (0, 6)
        finish = (4, 3)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        # Asserting the score and path are as expected
        self.assertEqual(score, 106)
        self.assertEqual(path, [(0, 6), (0, 5), (0, 4), (1, 4), (1, 5), (2, 5), (2, 6), (3, 6), (4, 6), 
                                (4, 5), (3, 5), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0), 
                                (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3)])
    
    #Testing a maze that only has one route
    def test_one_route(self):
        '''
        A test that tests a maze that only has one route and asserts the score and path are as expected
        '''
        print("Testing a maze with only one route")
        # Setting up the gird
        grid = maze.Maze(3,4)
        grid._set_maze([["*",  3,   8,  2],
                        ["*", "*", "*", 3],
                        ["*",  2,   6,  3]])
        start = (0,1)
        finish = (2,1)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        # Asserting the score and path are as expected
        self.assertEqual(score, 22)
        self.assertEqual(path, [(0,1), (0,2), (0,3), (1,3), (2,3), (2,2), (2,1)])
    
    #Edge case - A maze that is all walls
    def test_all_walls(self):
        '''
        A test that tests a maze that is all walls and asserts the score and path are as expected
        '''
        print ("Testing a maze that's all walls")
        # Setting up the grid
        grid = maze.Maze(2,4)
        grid._set_maze([[0,   "*",  "*", "*"],
                        ["*", "*",  "*",   1]])
        start = (0,0)
        finish = (1, 3)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
         # Asserting the score and path are as expected
        self.assertEqual(score, -1)
        self.assertEqual(path, [])


    #Edge case - A maze where start and finish are right next to each other
    def test_start_finish_close(self):
        '''
        Test a maze where the start and finish are adjacent and asserts the score and path are as expected
        '''
        print("Testing a maze where start and finish are adjacent")
        # Setting up the grid
        grid = maze.Maze(3,3)
        grid._set_maze([[0, 1, 5],
                        [6, 8, 3],
                        [2, 0, 4]])
        start = (0,0)
        finish = (1,0)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        # Asserting that the score and path are as expected
        self.assertEqual(score, 21)
        self.assertEqual(path, [(0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (1,1), (1,0)])

    #Edge case - A maze that is all numbers
    def test_all_numbers(self):
        '''
        Test a maze where it's only numbers and asserts the score and path are as expected
        '''
        print("Testing a maze that is all numbers")
        # Setting up the grid
        grid = maze.Maze(4,4)
        grid._set_maze([[1, 2, 3, 4],
                        [3, 9, 2, 6],
                        [4, 2, 0, 1],
                        [5, 3, 8, 2]])
        start = (0,3)
        finish = (3,3)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        # Asserting the score and path are as expected
        self.assertAlmostEqual(score, 49)
        self.assertEqual(path, [(0,3), (0,2), (0,1), (0,0), (1,0), (1,1), (1,2), (1,3), (2,3), 
                                (2,2), (2,1), (2,0), (3,0), (3,1), (3,2), (3,3)])
    
    #Edge case - A maze that is unsolveable
    def test_unsolveable_maze(self):
        '''
        A test that tests an unsolvable maze and asserts the score and path are as expected
        '''
        print("Testing a maze that is not solveable")
        # Setting up the grid
        grid = maze.Maze(2,2)
        grid._set_maze([["*",  1],
                        [1,  "*"]])
        start = (0,1)
        finish = (1,0)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        # Asserting the score and path are as expected
        self.assertEqual(score, -1)
        self.assertEqual(path, [])
        
    #Edge case - A maze that has all the same values
    def test_all_same_val(self):
        '''
        Testing a maze that has all the same values and asserts the score and path are as expected
        '''
        print("Testing a maze with all the same values")
        # Setting up the grid
        grid = maze.Maze(3, 4)
        grid._set_maze([["*", 3,  3,  "*"],
                        [3,   3,  "*",  3],
                        [3,   3,   3,   3]])
        start = (0, 2)
        finish = (2, 3)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        # Asserting the score and path are as expected
        self.assertEqual(score, 18)
        self.assertEqual(path, [(0,2), (0,1), (1,1), (1,0), (2,0), (2,1), (2,2), (2,3)])
    
    #Edge case - A maze that has all zero values
    def test_all_zero(self):
        '''
        Testing a maze that's value are all zeros andt that the score and path are as expected
        '''
        print("Testing a maze that has all zero values")
        # Setting up the grid
        grid = maze.Maze(3, 3)
        grid._set_maze([["*", 0,  0],
                        [0,   0, "*"],
                        [0,   0,  0]])
        start = (0, 2)
        finish = (2, 2)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        # Asserting the score and path are as expected
        self.assertEqual(score, 0)
        self.assertEqual(path, [(0,2), (0,1), (1,1), (1,0), (2,0), (2,1), (2,2)])


if __name__ == '__main__':
    unittest.main()

import unittest
from HWs.hw9_starter.Binary_Expression_Tree.BET import BETNode, create_trees, find_solutions, CCCXCXX_tree, CCXCXCX_tree


class TestBETNode(unittest.TestCase):
    print("Testing BETNode...")
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self): 
        '''
        Testing a tree of the following format and numbers/ operators
                *
              /   \
             2     +
                 /   \
                -     9
              /   \
             K     3 
        '''
        
        tree = CCCXCXX_tree("*", "2", "+", "-", "9", "K", "3")
        self.assertEqual(tree.evaluate(), 38)
    
    def test_evaluate_tree2(self): 
        '''
        Testing a tree of the following format and numbers/ operators
                   +
                /    \
               -      4
             /   \
            *     3
           / \
          A   2

        '''
        tree = CCXCXCX_tree("-", "+", "2", "/", "9", "6", "3")
        self.assertEqual(tree.evaluate(), 9)

    print("✅")

class TestCreateTrees(unittest.TestCase):
    print("Testing create_trees...")
    def test_hand1(self): 
        '''
        Testing a hand that creates all 7680 unique permutations
        '''
        trees = create_trees(["2", "4", "7", "9"])
        self.assertEqual(len(trees), 7680)
        
    def test_hand2(self): 
        '''
        Testing a hand that creates only 3840 unique permutations
        '''
        trees = create_trees(["6", "A", "3", "3"])
        self.assertEqual(len(trees), 3840)

    print("✅")

class TestFindSolutions(unittest.TestCase):
    print("Testing find_solutions...")
    def test0sols(self): 
        '''
        Testing a hand that has no solutions that sum to 24
        '''
        trees = find_solutions(["2", "2", "2", "2"])
        self.assertEqual(len(trees), 0)

    def test_A23Q(self): 
        '''
        Testing a hand that has 33 solutions that sum to 24
        '''
        trees = find_solutions(["A", "2", "3", "Q"])
        self.assertEqual(len(trees), 33)

    print("✅")
     
unittest.main()
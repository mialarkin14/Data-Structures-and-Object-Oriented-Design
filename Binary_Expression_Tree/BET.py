import itertools

class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    def add_left(self, val_op): 
        '''
        Adds a card or operation to the left of a node as a child
        '''
        #Sets the left to that val_op
        self.left = val_op

    def add_right(self, val_op): 
        '''
        Adds a card or operation to the right of a node as a child
        '''
        #Sets the right to that val_op
        self.right = val_op

    def evaluate(self): 
        '''
        Evaluates the subtree at the BETNode
        '''
        
        #If the value of the node is a plus, recurse through and add
        if self.value == "+":
            return self.left.evaluate() + self.right.evaluate()
        #If the value of the node is a plus, recurse through and subtract
        elif self.value == "-":
            return self.left.evaluate() - self.right.evaluate()
        #If the value of the node is a plus, recurse through and multiply
        elif self.value == "*":
            return self.left.evaluate() * self.right.evaluate()
        #If the value of the node is a plus, recurse through and divide
        elif self.value == "/":
            #If dividng by zero, return a large negative number
            if self.right.evaluate() == 0:
                return -1000000000
            else:
                return self.left.evaluate() / self.right.evaluate()
        else:
            #Return the value
            return self.CARD_VAL_DICT[self.value]

    def __repr__(self): 
        '''
        Displays the expression stored in the tree using infix notation
        '''
        
        #If the value is an operator 
        if self.value in self.OPERATORS:
            #Recurse through
            return "(" + repr(self.left) + str(self.value) + repr(self.right) + ")"
        #If the value is a number return the number
        else:
            return str(self.value)

def CCXCCXX_tree(a, b, c, d, e, f, g):
    '''
    Function that create a tree with the following format:

          +
        /    \
       *      -
      / \    / \
     A   2  3   4

    '''
    root = BETNode(str(a))
    root.add_left(BETNode(str(b)))
    root.add_right(BETNode(str(c)))
    root.left.add_left(BETNode(str(d)))
    root.left.add_right(BETNode(str(e)))
    root.right.add_left(BETNode(str(f)))
    root.right.add_right(BETNode(str(g)))
    return root


def CCXCXCX_tree(a, b, c, d,e, f, g):
    '''
    Function that creates a tree with the following format:
    
             +
           /   \
          -     4
        /   \
       *     3
      / \
     A   2

    '''

    root = BETNode(str(a))
    root.add_left(BETNode(str(b)))
    root.add_right(BETNode(str(c)))
    root.left.add_left(BETNode(str(d)))
    root.left.add_right(BETNode(str(e)))
    root.left.left.add_left(BETNode(str(f)))
    root.left.left.add_right(BETNode(str(g)))
    return root

def CCCXXCX_tree(a, b, c, d, e, f, g):
    '''
    Function that creates a tree with the following format:

                +
               /  \
              *    4
             / \
            A   -
               /  \
              2    3
    Takes in each tree value and strings it
    '''
    
    root = BETNode(str(a))
    root.add_left(BETNode(str(b)))
    root.add_right(BETNode(str(c)))
    root.left.add_left(BETNode(str(d)))
    root.left.add_right(BETNode(str(e)))
    root.left.right.add_left(BETNode(str(f)))
    root.left.right.add_right(BETNode(str(g)))
    return root

def CCCXCXX_tree(a, b, c, d, e, f, g):
    '''
    Function that creates a tree with the following format:
                *
              /   \
             A     +
                 /   \
                -     4
              /   \
             2     3 
    Takes in each tree value and strings it
    '''
    root = BETNode(str(a))
    root.add_left(BETNode(str(b)))
    root.add_right(BETNode(str(c)))
    root.right.add_left(BETNode(str(d)))
    root.right.add_right(BETNode(str(e)))
    root.right.left.add_left(BETNode(str(f)))
    root.right.left.add_right(BETNode(str(g)))
    return root

def CCCCXXX_tree(a, b, c, d, e, f, g):
    '''
    Function that creates a tree with the following format:

                *
              /   \
             A     -
                 /   \
                2     +
                    /   \
                   3     4 
    Takes in each tree value and strings it
    '''
    
    root = BETNode(str(a))
    root.add_left(BETNode(str(b)))
    root.add_right(BETNode(str(c)))
    root.right.add_left(BETNode(str(d)))
    root.right.add_right(BETNode(str(e)))
    root.right.right.add_left(BETNode(str(f)))
    root.right.right.add_right(BETNode(str(g)))
    return root


def create_trees(cards): 
    '''
    A Function that creates a set of trees that can be solved
    Takes in a list of cards
    There are 7680 unique trees when there are no duplicates in the inputed list
    ''' 
    #Operations that can be used to create a tree
    opers = ["+", "-", "*", "/"]
    #Create an empty set 
    trees = set()

    #Create all different types of combinations based on cards and operations
    for element in itertools.product(opers, repeat= 3):
        operations = list(element)
    
        for subset in itertools.permutations(cards + operations):
            #Create a string representation of each possible combination
            result = ""
            for element in subset:
                if element in ["+", "-", "*", "/"]:
                    result = result + "X"
                else:
                    result = result + "C"
            

            #If the string combination follows one of the following types of trees
            #Create that tree and add it to the set
            if result == "CCXCCXX":
                root = CCXCCXX_tree(subset[6], subset[5], subset[2], subset[3], subset[4], subset[1], subset[0])
                trees.add(root)
    
            if result == "CCXCXCX":
                root = CCXCXCX_tree(subset[6], subset[2], subset[5], subset[4], subset[3], subset[1], subset[0])
                trees.add(root)
        
            if result == "CCCXXCX":
                root = CCCXXCX_tree(subset[6], subset[3], subset[2], subset[1], subset[4], subset[5], subset[0])
                trees.add(root)

            if result == "CCCXCXX":
                root = CCCXCXX_tree(subset[6], subset[0], subset[3], subset[5], subset[4], subset[2], subset[1])
                trees.add(root)
            
            if result == "CCCCXXX":
                root = CCCCXXX_tree(subset[6], subset[1], subset[5], subset[2], subset[4], subset[3], subset[0])
                trees.add(root)

    #Return set of unique and valid trees
    return trees

def find_solutions(cards): 
    #Create an empty set of solutions
    solutions = set()
    #Generate all the possible trees
    trees = create_trees(cards)
    #Check if each tree evaluates to 24
    for tree in trees:
        if tree.evaluate() == 24:
            #Add to solutions set if the tree evaluates to 24
            solutions.add(repr(tree)) 
        

    #Return set of trees that evaluate to 24
    return solutions
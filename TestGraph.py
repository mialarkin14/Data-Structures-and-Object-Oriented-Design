from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    '''
    A class that tests the Graph class by setting up one graph
    and using it for various tests 
    '''
    
    print("Testing graph with Edge Set Graph and Adjaceny Set Graph...")
    
    def setUp(self):
        '''
        Sets up a graph and makes sure that each vertex and 
        edge is in the graph by testing the add vertex and add edge

                                1,728.4 miles
                Portland -------------------------- Minneapolis
                    \                                   
                     \  766.1 miles                                 
                      \                                 
                Salt Lake City ----------- Denver
                            /   518.7 miles  /         
              420.4 miles  /            / 757.7 miles 
                          /         /
                    Las Vegas /

        '''

        #Defines vertices, edges, and graph
        vertices = ["Portland", "Minneapolis", "Salt Lake City", "Denver", "Las Vegas"]
        edges = [("Portland", "Minneapolis", 1,728.4), ("Portland", "Salt Lake City", 766.1), 
                 ("Salt Lake City", "Portland", 766.1), ("Salt Lake City", "Denver", 518.7),
                 ("Salt Lake City", "Las Vegas", 420.4), ("Denver", "Salt Lake City", 518.7), 
                 ("Denver", "Las Vegas", 757.7), ("Las Vegas", "Salt Lake City", 420.4), 
                 ("Las Vegas", "Denver", 757.7), ("Minnapolis", "Portland", 1,728.4)]
        self.g0 = Graph()

        #Adds each vertex and edge to the graph
        for vertex in vertices:
            self.g0.add_vertex(vertex)
        for edge in edges:
            self.g0.add_edge(edge[0], edge[1], edge[2])
        
        #Testing that the vertices are in the graph
        for vertex in vertices:
            self.assertTrue(self.g0.contains_vertex(vertex))
        #Testing that the edges are in the graph
        for edge in edges:
            self.assertTrue(self.g0.contains_edge(edge[0], edge[1], edge[2]))
        
    def test_remove_vertex(self):
        '''
        Uses the graph made in setUp to test remove_vertex
        method in the Graph class
        '''

        #Removes vertex Portland and asserts it's not in the graph
        self.g0.remove_vertex("Portland")
        self.assertFalse(self.g0.contains_vertex("Portland"))
        #Asserts that the edges with Portland are removed from the graph
        self.assertFalse(self.g0.contains_edge("Portland", "Minneapolis", 1728.4)) 
        self.assertFalse(self.g0.contains_edge("Portland", "Salt Lake City", 766.1))
        self.assertFalse(self.g0.contains_edge("Salt Lake City", "Portland", 766.1))
        self.assertFalse(self.g0.contains_edge("Minneapolis", "Portland", 1728.4))

        #Try to remove a vertex not in the graph
        try:
            self.g0.remove_vertex("Phoenix")
        except:
            KeyError("Vertex Phoenix is not in the graph")
    
    def test_remove_edge(self):
        '''
        Uses the graph made in setUp to test remove_edge
        method in the Graph class
        '''

        #Removes edge ("Las Vegas", "Denver", 757.7) and asserts not in the graph
        self.g0.remove_edge("Las Vegas", "Denver", 757.7)
        self.assertFalse(self.g0.contains_edge("Las Vegas", "Denver", 757.7))
        self.assertFalse(self.g0.contains_edge("Denver", "Las Vegas", 757.7))
        #Try to remove an edge not in the graph
        try:
            self.g0.remove_edge("Phoenix", "Denver", 1509)
        except:
            KeyError("Edge (Phoenix, Denver, 1509), not in the graph")
    
    def test_neighbors(self):
        '''
        Uses the graph in setUp to test nbrs method in Graph class
        '''

        #Expected neighbors of Denver
        expected_neigh0 = {"Las Vegas", "Salt Lake City"}
        #Assert neighbors of New Haven are in expected neighbors
        x = {neigh for neigh in self.g0.nbrs("Denver")}
        self.assertEqual(x, expected_neigh0)     
        #Remove an edge and reassert
        self.g0.remove_edge("Denver", "Las Vegas", 757.7)
        y = {neigh for neigh in self.g0.nbrs("Denver")}
        self.assertEqual(y, {"Salt Lake City"})

        #Expected neighbors of Salt Lake City
        expected_neigh1 = {"Denver", "Portland", "Las Vegas"}
        #Assert neighbors of Salt Lake City are equal to expected neighbors
        a = {neigh for neigh in self.g0.nbrs("Salt Lake City")}
        self.assertEqual(a, expected_neigh1)
        #Remove an edge and reassert
        self.g0.remove_edge("Salt Lake City", "Denver", 518.7)
        b = {neigh for neigh in self.g0.nbrs("Salt Lake City")}
        self.assertEqual(b, {"Portland", "Las Vegas"})
        #Remove an edge and reassert
        self.g0.remove_edge("Salt Lake City", "Las Vegas", 420.4)
        b = {neigh for neigh in self.g0.nbrs("Salt Lake City")}
        self.assertEqual(b, {"Portland"})
        #Remove an edge and reassert
        self.g0.remove_edge("Salt Lake City", "Portland", 766.1)
        b = {neigh for neigh in self.g0.nbrs("Salt Lake City")}
        self.assertEqual(b, set())


        #Try a vertex that's not in the graph
        try:
            self.g0.nbrs("Fairfield")
        except:
            KeyError("Vertex Fairfield not in graph")

    def test_find_weight(self):
        '''
        Uses the graph in setUp to test the find_weight method in Graph class
        '''
        self.assertEqual(self.g0.find_weight("Portland", "Minneapolis"), 1,728.4)
        self.assertEqual(self.g0.find_weight("Denver", "Salt Lake City"), 518.7)
    
    def test_remove_edge_vertex(self):
        '''
        Uses the graph in setUp to test the remove_edge_vertex method in Graph class
        '''

        #Remove a city
        self.g0.remove_edge_vertex("Minneapolis")
        #Assert that any of the edges with the vertex is removed
        self.assertFalse(self.g0.contains_edge("Minneapolis", "Portland", 1728.4))
        self.assertFalse(self.g0.contains_edge("Portland", "Minneapolis", 1728.4)) 
        
    print("✅")
    
class test_GraphTraversal(unittest.TestCase):
    '''
    Class that tests Graph traversal
    Sets up one graph for all tests to use
    '''

    print("Testing Graph traversal algorithms...")

    def setUp(self):
        '''
        Sets up a graph and makes sure that each vertex and 
        edge is in the graph by testing the add vertex and add edge

                                                                  Moscow \ 
                                     4,399 miles       999 miles    /      \ 
                Chicago --------------------------------------- Berlin       \ 
                    \                               544 miles   /       \      \   2,697 miles
                     \                                      Paris          \     \ 
                       \                                      /  4313 miles   \    \ 
                         \                                   /                  Delhi
                           \                                /
              5,596 miles    \                             / 6861 miles
                               \                          / 
                                 \                       /
                                   \                   /     
                                       Buenos Aires   

        '''

    #Defines vertices, edges, and graph
        vertices = ["Chicago", "Buenos Aires", "Paris", "Berlin", "Moscow", "Delhi"]
        edges = [("Chicago", "Buenos Aires", 5596), ("Chicago", "Berlin", 4399), 
                 ("Buenos Aires", "Chicago", 5596), ("Buenos Aires", "Paris", 6861),
                 ("Berlin", "Chicago", 4399), ("Berlin", "Moscow", 999), ("Berlin", "Paris", 544),
                 ("Berlin", "Delhi", 4313),
                 ("Paris", "Buenos Aires", 6861), ("Paris", "Berlin", 544),
                 ("Moscow", "Berlin", 999), ("Moscow", "Delhi", 2697),
                 ("Delhi", "Berlin", 4313), ("Delhi", "Moscow", 2697)]
        self.g = Graph()

        #Adds each vertex and edge to the graph
        for vertex in vertices:
            self.g.add_vertex(vertex)
        for edge in edges:
            self.g.add_edge(edge[0], edge[1], edge[2])
        
        #Testing that the vertices are in the graph
        for vertex in vertices:
            self.assertTrue(self.g.contains_vertex(vertex))
        #Testing that the edges are in the graph
        for edge in edges:
            self.assertTrue(self.g.contains_edge(edge[0], edge[1], edge[2]))

    def test_fewest_flights(self):
        '''
        Uses the graph in setUp to test the fewest_flights method in the Graph class
        '''
    
    # Which alg do you use here, and why?
    # Alg: Breadth-First Search
    # Why: This algorithm finds the fewest number of edges to get to every other city which is the 
    #       the fewest number of flights in this case


        #Check fewest flights to travel from Berlin 
        trav, edge = self.g.fewest_flights("Berlin")
        #Expected traversal and edges
        exp_edge = {"Berlin": 0, "Moscow": 1, "Paris": 1, "Chicago": 1, 
                    "Delhi": 1, "Buenos Aires": 2}
        #Assert Equal
        self.assertEqual(edge, exp_edge)

        #Check fewest flights to travel from Delhi 
        trav, edge = self.g.fewest_flights("Delhi")
        #Expected traversal and edges
        exp_edge = {"Delhi": 0, "Moscow": 1, "Paris": 2, "Chicago": 2, 
                    "Berlin": 1, "Buenos Aires": 3}
        #Assert Equal
        self.assertEqual(edge, exp_edge)

 
    def test_shortest_path(self):
        '''
        Uses the graph in setUp to test the shortest_path method in the Graph class
        '''

    # Which alg do you use here, and why?
    # Alg: Dijkstra's 
    # Why: Dijkstra's algorithm will find the shortest distance from one node to every other node
    #       which is the shortest path in this case 

        #Check shortest paths from Berlin
        trav, diction = self.g.shortest_flights("Berlin")
        #Expected traversal and dictionary
        exp_diction = {"Berlin": 0, "Paris": 544, "Moscow": 999, "Delhi": 3696, "Chicago": 4399, "Buenos Aires": 7405}
        #Assert Equal
        self.assertEqual(diction, exp_diction)


        #Check shortest paths from Chicago
        trav, diction = self.g.shortest_flights("Chicago")
        #Expected traversal and dictionary
        exp_diction = {"Chicago": 0, "Paris": 4943, "Moscow": 5398, "Delhi": 8095, "Berlin": 4399, "Buenos Aires": 5596}
        #Assert Equal
        self.assertEqual(diction, exp_diction)


    def test_minimum_salt(self):
        '''
        Uses the graph in setUp to test the minimum_salt method in the Graph class
        '''
    # Which alg do you use here, and why?
    # Alg: Prim's Algorithm
    # Why: Prim's algorithm will create a minimum spanning path and this is what we want
    # to connect every other city int he graph with the fewest number of miles

        #Checks minimum salt path for Paris
        trav, dictionary = self.g.minimum_salt("Paris")
        #Expected total of path
        sum = 0
        for vert in dictionary:
            if dictionary[vert] == None:
                sum += 0
            else:
                sum += dictionary[vert]
        
        #Assert equal       
        self.assertEqual(sum, 14235)


    print("✅")
unittest.main()
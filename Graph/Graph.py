from HWs.hw11_starter.Graph.Heap import Heap
from HWs.hw11_starter.Graph.ADTs import Queue

class Graph:
    def __init__(self, V = None, E = None):
        '''
        Takes in an optional set of vertices and edges
        If no no input, vertex is set to an empty set and edges is set to 
        an empty set
        If input, iterates through each and adds to each set
        '''
        self.V = set()
        self.neighbors = dict()
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for e in E:
                self.add_edge(e)  
        
    def contains_vertex(self, v):
        '''
        Returns true if the vertex is in the graph
        else returns false
        MAINLY TO MAKE TESTING EASIER 
        '''
        return v in self.V
    
    def contains_edge(self, u, v, wt):
        '''
        Returns true if edge is in the graph
        else retuns false
        MAINLY TO MAKE TESTING EASIER 
        '''

        T_F = False

        #If the key is not in the dictionary, return false
        if u not in self.neighbors:
            #Return False
            return False

        #The key is in the dictionary so go through list at that key
        elif u in self.neighbors:
            for tup in self.neighbors[u]:
                #If the first value of the tuple is the vertex and the second is the weight
                if tup[0] == v and tup[1] == wt:
                    #Set tracker to true
                    T_F = True     
        return T_F
    
    def find_weight(self, u, v):
        '''
        Finds the weight associated with the connection
        '''
        #Sets a variable weight to None
        weight = None
        #Go through each vertex weight tuple at that key 
        for tup in self.neighbors[u]:
            #If the vertex is equal to the inputted vertex
            if tup[0] == v:
                #Set the weight to the weight at that edge
                weight = tup[1]

        #Return the weight
        return weight

    def add_vertex(self, v):
        '''
        Adds vertex v to graph
        '''
        self.V.add(v)

    def remove_vertex(self, v):
        '''
        Removes vertex v from graph
        Raises a KeyError if the edge is not in the graph
        '''
        #If the vertex is in the set, remove it
        if v in self.V:
            self.V.remove(v)
        #If it's not, raise a KeyError
        else:
            raise KeyError(f"Vertex {v} is not in the graph")
        #Removes the edges that have this vertex
        self.remove_edge_vertex(v)
        
    def add_edge(self, u, v, wt):
        '''
        Adds an edge with the given arguments
        Adds it to the dictionary as vertex: pointing vertex
        Each value in the dictionary is a list so you can add edges
        '''
        
        #If the vertex is not in the dictioanry, add it
        if u not in self.neighbors:
            self.neighbors[u] = [(v, wt)]
        
        #Vertex is in the dictionary so append it to list
        else:
            self.neighbors[u].append((v, wt))

        #Adds a vertex to the vertex set if not already in the set      
        if u not in self.V:
            self.add_vertex(u)
        if v not in self.V:
            self.add_vertex(v)

    
    def remove_edge_vertex(self, vertex):
        '''
        Removes an edge based on the vertex, any edge with that vertex also gets removed 
        Takes in a vertex
        '''

        #A list of keys to be removed
        remove_keys = []
        
        #Go through the dictionary 
        for v in self.neighbors:
            #Go through each tuple in the list 
            for tup in self.neighbors[v]:
                #If the vertex is equal to the vertex we want to remove
                if tup[0] == vertex:
                    #Remove only the tuple
                    self.neighbors[v].remove((tup))

        #Go through dictionary
        for v in self.neighbors:
            #If the key is the vertex, add that key to the remove keys list
            if v == vertex:
                remove_keys.append(v)
        
        #Go through the remove keys list and remove the key in the dictionary
        for key in remove_keys:
            del self.neighbors[key]
    
    def remove_edge(self, u, v, wt):
        '''
        Removes the edge with the given arguments
        Raises a KeyError if the edge is not in the graph
        '''
        tup = (v, wt)
        tup1 = (u, wt)
        in_dictionary = False
        #Checks that the starting vertex is in the dictionary
        if u in self.neighbors:
            #Go through the list at that key
            for vert_weight in self.neighbors[u]:
                #If a tuple in the list matches the arguments
                if vert_weight == tup:
                    #Remove that tuple and set in_dictionary to true
                    in_dictionary = True
                    self.neighbors[u].remove(vert_weight)
                    break
        #Repeats the above for the flipped edge
        if v in self.neighbors:
            for vert_weight1 in self.neighbors[v]:
                if vert_weight1 == tup1:
                    self.neighbors[v].remove(vert_weight1)
                    break

        #Raises a KeyError if edge not in the set
        elif in_dictionary == False: 
            raise KeyError(f"Edge {(u, v, wt)}, not in the graph")

    def nbrs(self, v):
        '''
        Returns an iterable colletion of neighbors of vertex v
        In the set, the values are stored as tuples
        with the edge and weight --> (v, wt)
        '''
        
        #If the vertex is not in the set of vertices, raise a KeyError
        if v not in self.V:
            raise KeyError(f"Vertex {v} not in graph")
        
        vertex_neigh = []
        x = self.neighbors[v]
        for tup in x:
            vertex_neigh.append(tup[0])
        #Return the set of neighbors
        return iter(vertex_neigh)
    
    
    def edgecount(self, tree, u, v):
        '''
        Takes in a tree and two vertices
        Finds the number of edges bewteen the two vertices based on the tree
        Returns the number of edges
        '''
        
        #Set variable edgecount to o 
        edgecount = 0
        #While city1 is not city2 
        while v is not u:
            #Add one to the edge count
            edgecount += 1
            #Turn city1 to its city in the tree traversal
            v = tree[v]
        #Return edge count
        return edgecount 
    
    def fewest_flights(self, city):
        '''
        Takes in a city and finds the fewest number of flights to 
        any other city in the graph
        Returns a dictionary tree showing traversal order
        Returns a dictionary of vertex:distance pairs 
        Uses a breadth-first search
        '''
        
        #Defines variables, uses a queue
        tree = {}
        to_visit = Queue()
        to_visit.enqueue((None, city))
        #While the length of t0_visit does not equal 0:
        while len(to_visit) != 0:
            #Dequeue (Remove and return item from begining of the queue)
            a, b = to_visit.dequeue()
            #If the city is not in the tree, make it's dictionary value the other city
            if b not in tree:
                tree[b] = a
                #Find neighbors of city (b) and add to queue
                for n in self.nbrs(b):
                    to_visit.enqueue((b,n))
        #Cycle above repeats until the length of the queue is zero
        
        #Find the number of edges using edgecount method 
        edge = dict()
        for vert in self.V:
            edge[vert] = self.edgecount(tree, city, vert)  
                
        #Returns tree traversal and edges
        return tree, edge

    def shortest_flights(self, city):
        '''
        Takes in a city and finds the fewest number of miles travelled
        to any other city in the graph
        Returns a dictionary tree showing traversal order
        Returns a dictionary of vertex:distance pairs 
        Uses Dijkstra's algorithm
        '''

        #Defines variables, uses a heap
        tree = {}
        dictionary = {city: 0}
        to_visit = Heap()
        to_visit.insert((None, city), 0)
        #For each city in to_visit
        for a,b in to_visit:
            #If the city is not in the tree, add it
            if b not in tree:
                tree[b] = a
                #Add the total weight from the city
                if a is not None:
                    dictionary[b] = dictionary[a] + self.find_weight(a,b)
                #Find new neighbors and add to to_visit with the weight being the total from the initial city
                for n in self.nbrs(b):
                    to_visit.insert((b,n), dictionary[b] + self.find_weight(b, n))
        
        #Returns tree traversal and each cities distance from the inputted city
        return tree, dictionary

    def minimum_salt(self, city):
        '''
        Takes in a city and connects to every other city in the graph 
        with fewest number of miles
        Returns a dictionary tree showing traversal order
        Returns a dictionary of vertex:distance pairs 
        Uses Prim's algorithm
        '''

        #Defines variables, uses a heap
        tree = {}
        to_visit = Heap()
        to_visit.insert((None, city), 0)
        #For each city in to_visit
        for a, b in to_visit:
            #If the city is not in the tree, add it
            if b not in tree:
                tree[b] = a
                #Find new neighbors and add to to_visit with the weight of the edge
                for n in self.nbrs(b):
                    to_visit.insert((b,n), self.find_weight(b, n))
        
        #Go through the tree and fidn the weight of each edge and add it to the dictionary
        length_edge = dict()
        for vert in tree:
            if vert[0] and vert[1] != None:
                length_edge[vert] = self.find_weight(vert, tree[vert])
        
        #Returns tree traversal and each distance from edge in the tree
        return tree, length_edge

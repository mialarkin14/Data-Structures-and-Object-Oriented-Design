# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1
        
        # adds the head to the dictionary
        self._nodes[self._head.item] = self._head

        # if that was the first node
        if len(self) == 1: self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: self._head._next._prev = self._head


    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1
        
        # adds the tail to the dictionary
        self._nodes[self._tail.item] = self._tail

        # if that was the first node
        if len(self) == 1: self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else: self._tail._prev._next = self._tail


    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # removes the head from the dictionary
        del self._nodes[item]

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None
        
        return item
        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # removes the tail from the dictionary
        del self._nodes[item]

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._head = None

        else: self._tail._next = None

        return item
        
    # TODO: Add a docstring and implement
    def __contains__(self, item):
        '''
        This method is a magic method that takes in an item and checks if the item
        is in the _nodes dictionary. We use this since _nodes is technically private
        and we don't want to actually call _nodes
        '''

        #Checks if the item is in the dictionary, if yes, then return true if not return false
        if item in self._nodes:
            return True   
        else:
            return False  
   
    # TODO: Add a docstring and implement
    def neighbors(self, item):
        '''
        This method takes in an item and returns the item immediately before 
        and after the node with the item. If the item is not in the DLL, then a
        RuntimeError will be raised.
        Returns the item before and after as a tuple
        '''
    
        #Checks if the item is in the dictionary 
        if item in self._nodes:
            #Gets the node of the item in the dictionary
            node = self._nodes[item]
            #If the next item is not None, then set the next_item to the item, else set to None
            if node._next != None:
                next_item = node._next.item
            elif node._next == None:
                next_item = None
            #If the previous item is not None, then set the previous_item to the item, else set to None
            if node._prev != None:
                previous_item = node._prev.item
            elif node._prev == None:
                previous_item = None
            #Return the previous item and next item as a tuple pair
            return (previous_item, next_item)

        #If the item is not in the dictionary, raise a runtimeerror    
        else:
            raise RuntimeError ("This item is not in the lsit")


    # TODO: Add a docstring and implement
    def remove_node(self, item):
        ''''
        The method removes a specific node and then sets the adjacent nodes pointing to 
        the right previous and next node.
        It will raise a RuntimeError if the item is not in the DLL
        Return the node that is removed 
        '''

        #Edge case where raise RuntimeError if the list/ dictionary is empty
        if len(self._nodes) == 0:
            raise RuntimeError ("Can't remove from an empty list")

        #Checks if the item is in the dictionary
        if item in self._nodes:
            #Gets the node of the item
            node = self._nodes[item]
            
            #If the item removed is the last item, then set the previous item to the new tail
            if node == self._tail:
                new_tail = node._prev
                new_tail._next = None
                self._tail = new_tail
                #Update length, remove item from dictionary, return item
                self._len -=1
                del self._nodes[item]
                return item
            else: 
            #Sets the previous item to the node's previous item and the next item to the node's next item
                node_previous_item = node._prev
            
            #If the item removed is the first item, then set the next item to the new head
            if node._prev == None:
                new_head = node._next
                new_head._prev = None
                self._head = new_head
                #Update length, remove item from dictionary, return item
                self._len-=1
                del self._nodes[item]
                return item
            else: 
                node_next_item = node._next

            #Stitches together by setting the previous item's next to the next item and the next item's previous item to the previous item
            node_previous_item._next = node_next_item 
            node_next_item._prev = node_previous_item

            #Update length, remove item from dictionary, return item
            self._len -= 1
            del self._nodes[item]
            return item
        
        #If the item isn't in the list, raise a RuntimeError
        else:
            raise RuntimeError ("This item is not in the list")
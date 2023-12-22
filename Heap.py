class Entry:
    '''
    A class that creates an entry with 
    the item and it's priority
    '''

    def __init__(self, item, priority):
        '''
        Defines item and priority to be be class variables
        '''
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        '''
        Defines less than to be a comparision of priorities 
        '''
        return self.priority < other.priority

    def __repr__(self):
        '''
        Returns and representation of the entry
        '''
        return f"Entry(item={self.item}, priority={self.priority})"

class Heap:
    def __init__(self):
        '''
        Uses a list wrapper to create the heap
        '''
        self._L = []

    def __len__(self): 
        '''
        Returns the length of the heap
        '''
        return len(self._L)

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self) > 0:
            return self.remove_min()
        else:
            raise StopIteration 

    def _i_parent(self, idx):
        '''
        Returns the index of the parent of index idx
        '''
        return (idx-1) // 2 if (idx-1) // 2 >= 0 else None
    
    def _i_left(self, idx):
        '''
        Returns the index of the left child of index idx
        '''
        il = idx*2+1
        return il if il<len(self) else None
    
    def _i_right(self, idx):
        '''
        Returns the index of the right child of index idx
        '''
        ir = idx*2+2
        return ir if ir<len(self) else None

    def insert(self, item, priority):
        '''
        Adds item w/ given priority to heap
        '''
        #Create a new entry
        new_e = Entry(item=item, priority=priority)
        #Append entry to list
        self._L.append(new_e)
        #Upheap the tree until it's balanced
        self._upheap(len(self)-1)
    
    def _upheap(self, idx):
        '''
        Upheaps the item at idx 
        '''
        #Find the parent index
        i_p = self._i_parent(idx)

        #While the parent exists and parent is bigger: swap
        while i_p is not None and self._L[i_p] > self._L[idx]:
            #Swap them
            self._L[i_p], self._L[idx] = self._L[idx], self._L[i_p]
            #Update variables for the next loop
            idx = i_p
            i_p = self._i_parent(idx)
        
    def peek(self):
        '''
        Returns item with minimum priority
        Doesn't remove the item
        '''
        return self._L[0].item
    
    def remove_min(self):
        '''
        Returns item with minimum priority
        Removes the item
        '''
        
        #Defines minimum item to be the first item in the heap
        min_item = self._L[0].item
        
        #Edge case only one entry in heap
        if len(self) == 1:
            self._L.pop()
            return min_item
        
        #Removes the minimum item and downheap until heap balanced
        self._L[0] = self._L.pop()
        self._downheap(idx = 0)

        #Return the minimum item
        return min_item

    def _find_min_child(self, idx):
        '''
        Returns the idx of the minimum child if it exists
        Returns None otherwise 
        '''
        il = self._i_left(idx)
        ir = self._i_right(idx)

        #Only have one child
        if ir is None:
            return il
        
        #Have two children 
        else:
            return il if self._L[il] < self._L[ir] else ir

    def _downheap(self, idx):
        '''
        Upheaps the item at idx 
        '''

        #Finds minimum child at the index
        i_min = self._find_min_child(idx)

        #While minimum child exists and is less than item: swap
        while i_min is not None and self._L[i_min] < self._L[idx]:
            #Swap
            self._L[i_min], self._L[idx] =  self._L[idx], self._L[i_min]
            #Updates variables for next loop
            idx = i_min
            i_min = self._find_min_child(idx)
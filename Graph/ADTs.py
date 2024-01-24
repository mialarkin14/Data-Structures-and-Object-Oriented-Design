class Queue:
    '''
    A List Wrapper that implements a Queue
    '''

    def __init__(self):
        self._L = []

    def enqueue(self, item):
        '''
        Add an item to end of queue
        '''

        self._L.append(item)
    
    def dequeue(self):
        '''
        Remove and return an item from beginning of queue
        '''

        return self._L.pop(0)

    def __len__(self):
        '''
        Returns the length of the queue
        '''

        return len(self._L)

class Stack:
    '''
    A List Wrapper that implements a Stack
    '''

    def __init__(self):
        self._L = []

    def push(self, item):
        '''
        Add an item to end of stack
        '''

        self._L.append(item)

    def pop(self):
        '''
        Remove and return an item from end of stack
        '''

        return self._L.pop()
    
    def __len__(self):
        '''
        Returns the length of the stack
        '''
        
        return len(self._L)
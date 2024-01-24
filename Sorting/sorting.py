# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L): 
    ''''
    A function that finds the index of the zero in a half sorted list. 
    Has a Big-O of O(log(n))
    Uses a binary search to find the zero in log(n) run time
    '''
    
    #Edge case - The list is empty
    if L == []:
        return -1

    #Sets the left index to zero and the right index to the length of the list
    left_index = 0
    right_index = len(L)
    #While the (right index - the left index) is greater than zero:
    #   1) Calculate the median
    #   2) If the value at the median index is greater than zero, then we know zero must be an index
    #      less than the median index (in the left half), thus the right index becomes the new median
    #   3) If the value at the median index is less than zero, then we know zero must be at an index
    #      greater than the median index (in the right half), thus the left index becomes the new median
    while right_index - left_index > 1:
        median = (right_index + left_index)//2 
        if 0 < L[median]:
            right_index = median
        else: 
            left_index = median
    #Exiting the while loop, (right index - left index) must equal 1 so if the right index is greater than
    #the left index and the value at the left index is zero, return the left index
    if right_index > left_index and L[left_index] == 0:
        return left_index 
    
def bubble(L, left, right):  
    '''
    This is a function that uses bubble sort to sort a list that is split into negative and positive
    by a zero. It bubbles the first highest value it encouters in iteration to the end of the list and 
    repeats for the length of the list.
    It takes in a list, the left index, and the right index. It sorts it in place, not returning anything. 
    In the best case the Big-O will be O(n). In the worse case, it will be O(n^2). Average it will be O(n^2)
    '''
    #The invariant for the bubble sort is after j loops, we know the largest j items are in their final sorted location 
    #Iterate through the "mini" list seperated by a zero
    for j in range(left, right-1):
        #Iterate through the "mini" list and create a flag to stop early
        keepgoing = False
        for i in range(left, right -1): 
            #If two items are out of place
            if L[i] > L[i + 1]:     
                keepgoing = True
                #Switch them
                L[i], L[i + 1] = L[i + 1], L[i]     
        if not keepgoing: break

def selection(L, left, right):  
    '''
    This is a function that uses a selection sort to sort a list that is split into negative and positive by a zero. 
    It selects the smallest element from the list and places it at the beginning for each iteration
    It takes in a list, the left index, and the right index. It sorts it in place, not returning anything.
    In any case, worst, best, or average, the Big-O will be O(n^2)
    '''
    #The invariant for the selection sort is after j loops, the last j items are in their final sorted location
    #Iterate through the "mini" list seperated by a zero
    for j in range(left, right):
        #Suppose j is the smallest item in the "mini" list
        min_index = j
        for i in range(j+1, right):
            #Find the true smallest item
            if L[i] < L[min_index]:
                min_index = i
        #Swaps the smallest item to the corret spot
        L[j], L[min_index] = L[min_index], L[j] 


def insertion(L, left, right): 
    '''
    This is a function that uses an insertion sort to sort a list that is split into negative and positive
    by a zero. 
    It creates sub sorted lists as it iterates through. The next value it iterates to is then inserted into the correct
    place in the sub sorted list
    It takes in a list, the left index, and the right index. It sorts it in place, not returning anything. 
    In the best case the Big-O will be O(n). The worst case and average case will be O(n^2)
    '''
    
    #The invariant for insertion sort is after j loops, the last j items will be sorted relative to each other
    #Iterate through the "mini" list seperated by a zero
    for j in range(left, right):
        #Key always stays the same
        key = L[j]
        i = j -1
        #Compare the key with each element to the left of it until you find a smaller element
        while i >=0 and key < L[i]:
            L[i +1] = L[i]
            i -= 1
        #Insert that key after the element that is smaller than it 
        L[i+1] = key
        

def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half


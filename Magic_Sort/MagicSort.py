from math import log2

def linear_scan(L): 
    '''
    A function that conducts a linear scan on a list.
    Looks for edge cases:
        1) If the list is already sorted 
        2) If at most, there are 5 items our of place, use insertion sort function
        3) If the list is reverse sorted, use the reverse list function
    Returns a tuple that detonates which (if any) edges cases apply in order of sorted, insertion sort, reverse sort
    '''
    
    out_of_place = 0            #Counter for the number of items out of place
    n = len(L)                  #Keep a variable for the length of the list

    for i in range(n-1):        #Go through each item in a list
        if L[i] >= L[i + 1]:     #If the value beforehand is greater than the second one
            out_of_place += 1   #Increase the out of place counter

    if out_of_place == 0:       #If the number of out of place is zero
        return L                #Return the list
    
    if out_of_place == n-1:     #If the number of out of place is all of the list, (the list is in reverse)
        return "Use reverse sort"  #Return this message
    
    if out_of_place < 5 and out_of_place != 0:       #If the number of out of place items is less than or equal to 5, 
        return "Use insertion"  #Return this message


def reverse_list(L, track_sort = set()): 
    '''
    If the list is reverse sorted, reverse the list in linear time
    '''
    
    track_sort.add("reverse_list")

    #Not allowing the reverse sort of a non reversed list
    x = linear_scan(L)
 
    n = len(L) - 1              #Variable for the length of list - 1
    i = 0                       #Variable for stepping through each value in the list
    L1 = L[::]                  #Making a copy of the list
    
    while i <= (len(L)-1):      #Keep doing the following until i is less than or equal to the length of list 
        #Going through each value in the original list and replacing it with the correct 
        # value from the copied list
        L[i] = L1[n]
        n -= 1
        i += 1  
    
    return track_sort

def insertionsort(L, left = None, right = None, track_sort = set()): 
    '''
    Uses insertion sort to sort the list in place
    '''

    #Add insertionsort to the set
    track_sort.add("insertionsort")
    
    #Setting left and right equal to 0 and length of list if no change in parameter
    if left == None:
        left = 0
    if right == None:
        right = len(L) 
    
    #Insertion sort
    for j in range(left, right):
        key = L[j]
        i = j -1
        
        while i >=0 and key < L[i]:
            L[i +1] = L[i]
            i -= 1
        L[i+1] = key
    
    return track_sort

    
def quicksort(L, left = 0, right = None, depth = 0, track_sort = set()): 
    '''
    Uses a quicksort to sort a list in place. Best-max recursion depth should be log2(n) +1
    In the case were our recursive depth reaches 2 times the best-max recursion depth
    fall to mergesort  
    '''
    
    #Add quicksort to the set
    track_sort.add("quicksort")
    
    #Increment depth each recursive call
    depth +=1
    
    #Base case --> If no input for the right index, set it to the length of the list
    if right is None:
        right = len(L)
    
    #Base case --> If recursive depth is too deep switch to mergesort
    if depth >= 2*(log2(len(L)) +1):
        mergesort(L, track_sort)
    
    #Base case --> If the list is 16 or fewer items sort using insertion
    if right - left <= 16:
        #track_sort.add('insertionsort')
        insertionsort(L, left, right, track_sort)
    
    #Base case --> Smallest divisible part
    #Return the tracked set
    if right - left <= 1: 
        return track_sort

    #Set the pivot to be the last number of the list
    #Partition around the pivot
    pivot = right - 1
    i, j = left, right - 2          #Creating counters 

    #Pivot:
    while i < j:
        #Finding the first item bigger than the pivot
        while L[i] < L[pivot]:
            i += 1 
        #Finding the first item smaller than pivot
        while L[j] >= L[pivot] and i < j:       #Also have to have i < j to make sure there is no overlap
            j -= 1

        if i < j:
            #Swapping
            L[i], L[j] = L[j], L[i]    

    if L[i] >= L[pivot]:                        #Double checking the item is bigger than or equal the pivot
        #Placing pivot in the correct spot
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    
    #Recursively calling quicksort on the left and right halves
    quicksort(L, left, pivot, depth, track_sort)
    quicksort(L, pivot + 1, right, depth, track_sort)


def mergesort(L, track_sort = set()):
    '''
    Uses a mergesort to sort a list in place
    ''' 
    
    #Add mergesort to the set
    track_sort.add("mergesort")

    #Base case --> If the sublist is smaller 16 items, use insertionsort
    if len(L) <= 16:
        #track_sort.add('insertionsort')
        insertionsort(L, None, None, track_sort)
    
    #Base case --> Smallest divisible part
    if len(L) <= 1:
        return L
    
    #Finding the median
    median = len(L) // 2
    left = L[:median]
    right = L[median:]

    #Keep splitting up recursively
    left = mergesort(left, track_sort)
    right = mergesort(right, track_sort)

    #Zip up the sublists 
    
    #Variables to increment through
    i = 0                 
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i + j] = left[i]
            i += 1

        else:
            L[i + j] = right[j]
            j += 1

    #Since we are done comparing, we know the rest are in order so just add them on
    L[i + j:] = left[i:] + right[j:]

    #Return the tracked set
    return L
   
def magic_sort(L): 
    '''
    This sorts in place using a variety of different sorting algorithms to achieve the 
    optimal running time for sorting a list. 
    Keeps tracks of the sorting algorithms used and returns them as a set
    '''
    
    #Create an empty set to keep the algorithms in
    algorithms = set()
    
    #Use linearscan method to check for edge cases
    x = linear_scan(L)

    #See if any of the edge cases are hit and if so, use them and return that sorting method
    if x == "Use reverse sort":
        reverse_list(L, algorithms)
        return algorithms
    
    elif x == "Use insertion":
        insertionsort(L, None, None, algorithms) 
        return algorithms
    
    #If none of the edge cases are detected, use quicksort where the pivot is the last number
    else:
        quicksort(L, 0, None, 0, algorithms)
        return algorithms
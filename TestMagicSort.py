import unittest
import random
from HWs.hw7starter.Magic_Sort.MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort


def is_sorted(L):
    '''
    Returns True if list is sorted and False if list is not sorted
    '''
    return not any(L[i] > L[i + 1] for i in range(len(L)-1))


class Test_linear_scan(unittest.TestCase): 
    '''
    Tests the output of the linear scan.
    Looking for edge cases:
        1) List is already sorted
        2) At least 5 items are out of place
        3) The list is reverse sorted
    '''

    print("Testing the linear scan")

    def test_alread_sorted(self):
        '''
        Tests if a list is already sorted testing two lists
        '''
        #In exact order
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = linear_scan(L)
        self.assertEqual(x , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        #Missing some numbers in between but still sorted
        L1 = [2, 5, 8, 10, 12, 15]
        y = linear_scan(L1)
        self.assertTrue(y, [2, 5, 8, 10, 12, 15])
    
    def test_use_insertion(self):
        '''
        Tests if a list needs to use insertion sort based on edge case
        Testing a list with less than 5 out of place, more than 5 out of place, exactly 5 out of place
        '''
        #Less than 5 list
        L = [3, 2, 7, 2, 7, 8, 9, 10, 11, 12]
        x = linear_scan(L)
        self.assertEqual(x, "Use insertion")

        #More than 5 list
        L1 = [4, 6, 2, 8, 1, 0, 5, 7, 2, 9, 5, 8, 0, 11, 3]
        y = linear_scan(L1)
        self.assertEqual(y, None)

        #Exactly 5 list
        L2 = [6, 4, 7, 3, 8, 2, 9, 1, 10, 9]
        z = linear_scan(L2)
        self.assertEqual(z, None)
    
    def test_reverse(self):
        '''
        Tests if a list is reverse sorted by testing two lists
        '''
        #In exact reverse order 
        L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        x = linear_scan(L)
        self.assertEqual(x, "Use reverse sort")

        #Missing some numbers in between but still reverse sorted
        L1 = [20, 18, 14, 13, 11, 9, 5, 1, 0]
        y = linear_scan(L1)
        self.assertEqual(y, "Use reverse sort")
    
    def test_insertion_reverse(self):
        '''
        Tests that only returns use insertion when less than 5 is also valid
        '''
        #In reverse order with less than 5 out of order
        L = [20, 14, 10, 5, 1]
        x = linear_scan(L)
        self.assertEqual(x, "Use reverse sort")

        #In reverse order with exactly 5 out of order
        L1 = [24, 21, 18, 14, 12, 10]
        y = linear_scan(L1)
        self.assertEqual(y, "Use reverse sort")


class Test_reverse_list(unittest.TestCase): 
    '''
    Tests if the reverse_list function works
    '''
    
    print("Testing reverse sort")

    def test_reverse_list(self):
        '''
        Tests a variety of different reverse list to sort
        '''
        #In exact reverse order
        L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        #In reverse order but skipping a few
        L1 = [20, 14, 10, 5, 1]

        #In reverse order with some repeats
        L2 = [15, 12, 11, 10, 10, 9, 4, 2, 2]

        #In reverse order with all negatives
        L3 = [-1, -2, -3, -4, -5, -6, -7, -8]

        L0 = [L, L1, L2, L3]
        for list in L0:
            reverse_list(list)
            self.assertTrue(is_sorted(list))

class Test_insertionsort(unittest.TestCase): 
    '''
    Test that the insertion sort function works
    '''
    
    print("Testing insertion sort")

    def test_random_list(self):
        '''
        Tests lists with random inputs
        '''
        #A random list
        L = []
        for i in range(20):
            L.append(random.randint(0, 30))

        #A list with less than 5 out of place
        L1 = [90, 30, 2, 3, 11, 0, 5]

        #List with random numbers including negative numbers
        L2 = []
        for i in range(20):
            L2.append(random.randint(-30, 20))

        L0 = [L, L1, L2]
        for list in L0:
            insertionsort(list)
            self.assertTrue(is_sorted(list))


class Test_quicksort(unittest.TestCase): 
    '''
    Test that the insertion function works
    '''
    
    print("Testing quicksort")

    def test_random_list_good(self):
        '''
        Test lists with random inputs and good pivots 
        '''
        
        #A large list with a good pivot
        L = [17, 20, 32, 1, 2, 8, -3, 9, 3, 15, 21, 16]

        #A small list with a good pivot
        L1 = [3, 8, 2, 7, 4]

        L0 = [L, L1]
        for list in L0:
            quicksort(list)
            self.assertTrue(is_sorted(list))
    
    def test_random_list_bad(self):
        '''
        Tests lists with random inputs and bad pivots
        '''
        
        #A large list with bad pivot
        L = [20, 1, 8, 4, 5, 8, 3, 10, 14, 19, 11, 23, 9, 0, 2]
       
        #A small list with a bad pivot
        L1 = [9, 2, 5, 1, 8, 0]

        #Some negative numbers
        L2 = [-4, 5, 1, 0, -3, 8, 11, 12, 2]

        L0 = [L, L1, L2]
        for list in L0:
            quicksort(list)
            self.assertTrue(is_sorted(list))
        


class Test_mergesort(unittest.TestCase): 
    '''
    Test that the mergesort function works
    '''

    print("Testing mergesort")

    def test_random_list(self):
        '''
        Tests lists with random inputs for mergesort
        '''
        
        #A large list
        L = []
        for i in range(100):
            L.append(random.randint(0,200))

        #A small list
        L1 = []
        for i in range(10):
            L1.append(random.randint(0,20))

        #List with negative numbrs
        L2 = []
        for i in range(50):
            L2.append(random.randint(-50, 50))

        L0 = [L, L1, L2]
        for list in L0:
            mergesort(list)
            self.assertTrue(is_sorted(list))



class Test_magicsort(unittest.TestCase): 
    '''
    Tests that magic sort function
    '''

    print("Testing magicsort")
    
    def test_use_reverse(self):
        '''
        Makes sure magic sort returns a set with reverse_list in it
        '''

        #A list with some negative numbers
        L = [20, 15, 13, 11, 10, 5, 2, -1, -3]

        #An all negative list
        L1 = [-1, -3, -7, -8]

        L0 = [L, L1]
        for list in L0:
            self.assertEqual(magic_sort(list), {"reverse_list"})
            self.assertTrue(is_sorted(list))


    def test_insertion_only(self):
        '''
        Check that magic sort returns a set with insertionsort where only use 
        insertion sort on it
        '''

        #A small list 
        L = [19, 3, 1, 7]

        #List with some negative numbers
        L1 = [0, -2, 3, 6, 8, -1]

        #Random list less than or equal to the length of 16
        L2 = [10, 5, 1, 3, 6, 2, -4, -1, 0]

        L0 = [L, L1, L2]
        for list in L0:
            self.assertEqual(magic_sort(list), {"insertionsort"})
            self.assertTrue(is_sorted(list))
        

    def test_quick_insertion_merge(self):
        '''
        Check that magic sort returns a set with quicksort, insertionsort, mergesort
        when only those edge cases are hit
        '''

        #A list where reverse sorted except 1
        L = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 18, 19, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(magic_sort(L), {"quicksort", "insertionsort", "mergesort"})
        self.assertTrue(is_sorted(L))


    def test_quick_insertion(self):
        '''
        Check that magic sort returns a set with only quicksort and insertionsort 
        since it only hits the insertionsort edge case
        '''

        #List with negative
        L = [-5, 1, 6, 2, 7, 1, 0, 9, 2, -1, 0, 3, 2, 1, 7, 2, 4, 6, 2]

        #Small list all positive
        L1 = [20, 19, 2, 5, 1, 6, 3, 2, 6, 1, 8, 3, 2, 6, 2, 11, 13]

        L0 = [L, L1]
        for list in L0:
            self.assertEqual(magic_sort(list), {"quicksort", "insertionsort"})
            self.assertTrue(is_sorted(list))
        


unittest.main()
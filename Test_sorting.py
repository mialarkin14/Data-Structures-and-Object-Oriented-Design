import unittest
from HWs.hw6_starter.Sorting.sorting import find_zero, sort_halfsorted, bubble, selection, insertion
from HWs.hw6_starter.Sorting.TestHelpers import generate_halfsorted, is_sorted

# TODO: implement tests for sort_halfsorted

class Test_Empty_List(unittest.TestCase):
   def test_empty_list(self):
      '''
      This is a function that tests an edge case if the list is empty.
      '''
      
      # use an empty list to test that the return is -1
      print("Testing an empty list")
      L = []
      self.assertEqual(find_zero(L), -1)

class Test_SortHalfSorted(unittest.TestCase):
   def test_halfsorted_bubble(self): 
      '''
      Test that uses the halfsorted method to test if bubble sort correctly sorts and
      check if all the elements are the same to the original item
      '''
      
      # use sort_halfsorted(L, bubble) to test
      print("Testing bubble sort with different types of lists")
      
      #Simple test to check that bubble is sorting left to right
      L0 = [-9, 7, 2, -3, 3, 1, -2]
      bubble(L0, 1, 4)
      assert L0 == [-9, -3, 2, 7, 3, 1, -2]
      
      #Testing different patterns for a half-sorted list with placing zero at a random index
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        #Generating a half-sorted list
                        L, idx_zero = generate_halfsorted(n, idx_zero=None, pattern=pattern)
                        #Creating a deep copy of the random list
                        L2 = L[::]
                        sort_halfsorted(L, bubble)
                        #Asserting the bubble sort correctly sorts
                        self.assertTrue(is_sorted(L))
                        #Asserting the sorted list contains the same elements as the original list
                        self.assertCountEqual(L, L2)
      
      #Testing if all positive list
      for pattern in ['random', 'reverse']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        #Generating a half-sorted list
                        L, idx_zero = generate_halfsorted(n, idx_zero=0, pattern=pattern)
                        #Creating a deep copy of the random list
                        L2 = L[::]
                        sort_halfsorted(L, bubble)
                        #Asserting the bubble sort correctly sorts
                        self.assertTrue(is_sorted(L))
                        #Asserting the sorted list contains the same elements as the original list
                        self.assertCountEqual(L, L2)
      
      #Testing if all negative list
      for pattern in ['random', 'reverse']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        #Generating a half-sorted list
                        L, idx_zero = generate_halfsorted(n, idx_zero=len(L)-1, pattern=pattern)
                        #Creating a deep copy of the random list
                        L2 = L[::]
                        sort_halfsorted(L, bubble)
                        #Asserting the bubble sort correctly sorts
                        self.assertTrue(is_sorted(L))
                        #Asserting the sorted list contains the same elements as the original list
                        self.assertCountEqual(L, L2)

   


   def test_halfosrted_selection(self): 
      '''
      Test that uses the halfsorted method to test if the selection sort correctly sorts and
      check if all the elements are the same to the original item
      '''
      
      # use sort_halfsorted(L, selection) to test
      print("Testing selection sort with different types of lists")

      #Simple test to check that selection is sorting left to right
      L0 = [-3, 7, 1, 0, 3, -2, -1, 4, 2]
      selection(L0, 4, 8)
      assert L0 == [-3, 7, 1, 0, -2, -1, 3, 4, 2]
      
      #Testing different patterns for a half-sorted list with placing zero at a random index
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        #Generating a half-sorted list
                        L, idx_zero = generate_halfsorted(n, idx_zero=None, pattern=pattern)
                        #Creating a deep copy of the random list
                        L2 = L[::]
                        sort_halfsorted(L, selection)
                         #Asserting the selection sort correctly sorts
                        self.assertTrue(is_sorted(L))
                        #Asserting the sorted list contains the same elements as the original list
                        self.assertCountEqual(L, L2)

      #Testing if all positive list
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        #Generating a half-sorted list
                        L, idx_zero = generate_halfsorted(n, idx_zero=0, pattern=pattern)
                        #Creating a deep copy of the random list
                        L2 = L[::]
                        sort_halfsorted(L, selection)
                        #Asserting the selection sort correctly sorts
                        self.assertTrue(is_sorted(L))
                        #Asserting the sorted list contains the same elements as the original list
                        self.assertCountEqual(L, L2)
      
      #Testing if all negative list
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        #Generating a half-sorted list
                        L, idx_zero = generate_halfsorted(n, idx_zero=len(L)-1, pattern=pattern)
                        #Creating a deep copy of the random list
                        L2 = L[::]
                        sort_halfsorted(L, selection)
                        #Asserting the selection sort correctly sorts
                        self.assertTrue(is_sorted(L))
                        #Asserting the sorted list contains the same elements as the original list
                        self.assertCountEqual(L, L2)
      
   def test_halfsorted_insertion(self): 
      '''
      Test that uses the halfsorted method to test if the insertion sort correctly sorts and
      check if all the elements are the same to the original item
      '''
      
      # use sort_halfsorted(L, insertion) to test
      print("Testing insertion sort with different types of lists")

      #Simple test to check that insertion sort is sorting left to right
      L0 = [0, -5, 2, 7, 9, 6, -4, 10, 7, 1]
      insertion(L0, 2, 7)
      assert L0 == [0, -5, -4, 2, 6, 7, 9, 10, 7, 1]
      
      #Testing different patterns for a half-sorted list with placing zero at a random index
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        #Generating a half-sorted list
                        L, idx_zero = generate_halfsorted(n, idx_zero=None, pattern=pattern)
                        #Creating a deep copy of the random list
                        L2 = L[::]
                        sort_halfsorted(L, insertion)
                        #Asserting the insertion sort correctly sorts
                        self.assertTrue(is_sorted(L))
                        #Asserting the sorted list contains the same elements as the original list
                        self.assertCountEqual(L, L2)
      
      #Testing if all positive list
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        #Generating a half-sorted list
                        L, idx_zero = generate_halfsorted(n, idx_zero=0, pattern=pattern)
                        #Creating a deep copy of the random list
                        L2 = L[::]
                        sort_halfsorted(L, insertion)
                        #Asserting the insertion sort correctly sorts
                        self.assertTrue(is_sorted(L))
                        #Asserting the sorted list contains the same elements as the original list
                        self.assertCountEqual(L, L2)
      
      #Testing if all negative list
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        #Generating a half-sorted list
                        L, idx_zero = generate_halfsorted(n, idx_zero=len(L)-1, pattern=pattern)
                        #Creating a deep copy of the random list
                        L2 = L[::]
                        sort_halfsorted(L, insertion)
                        #Asserting the insertion sort correctly sorts
                        self.assertTrue(is_sorted(L))
                        #Asserting the sorted list contains the same elements as the original list
                        self.assertCountEqual(L, L2)
      

# Test provided for you
class Test_FindZero(unittest.TestCase):
   def test1_allLengthsAllIndices(self):
      '''Tests find_zero for every possible index, for lists from 1 to 100 items

         Lists
         -----
            '-' and '+' denote negative and positive ingeters, respectively
                                 idx_zero
            n = 1                
               L = [0]           0

            n = 2
               L = [0, +]        0
               L = [-, 0]        1

            n = 3                
               L = [0, +, +]     0
               L = [-, 0, +]     1  
               L = [-, -, 0]     2

            n = 4
               L = [0, +, +, +]  0
               L = [-, 0, +, +]  1
               L = [-, -, 0, +]  2
               L = [-, -, -, 0]  3
            ...
            n = 100
               L = [0, ..., +]   0
               ...
               L = [-, ..., 0]   99
      '''

      # note the use of `subTest`. These all count as 1 unittest if they pass,
      # but all that fail will be displayed independently
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

unittest.main()


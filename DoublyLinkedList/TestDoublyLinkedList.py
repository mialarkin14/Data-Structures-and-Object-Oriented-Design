from HWs.hw4_starter.DoublyLinkedList.DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        '''
        Tests if an item is in the doublylinkedlist using the magic method __contains__
        '''
        
        print("Testing if an item is in the list")
        #Testing two double link list
        dll = DLL(range(0, 10, 2))      #Even values up to 10 (not including)
        dll2 = DLL(range(0, 15, 3))     #Factors of 3 up to 15 (ot including)
        self.assertEqual(4 in dll, True)
        self.assertEqual(5 in dll, False)
        self.assertEqual(10 in dll, False)
        self.assertEqual(3 in dll2, True)
        self.assertEqual(15 in dll2, False)
        
        #Adds an item as first value and remove it. Check if in list
        dll.add_first(12)
        self.assertEqual(12 in dll, True)
        dll.remove_first()
        self.assertEqual(12 in dll, False)
        dll2.add_first(15)
        self.assertEqual(15 in dll2, True)
        dll2.remove_first()
        self.assertEqual(15 in dll2, False)
        
        #Adds an item as the last value and remove it. Check if in list
        dll.add_last(14)
        dll.add_last(16)
        dll.remove_last()
        self.assertEqual(16 in dll, False)
        dll2.add_last(2)
        dll2.remove_last()
        self.assertEqual(2 in dll2, False)

        #Keeps removing until there is only one item in the list. Check if in list
        for i in range(5):
            dll.remove_last()
        self.assertEqual(0 in dll, True)

        #Check no items are in the list
        dll.remove_last()
        self.assertEqual(0 in dll, False)

    def test_neighbors(self):
        '''
        Tests if neighbors returns the previous item and the next item
        '''
        
        print("Testing if the neighbors of an item are correct")
        #Testing a double linked list with all values between 1-15, including 15
        dll = DLL(range(0, 16, 1))
        x = dll.neighbors(5)
        self.assertEqual(x, (4, 6))

        #Testing edge cases of head and tail
        y = dll.neighbors(15)
        self.assertEqual(y, (14, None))
        z = dll.neighbors(0)
        self.assertEqual(z, (None, 1))

        #Testing if the item is not in the dll, a runtime error will be raised
        try:
            dll.neighbors(16)
        except:
            RuntimeError

    def test_remove_item(self):
        '''
        Test if remove_node removes the item and correctly stitches the previous and next node
        together
        '''

        print("Testing the removal of an item based on item name")
        #Testing a double linked list with every 5th value between 0 - 35, excluding 35
        dll = DLL(range(0, 35, 5))
        dll.remove_node(15)
        x = dll.neighbors(10)
        self.assertEqual(x, (5, 20))
        
        #Testing that the tail is removed and the previous item of the original tail becomes the new tail
        dll.remove_node(30)
        y = dll.neighbors(25)
        self.assertEqual(y, (20, None))

        #Testing that the head is removed and the next item of the original head becomes the new head
        dll.remove_node(0)
        z = dll.neighbors(5)   
        self.assertEqual(z, (None, 10))     

        #Testing that if trying to remove an item not in dll
        try:
            dll.remove_node(35)
        except:
            RuntimeError

        #Testing that the length decreases, the item is returned, and the item is removed from dictionary
        self.assertEqual(len(dll), 4)
        self.assertEqual(dll.remove_node(5), 5)
        self.assertEqual(5 in dll, False)

unittest.main()

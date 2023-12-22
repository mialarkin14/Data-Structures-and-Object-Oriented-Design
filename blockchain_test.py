import unittest
from HWs.hw8_starter.Blockchain.hashmap import HashMap as hm
from HWs.hw8_starter.Blockchain.blockchain import Transaction, Block, Ledger, Blockchain

class Test_Hash_Map(unittest.TestCase):
    '''
    Class that tests HashMap ADT which is a wrapper of the 
    Python dictionary
    '''
    
    print("Testing HashMap...")

    def test_contains(self):
        '''
        Creates an instance of Hashmap ADT and checks if item in map
        '''
        dict0 = hm()
        self.assertFalse(0 in dict0)
        #Adds 'Mia'
        dict0["Mia"] = 500
        self.assertTrue("Mia" in dict0)
        #Removes 'Mia'
        dict0.remove("Mia")
        self.assertFalse("Mia" in dict0)

        #New dictionary
        dict1 = hm()
        dict1["Bob"] = 700
        dict1["Sarah"] = 350
        dict1["Tom"] = 700
        dict1.remove("Tom")
        self.assertTrue("Bob" in dict1)
        self.assertTrue("Sarah" in dict1)
        self.assertFalse("Tom" in dict1)

    def test_changing_value(self):
        '''
        Creates an instance of Hashmap ADT and checks if a value gets updated
        '''
        dict0 = hm()
        dict0["Emily"] = 100
        self.assertEqual(dict0["Emily"], 100)
        #Changes 'Emily' value
        dict0["Emily"] = 275
        self.assertEqual(dict0["Emily"], 275)
        
        #New dictionary 
        dict1 = hm()
        dict1["Buffy"] = 27
        self.assertEqual(dict1["Buffy"], 27)
        #Changes 'Buffy' value
        dict1["Buffy"] = 347
        self.assertEqual(dict1["Buffy"], 347)
    
    print("✅")

class Test_Transaction(unittest.TestCase):
    '''
    Class that tests Transaction class that holds the sender user, reciever user
    and the amount of HuskyCoin sent 
    '''

    print("Testing Transaction...")

    def test_transaction(self):
        '''
        Creates an instance of Transaction and tests that passed elements are correct
        '''
        trans1 = Transaction("Emily", "Mia", 100)
        self.assertEqual(trans1.from_user, "Emily")
        self.assertEqual(trans1.to_user, "Mia")
        self.assertEqual(trans1.amount, 100)
        #Checking string repr
        self.assertEqual(repr(trans1), "(Sender: Emily, Reciever: Mia, Amount: 100 HuskyCoin)")

        #New transaction
        trans2 = Transaction("John", "Serina", 500)
        self.assertEqual(trans2.from_user, "John")
        self.assertEqual(trans2.to_user, "Serina")
        self.assertEqual(trans2.amount, 500)
        #Checking string repr
        self.assertEqual(repr(trans2), "(Sender: John, Reciever: Serina, Amount: 500 HuskyCoin)")

    print("✅")

class Test_Block(unittest.TestCase):
    '''
    Class that test the Block class that holds a list of transactions
    '''

    print("Testing Block...")

    def test_adding_transaction(self):
        '''
        Creates an instance of block and keeps adding, 
        checking that it's added to the list of transactions
        '''
        block1 = Block()
        #Creating a transaction
        trans1 = ("Milly", "Sam", 720)
        block1.add_transaction(trans1)
        self.assertIn(trans1, block1.transactions)
        #Creating a transaction
        trans2 = ("Nick", "Max", 800)
        block1.add_transaction(trans2)
        self.assertIn(trans2, block1.transactions)
        #Creating a transaction
        trans3 = ("Phlip", "Hailey", 200)
        block1.add_transaction(trans3)
        self.assertIn(trans3, block1.transactions)

    def test_string_of_trans(self):
        '''
        Creates an instance of block and adds transactions.
        Checks string represenation of block
        '''
        block1 = Block()
        #Creating a transaction
        trans1 = ("Clark", "Sky", 50)
        block1.add_transaction(trans1)
        #Creating a transaction
        trans2 = ("Ann", "Caitlin", 136)
        block1.add_transaction(trans2)
        #Creating a transaction
        trans3 = ("Summer", "John", 853)
        block1.add_transaction(trans3)
        self.assertEqual(repr(block1), "Transactions: [('Clark', 'Sky', 50), ('Ann', 'Caitlin', 136), ('Summer', 'John', 853)]")
    
    print("✅")


class Test_Ledger(unittest.TestCase):
    '''
    Class that tests the Ledger class that checks if sufficient funds,
    allows deposits, and allows transfers
    '''
    
    print("Testing Ledger...")
    
    def test_has_funds(self):
        '''
        Creates an instance of Ledger and tests if a user has funds 
        '''
        #Edge case try-except user not there
        ledger1 = Ledger()
        try:
            ledger1.has_funds("Mia", 100)
        except:
            "Mia is not in Ledger"
        
        #Remotely accessing hashmap for sole purpose of testing
        ledger1._hashmap["Mia"] = 100
        self.assertTrue(ledger1.has_funds("Mia", 100))
        ledger1._hashmap["Squid"] = 57
        self.assertFalse(ledger1.has_funds("Squid", 100))
        ledger1._hashmap["Rachel"] = 540
        self.assertFalse(ledger1.has_funds("Rachel", 1000))

    def test_deposit(self):
        '''
        Creates an instance of Ledger and tests the deposit method 
        '''
        #Edge case try-except user not in ledger
        ledger1 = Ledger()
        try:
            ledger1.deposit("Timmy", 729)
        except:
            "Timmy is not in Ledger"
        
        #Remotely accessing hashmap for sole purpose of testing 
        ledger1._hashmap["Timmy"] = 0
        ledger1.deposit("Timmy", 476)
        self.assertEqual(ledger1._hashmap["Timmy"], 476)
        ledger1._hashmap["Evan"] = 0
        ledger1.deposit("Evan", 562)
        self.assertEqual(ledger1._hashmap["Evan"], 562)
    
    def test_transfer(self):
        '''
        Creates an instance of Ledger and tests the transfer method
        '''
        #Edge case try-except user no in ledger
        ledger1 = Ledger()
        try:
            ledger1.transfer("Felix", 20)
        except:
            "Felix is not in Ledger"

        #Remotely accessing hashmap for sole purpose of testing 
        ledger1._hashmap["Felix"] = 350
        ledger1.transfer("Felix", 20)
        self.assertEqual(ledger1._hashmap["Felix"], 330)
        ledger1._hashmap["Johnny"] = 182
        ledger1.transfer("Johnny", 149)
        self.assertEqual(ledger1._hashmap["Johnny"], 33)
    
    def test_repr(self):
        '''
        Uses previous tests, transfer and deposit, to write a ledger
        '''
        ledger1 = Ledger()
        
        #Remotely accessing hashmap for sole purpose of testing 
        ledger1._hashmap["Timmy"] = 0
        ledger1.deposit("Timmy", 476)
        self.assertEqual(ledger1._hashmap["Timmy"], 476)
        ledger1._hashmap["Evan"] = 0
        ledger1.deposit("Evan", 562)
        self.assertEqual(ledger1._hashmap["Evan"], 562)
        ledger1._hashmap["Felix"] = 350
        ledger1.transfer("Felix", 20)
        self.assertEqual(ledger1._hashmap["Felix"], 330)
        ledger1._hashmap["Johnny"] = 182
        ledger1.transfer("Johnny", 149)
        self.assertEqual(ledger1._hashmap["Johnny"], 33)
        #Check repr of ledger
        self.assertEqual(repr(ledger1), "Ledger: {'Timmy': 476, 'Evan': 562, 'Felix': 330, 'Johnny': 33}")
    
    print("✅")

class Test_Blockchain(unittest.TestCase):
    '''
    Class that tests the Blockchain class that has an add block method,
    validate chain method, and a root block   
    '''
    
    print("Testing Blockchain...")
    
    def test_add_block(self):
        '''
        Creates an instance of Blockchain and block along with a starter block 
        '''
        bc1 = Blockchain()
        block1 = Block()
        #Creating transactions
        trans1 = Transaction("Mike", "Ann", 200)
        trans2 = Transaction("Mike", "Ann", 50)
        trans3 = Transaction("Bob", "Jill", 500)
        #Setting up a balance of 1000 for users
        bc1.distribute_mining_reward("Mike")
        bc1.distribute_mining_reward("Ann")
        bc1.distribute_mining_reward("Bob")
        #Adding transactions
        block1.add_transaction(trans1)
        block1.add_transaction(trans2)
        block1.add_transaction(trans3)
        #Adding block and checking equal
        bc1.add_block(block1)
        self.assertEqual(repr(bc1._bc_ledger), "Ledger: {'ROOT': 996999, 'Mike': 750, 'Ann': 1250, 'Bob': 500, 'Jill': 500}")
        self.assertTrue(bc1.add_block(block1))
        #Transaction that can't make
        trans4 = Transaction("Mike", "Ann", 5000)
        block1.add_transaction(trans4)
        try:
            bc1.add_block(block1)
        except:
            "Mike does not have enough funds to send 5000 to Ann"

    def test_validate_chain(self):
        '''
        Creates an instance of blockchain and multiple blocks to validate the block chain
        '''
        bc1 = Blockchain()
        block1 = Block()
        block2 = Block()
        block3 = Block()
        #Creating transactions
        trans1 = Transaction("Mike", "Ann", 200)
        trans2 = Transaction("Mike", "Ann", 50)
        trans3 = Transaction("Bob", "Jill", 500)
        trans4 = Transaction("Mia", "Astrid", 63)
        trans5 = Transaction("Milo", "Reed", 128)
        #Setting up a balance of 1000 for users
        bc1.distribute_mining_reward("Mike")
        bc1.distribute_mining_reward("Ann")
        bc1.distribute_mining_reward("Bob")
        bc1.distribute_mining_reward("Mia")
        bc1.distribute_mining_reward("Milo")
        #Adding transactions
        block1.add_transaction(trans1)
        block1.add_transaction(trans2)
        block2.add_transaction(trans3)
        block2.add_transaction(trans4)
        block3.add_transaction(trans5)
        #Adding block 
        bc1.add_block(block1)
        bc1.add_block(block2)
        bc1.add_block(block3)

        #Assert that the blockchain is valid
        self.assertEqual(bc1.validate_chain(), [])
        
        #Tamper with the block and assert
        tamper_transaction = Transaction("Mike", "Ann", 100)
        block1.add_transaction(tamper_transaction)
        self.assertEqual(bc1.validate_chain(), ["[(Sender: Mike, Reciever: Ann, Amount: 200 HuskyCoin), (Sender: Mike, Reciever: Ann, Amount: 50 HuskyCoin), (Sender: Mike, Reciever: Ann, Amount: 100 HuskyCoin)]"])

    print("✅")

unittest.main()
from HWs.hw8_starter.Blockchain.hashmap import HashMap as Map
class Transaction():
    '''
    Class that holds a single transaction
    '''
    def __init__(self, from_user, to_user, amount):
        '''
        Contains a single transaction of HuskyCoin with info on who sends the money,
        who recieves the money, and the amount of money
        '''
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount
        
    def __repr__(self):
        '''
        Returns a string representation of a transaction
        '''
        return f"(Sender: {self.from_user}, Reciever: {self.to_user}, Amount: {self.amount} HuskyCoin)" 
    
class Block():
    '''
    Class that holds multiple transactions 
    '''
    def __init__(self, transactions=None, previous_block = None):
        '''
        Defines variables:
            - If there are no transactions we set transactions to an empty list
            - Have hash of previous block as a parameter 
        '''
        
        self.transactions = transactions
        self.previous_block = previous_block
        if self.transactions == None:
            self.transactions = []
            

    def add_transaction(self, transaction):
        '''
        Adds a transaction to the list of transactions that the block holds
        '''
        #Create an instance of transation and append it to the list as a tuple
        #transaction = Transaction(sender, reciever, money)
        #tuple = (transaction.from_user,transaction.to_user,transaction.amount)
        self.transactions.append(transaction)
    
    def __repr__(self):
        '''
        Returns a string represenation of the transactions in a block
        '''
        return f"Transactions: {self.transactions}"
    
    def __hash__(self):
        '''
        Sets the hash of a block to be the built-in python hash of the 
        string of the transaction list
        '''
        #Gets the string of the transactions
        x = repr(self.transactions)
        #Sets the hash of the block to the length of the string
        return hash(x)
    
    def __eq__(self, other):
        return hash(self) == hash(other)

class Ledger(): 
    '''
    The ledger keeps tracks of the current balance of a user
    '''
    def __init__(self):
        '''
        Defines variables using an instance of Hashmap ADT
        '''
        self._hashmap = Map()
    
    def has_funds(self, user, amount):
        '''
        Checks if the user has funds or not
        '''
        #First checks if the user is in the hashmap, if they are not
        #return False
        if user not in self._hashmap:
            False
        #Gets the balance of the user from the hashmap 
        balance = self._hashmap[user]
        #Returns true if the user has that amount of funds or more and false if not
        return balance >= amount

    def deposit(self, user, amount):
        '''
        Adds Huskycoins to a user
        '''
        #First check if the user is in the hashmap, if not, return False
        if user not in self._hashmap:
            self._hashmap[user] = 0
        #Adds the amount to the user's balance
        self._hashmap[user] = self._hashmap[user] + amount
    
    def transfer(self, user, amount):
        '''
        Subtracts Huskycoins from a user
        '''
        #First check if the user is in the hashmap, if not, return False
        if user not in self._hashmap:
            self._hashmap[user] = 0
        #Subtracts the amount to the user's balance
        self._hashmap[user] = self._hashmap[user] - amount

    def __repr__(self):
        '''
        Returns a string representation of the ledger
        '''
        return f"Ledger: {self._hashmap}"

class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        '''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    def add_block(self, block):
        '''
        Adds a block and adds/ subtracts appropriate funds 
        '''
        #Stores hash of previous block
        block.previous_block = hash(self._blockchain[-1])
        
        #Update ledger by getting block's transactions and looping through
        for trans in block.transactions:
            from_user = trans.from_user
            to_user = trans.to_user
            amount = trans.amount
            #Checking if sending user has funds
            if self._bc_ledger.has_funds(from_user, amount) == True:
                #Subtract funds from sending user and add to recieving user
                self._bc_ledger.transfer(from_user, amount)  
                self._bc_ledger.deposit(to_user, amount) 
            
            else:
                #Raise an error saying no funds
                raise ValueError(f"{from_user} does not have enough funds to send {amount} to {to_user}") 
        #Add the block 
        self._blockchain.append(block)

        #Return true or false if block was successfully added
        if block in self._blockchain:
            return True
        return False

    def validate_chain(self):
        '''
        Checks if a block has been tampered with
        '''
        i = 1
        tamp_blocks = []
        #Loops through each block
        while i <= len(self._blockchain)-1:
            #Check if hash is correct
            if self._blockchain[i].previous_block != hash(self._blockchain[i-1]):
                tamp_blocks.append(self._blockchain[i-1])
            i += 1
        #Return tampered blocks   
        return tamp_blocks 

    def __repr__(self):
        '''
        Returns a string representation of the blockchain
        '''
        return f"Blockchain: {self._blockchain}"
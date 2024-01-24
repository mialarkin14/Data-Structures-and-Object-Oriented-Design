class HashMap:
    def __init__(self):
        '''
        Defines our map to be a wrapper method of the dictionary function
        '''
        self.map = {}

    def __contains__(self, user):
        '''
        Returns true if user already exists in our mapping and false otherwise
        '''
        if user in self.map:
            return True
        return False
    
    def __setitem__(self, user, balance):
        '''
        Adds key:value pair to HashMapping or updates the kay value if it already exists
        '''
        self.map[user] = balance

    def __getitem__(self, user):
        '''
        Takes in a key and returns the value associated with that key if no key exists, 
        raise a KeyError
        '''
        if user in self.map:
            return self.map[user]
        raise KeyError(f"{user} is not in Ledger")
    
    def remove(self, user):
        '''
        Removes the key:value pair from the mapping. If no key exists, raise a KeyError
        '''
        self.map.pop(user)
    
    def __len__(self):
        '''
        Gets the length of the dictionary
        '''
        return len(self.map)
    
    def __repr__(self):
        '''
        Creates a string represenation of Hashmap
        '''
        return str(self.map)


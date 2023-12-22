class Card:
    '''
    A class that takes in a card value and suit
    Through methods in the class, you can see the card, determine if a card is less than another 
    based on alphabetical suit first and then value, or see if cards are equal to each other
    '''
    def __init__(self, value, suit):
        #Defines instance variables: value and suit
        self.value = value
        self.suit = suit

    def __repr__(self):
        #Returns a card showing in Card(value of suit) form
        return f"Card({self.value} of {self.suit})"

    def __lt__(self, other):
        #Defines is one card is less than another 
        return (self.suit, self.value) < (other.suit, other.value)

    def __eq__(self, other):
        #Defines if one card is equal to another
        return (self.suit, self.value) == (other.suit, other.value)

class Deck:
    '''
    A class that takes in a list of values and suits and then adds them to a list.
    Through methods in the class, you can see the length of the deck, show the deck as a string,
    sort the deck in order of suits and then number, shuffle the deck into a random order, and draw a card from the deck 
    '''
    
    def __init__(self, values = [2,1,3,4,5,6,7,8,9,10,11,12,13], suits = ["diamonds", "clubs", "hearts", "spades"]):
        #Defines instance variables: values is automatically set to 1-13 unless changed, suits is automatically set to
        #clubs, diamonds, hearts, and spades unless specified otherwise in call, card_list is empty 
        self.values = values
        self.suits = suits
        self.card_list = []

        #Takes in each given value and suit and assigns it to a card. Adds it to the card_list
        for val in self.values:
            for suit in self.suits:
                self.card_list.append(Card(val, suit))

    def __len__(self):
        #Magic method that returns the length of the deck 
        return len(self.card_list)

    def __repr__(self):
        #Magic method that returns a string of the deck
        return f"Deck: {self.card_list}"
    
    def sorts(self):
        #Method that sorts the deck in order of suit and number
        self.card_list.sort()
        return self.card_list

    def shuffle(self):
        #Method that shuffles the cards in a random order
        import random
        random.shuffle(self.card_list)
        return self.card_list

    def draw_top(self):
        #Method that takes the last card as the top card and removes it. If the deck is empty, raise a RuntimeError
        x = len(self.card_list)
        if x != 0:
            return repr(self.card_list.pop(x-1))
        else:
            raise RuntimeError ("Cannot draw from empty Deck")

class Hand(Deck):
    '''
    Class that creates a hand of cards and is able to sort them, find the amount of cards, 
    return the cards in a string and play a card
    '''
    def __init__(self, card_list = []):
        #Defines instance variable card list 
        Deck.__init__(self, values = [2,1,3,4,5,6,7,8,9,10,11,12,13], suits = ["diamonds", "clubs", "hearts", "spades"])
        self.card_list = card_list

    def __repr__(self):
        #Returns the hand as a string using a magic method
        return f"Hand: {self.card_list}"

    def play_card(self, card):
        #Removes the card from the deck and then returns the card. If the card is not in the deck, raise a RuntimeError 
        self.card = card
        if self.card in self.card_list:
            self.card_list.remove(self.card)
            return repr(self.card)
        else:
            raise RuntimeError (f"Attempt to play {self.card} that is not in the Hand")
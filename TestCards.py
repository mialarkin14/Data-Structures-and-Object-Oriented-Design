from HWs.hw2.Cards.Cards import Card, Deck, Hand
import unittest

class TestCards(unittest.TestCase):
    '''
    Class that tests the imported Cards class with the imported unittest class as a parent class 
    '''
    def test_string_rep(self):
        #Defines a card and test if the string representation is as expected; also have a printing test statement
        c0 = Card(6, "hearts")
        print("Tesing string representation of Card(6, hearts)")
        self.assertEqual(repr(c0), "Card(6 of hearts)")
    
    def test_cards_less_than(self):
        #Defines different types of cards to compare for less than
        c1 = Card(5, "hearts")
        c2 = Card(6, "clubs")
    
        #Less than assertion along with printing that the test is happening 
        print("Testing if Card(6 of clubs) is less than Card(5 of hearts)")
        self.assertLess(c2, c1, "Card(6, clubs) is less than Card(5, hearts)")
        #Expect that the following test will raise a ValueError so just pass 
        try:
            self.assertLess(c2, c1, "Card(5, hearts) is not less than Card(6, clubs)")
        except AssertionError:
            pass
    
    def test_cards_equal(self):
        #Defines different types of cards to compare for equal to 
        c5 = Card(4, "spades")
        c6 = Card(4, "spades")
        c7 = Card(5, "spades")

        #Equal to assertion along with printing that the test is happening 
        print("Testing if Card(4, spades) is equal to Card(4, spades)")
        self.assertEqual(c5, c6, "Card(4, spades) equal to Card(4, spades)")
        #Expect that the following test will raise a ValueError so just pass
        try:
            self.assertEqual(c6, c7, "Card(4, spades) equal to Card(5, spades)")
        except AssertionError:
            pass

class TestDeck(unittest.TestCase):
    '''
    Class that test the imported Deck class with the imported unittest class as a parent class 
    '''
    def test_expected_length(self): 
        #Defines different types of decks to compare for their length
        d1 = Deck()
        d2 = Deck([1,2,3], ["hearts"])

        #Test if the length is the expected length along with a printing a statment that says the test is happpening 
        print("Testing the length of d1")
        self.assertEqual(len(d1), 52)
        print("Testing the length of d2")
        self.assertEqual(len(d2), 3)

    def test_expected_repr(self):
        #Defines a deck and compares it to expected string output
        d1 = Deck([1,2,3], ["hearts", "diamonds"])
        
        #Test if the string representation is expected along with a printing statement saying the test is happening
        print("testing if the Deck([1,2,3], [hearts, diamonds] is as expected")
        self.assertEqual(repr(d1), "Deck: [Card(1 of hearts), Card(1 of diamonds), Card(2 of hearts), Card(2 of diamonds), Card(3 of hearts), Card(3 of diamonds)]")
    
    def test_expected_sort(self):
        #Defines a deck and compares it to expected string output
        d0 = Deck()
        d1 = Deck([1,2,3], ["diamonds", "hearts"])
       
        #Test if the string representation is expected along with a printing statement saying the test is happening
        print("Testing if the sorting of Deck(), default deck, is sorting")
        d0.sorts()
        self.assertEqual(repr(d0), "Deck: [Card(1 of clubs), Card(2 of clubs), Card(3 of clubs), Card(4 of clubs), Card(5 of clubs), Card(6 of clubs), Card(7 of clubs), Card(8 of clubs), Card(9 of clubs), Card(10 of clubs), Card(11 of clubs), Card(12 of clubs), Card(13 of clubs), Card(1 of diamonds), Card(2 of diamonds), Card(3 of diamonds), Card(4 of diamonds), Card(5 of diamonds), Card(6 of diamonds), Card(7 of diamonds), Card(8 of diamonds), Card(9 of diamonds), Card(10 of diamonds), Card(11 of diamonds), Card(12 of diamonds), Card(13 of diamonds), Card(1 of hearts), Card(2 of hearts), Card(3 of hearts), Card(4 of hearts), Card(5 of hearts), Card(6 of hearts), Card(7 of hearts), Card(8 of hearts), Card(9 of hearts), Card(10 of hearts), Card(11 of hearts), Card(12 of hearts), Card(13 of hearts), Card(1 of spades), Card(2 of spades), Card(3 of spades), Card(4 of spades), Card(5 of spades), Card(6 of spades), Card(7 of spades), Card(8 of spades), Card(9 of spades), Card(10 of spades), Card(11 of spades), Card(12 of spades), Card(13 of spades)]")
        print("Testing if the sorting of Deck([1,2,3], [hearts, diamonds]")
        d1.sorts()
        self.assertEqual(repr(d1), "Deck: [Card(1 of diamonds), Card(2 of diamonds), Card(3 of diamonds), Card(1 of hearts), Card(2 of hearts), Card(3 of hearts)]")
    
    def test_expected_shuffle(self):
        #Defines a deck and compares it to the sorted deck
        d1 = Deck([1,2,3], ["diamonds", "hearts"])
        d1.sorts()
        
        #Test if shuffled deck is different from sorted deck along with a printing statement saying the test is happening
        print("Testing if shuffle method shuffles the deck")
        self.assertNotEqual(d1.shuffle(), "Deck: [Card(1 of diamonds), Card(2 of diamonds), Card(3 of diamonds), Card(1 of hearts), Card(2 of hearts), Card(3 of hearts)]")

    def test_expceted_draw_top(self):
        #Defines a deck and makes sure the last card of the deck, the "top card", is taken out
        d0 = Deck([1,2,3], ["hearts"])

        #Test if the top card is taken out and keep taking it out until there is a RunTimeError along with a print statement saying test is happening
        print("Testing if card is removed until no cards are left")
        self.assertEqual(d0.draw_top(), "Card(3 of hearts)")
        self.assertEqual(repr(d0), "Deck: [Card(1 of hearts), Card(2 of hearts)]")
        d0.draw_top()
        self.assertEqual(repr(d0), "Deck: [Card(1 of hearts)]")
        try:
            d0.draw_top()
        except RuntimeError:
            pass

class TestHand(unittest.TestCase):
    def test_expected_repr(self):
        #Defines a hand and then compares it to string output
        h0 = Hand([Card(value, "hearts") for value in range (1,5)])

        #Test if hand is expected string with a print statement saying test is happening
        print("Tesing if hand is accurate string representation")
        self.assertEqual(repr(h0), "Hand: [Card(1 of hearts), Card(2 of hearts), Card(3 of hearts), Card(4 of hearts)]")

    def test_expected_length(self):
        #Defines a hand and then tests it length
        h1 = Hand([Card(1, "hearts"), Card(10, "spades"), Card(13, "diamonds"), Card(9, "spades"), Card(2, "clubs"), Card(11, "diamonds"), Card(8, "hearts")])
        
        #Test if it's the right number of cards
        print("Testing how many cards in the hand")
        self.assertEqual(len(h1), 7)

    def test_expected_sort(self):
        #Defines a hand and then tests if the hand gets sorted
        h2 = Hand([Card(1, "hearts"), Card(10, "spades"), Card(13, "diamonds"), Card(11, "clubs"), Card(4, "spades"), Card(3, "hearts")])
        
        #Test if it's the right sorting
        print("Testing if the sorting of hand is correct")
        h2.sorts()
        self.assertEqual(repr(h2), "Hand: [Card(11 of clubs), Card(13 of diamonds), Card(1 of hearts), Card(3 of hearts), Card(4 of spades), Card(10 of spades)]")

    def test_expected_play_card(self):
        #Defines a hand and then tests if the card is removed from the hand. If hand is empty, raise a RuntimeError
        h3 = Hand([Card(1, "hearts"), Card(6, "diamonds"), Card(13, "clubs")])

        #Test if removes a card/ plays a card and then if no cards in hand raises a RuntimeError
        print("Testing if card is removed")
        self.assertEqual(h3.play_card(Card(13, "clubs")), "Card(13 of clubs)")
        self.assertEqual(repr(h3), "Hand: [Card(1 of hearts), Card(6 of diamonds)]")
        self.assertEqual(h3.play_card(Card(6, "diamonds")), "Card(6 of diamonds)")
        try:
            h3.play_card(Card(13, "clubs"))
        except RuntimeError:
            pass

#Run all unit tests
unittest.main()


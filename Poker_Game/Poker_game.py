# POKER GAME
import random

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return f"{self.suit} --> {self.value}"
    
    
class Deck:
    def __init__(self):
        
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]
        
        self.cards = [Card(suit, value) for suit in suits for value in values]
        
    def __repr__(self):
        return "Cards left " + str(len(self.cards))
    
    
    def shuffle(self):
        if len(self.cards) < 52:
            print("Sorry ! all the cards should be shuffled")
            
        else:
            random.shuffle(self.cards)
        return self.cards
            
    def deal(self):
        if len(self.cards) == 0:
            print("All the cards are dealt")
        else:
            return self.cards.pop()
        
        
deck = Deck()
deck.shuffle()
print(deck.deal())
print(deck.deal())
print(deck)
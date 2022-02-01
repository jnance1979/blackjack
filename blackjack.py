import random

# values = { 1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, 11 : 11, 12 : 12, 13 : 13}

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f'{self.value} of {self.suit}'

class Deck:
    def __init__(self):
        self.deck = []
        self.create_cards()

    def create_cards(self):
        for s in ['Diamonds', 'Clubs', 'Spades', 'Hearts']:
            for v in range(1, 14):
                card1 = Card(v, s)
                self.deck.append(card1)

x = Deck()

def deal_card():
    pick = (random.choice(x.deck))
    x.deck.remove(pick)
    return pick

class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

class Dealer(Player):
    def __init__(self):
        self.hand = []
        self.val = 0

class Human(Player):
    def __init__(self):
        self.hand = []
        self.val = 0


bot = Dealer()
ron = Human()

print ('\nWelcome to the blackjack table. Your first card is:')
dealt = (deal_card())
ron.add_card(dealt)
print (dealt)

print ("\nThe dealer's first card is:")
dealt = deal_card()
bot.add_card(dealt)
print (dealt)

print ('\nYour next card is:')
dealt = (deal_card())
ron.add_card(dealt)
print (dealt)
print ("\nYour hand is currently: ")
print (ron.hand)

dealt = deal_card()
bot.add_card(dealt)

print ("\nWhat would you like to do now?")
choice = input("Enter h to hit or s to stay: ")

print (ron.hand)

if choice.lower() == 'h':
    dealt = (deal_card())
    ron.add_card(dealt)
    print ("Your hand is now: ")
    print (ron.hand)
    
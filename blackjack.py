import random

game = True
while game == True:
    print('################## Blackjack ##################')

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
    ron.val += dealt.value
    print (dealt)

    print ("\nThe dealer's first card is:")
    dealt = deal_card()
    bot.add_card(dealt)
    bot.val += dealt.value
    print (dealt)

    print ('\nYour next card is:')
    dealt = (deal_card())
    ron.add_card(dealt)
    ron.val += dealt.value
    print (dealt)

    dealt = deal_card()
    bot.add_card(dealt)
    bot.val += dealt.value

    if ron.val>21:
        print("you busted - dealer wins!")
        continue
    elif ron.val==21:
        print("Blackjack! - you win!")
        continue
    elif bot.val>21:
        print("dealer busted - you win!")
        continue

    flag = True
    while ron.val < 21 and flag == True:
        print ("\nYour hand is currently: ")
        print (ron.hand)
        print ("\nWhat would you like to do now?")
        choice = input("Enter h to hit or s to stay: ")
        if choice.lower() == 'h':
            print('################## Hit! ##################')
            print('\nYour next card is:')
            dealt = (deal_card())
            ron.add_card(dealt)
            ron.val += dealt.value
            print (dealt)
            if ron.val>21:
                print("you busted!")
                continue
            elif ron.val == 21:
                print("that makes 21 - you win!")
                continue
            else:
                continue

        elif choice.lower() == 's':
            flag = False
            print('################## Stay ##################')
            print ("\nThe dealer's hand is:")
            print (bot.hand)

            while bot.val<ron.val or (bot.val == ron.val and bot.val<17):
                while bot.val<17 or bot.val<ron.val:    
                    print('################## Hit! ##################')
                    print ("The dealer hits. His next card is:")
                    dealt = deal_card()
                    bot.add_card(dealt)
                    bot.val += dealt.value
                    print (dealt)
                    if bot.val > ron.val:
                        break


            if bot.val > 21:
                print("dealer busts - you win!")
            elif bot.val == 21:
                print("dealer got 21 - dealer wins!")
            elif ron.val > bot.val:
                print (f'Dealer total: {bot.val}')
                print (f'Your total: {ron.val}')
                print ("\nCongrats, you win!")
            elif bot.val > ron.val:
                print (f'Dealer total: {bot.val}')
                print (f'Your total: {ron.val}')
                print ('\nDealer wins')
            elif bot.val == ron.val:
                print (f'Dealer total: {bot.val}')
                print (f'Your total: {ron.val}')
                print ('\nThe game is a draw!')
            else:
                continue

    answer = input("\n\nWould you like to play again? Enter 'no' to quit or hit enter any other key to continue:  >")
    if answer.lower() == 'no':
        game = False
    else:
        continue

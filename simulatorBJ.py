# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:15:20 2022

@author: Christopher
"""

import random

#TODO: remove global variables.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self, numDecks=1):
        self.deck = []  # start with an empty list#
        #allows for multiple decks
        for i in range(numDecks):
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))
    
    def __str__(self):
        compDeck = '' #starting competition deck empty#
        for card in self.deck:
            compDeck += '\n' + card.__str__() #add each card object;s strin#
        return 'The deck has' + compDeck
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        card = self.deck.pop()
        return card
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def drawCard(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjustForAce(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1  

class Visualizer:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
    
    def displayPartial(self):
        print("\nDealer's Hand")
        print("<card hidden>")
        print(' ', self.dealer.cards[1])
        print("\nPlayer's Hand: ", *self.player.cards, sep= '\n')
            
    def displayAll(self):
        print("\nDealer's Hand:", *self.dealer.cards, sep="\n")
        print("Dealer's Hand =",self.dealer.value)
        print("\nPlayer's Hand: ", *self.player.cards, sep= '\n')
        print("Player's Hand = ", self.player.value)
    
class Game:
    def __init__(self):
        # Create & shuffle the deck
        self,playing = True
        self.deck = Deck()
        self.deck.shuffle()
        #initialize hands
        self.dealer = Hand()
        self.player = Hand() #TODO: change to allow multiple players
        
    def start(self):
        #draw first card
        self.player.drawCard(self.deck.deal())
        self.dealer.drawCard(self.deck.deal())

        #draw second card
        self.player.drawCard(self.deck.deal())
        self.dealer.drawCard(self.deck.deal())
        
    def hit(self):
        self.player.drawCard(self.deck.deal())
        self.player.adjustForAce()
        
    def stand(self):
        return False
    
    def validator(self):
        
        if player.value <= 21:
         
         while dealer.value <17:
             hit(deck, dealer)
     
         # Show all cards
         gui.displayAll()
         
         # Run different winning scenarios
         if dealer.value > 21:
             print("Dealer busts!")
 
         elif dealer.value > player.value:
             print("Dealer wins!")
 
         elif dealer.value < player.value:
              print("Player wins!")
 
         else:
             print("Dealer and Player tie! It's a push.") 
        
rounds = 10 #number of round to simulate

for r in range(rounds):
    game = Game()
    game.start() #deals two cards to all players
    #TODO store players initial totals
    #TODO player action
    if r < rounds/2:
        game.hit()
    else:
        game.stand()

    #TODO winner validator
    print(r)

# =============================================================================
# while True:
#     
#     while playing:  # recall this variable from our hit_or_stand function
#         x = input("Would you like to Hit or Stand? Enter 'h' or 's'")
#         
#         if x[0].lower() == 'h':
#             hit(deck, player)  # hit() function defined above
# 
#         elif x[0].lower() == 's':
#             print("Player stands. Dealer is playing.")
#             playing = False
# 
#         else:
#             print("Sorry, please try again.")
#             continue
#         
#         # Show cards (but keep one dealer card hidden)
#         gui.displayPartial()
#         
#         # If player's hand exceeds 21, run player_busts() and break out of loop
#         if player.value >21:
#             print("Player busts!")
#             break
# 
#     # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
#     if player.value <= 21:
#         
#         while dealer.value <17:
#             hit(deck, dealer)
#     
#         # Show all cards
#         gui.displayAll()
#         
#         # Run different winning scenarios
#         if dealer.value > 21:
#             print("Dealer busts!")
# 
#         elif dealer.value > player.value:
#             print("Dealer wins!")
# 
#         elif dealer.value < player.value:
#              print("Player wins!")
# 
#         else:
#             print("Dealer and Player tie! It's a push.") 
# =============================================================================

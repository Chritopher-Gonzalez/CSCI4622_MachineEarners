# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:15:20 2022

@author: Christopher
"""

import random
import numpy as np

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

    def getValue(self):
        return self.value

    def getHasAces(self):
        if(self.aces >= 1):
            return True
        else:
            return False

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
        self.playing = True
        self.deck = Deck()
        self.deck.shuffle()
        #initialize hands
        self.dealer = Hand()
        self.player = Hand() #TODO: change to allow multiple players
        self.actions = 0

        # data
        self.isSoft = 0
        self.playerValue = 0
        self.shownDealerCard = 0
        self.shownCardIsAce = 0
        self.outcome = 0 # 1 for player wins, -1 for player loses, 0 for push
        self.dealerValue = 0 # just used for testing
        self.action = 0
        self.drawnCard = 0
        self.dealerFinalVal = 0

    def start(self):
        #draw first card
        self.player.drawCard(self.deck.deal())
        self.dealer.drawCard(self.deck.deal())

        #draw second card
        self.player.drawCard(self.deck.deal())
        self.dealer.drawCard(self.deck.deal())

        # player data
        self.playerValue = self.player.getValue()
        if(self.player.cards[0].rank == "Ace" or self.player.cards[1].rank == "Ace"):
            self.isSoft = 1

        # dealer data
        self.shownDealerCard = values[self.dealer.cards[1].rank]
        if(self.shownDealerCard == 11):
            self.shownCardIsAce = 1

        self.dealerValue = self.dealer.getValue()



    def hit(self, player):
        if player == True:
            self.player.drawCard(self.deck.deal())
            self.player.adjustForAce()
        else:
            self.dealer.drawCard(self.deck.deal())
            self.dealer.adjustForAce()

    def stand(self):
        self.playing = False

    def updateActions(self):
        self.actions =+ 1

    def playGame(self, action):
        if(action):
            self.action = 1

        if self.dealer.value == 21:
            if self.player.value == 21:
                return 0 #push scenario game ended in a tie
            else:
                return -1 #player lost due to action
        else:
            if action:
                self.hit(player=True)
                self.updateActions()
                self.drawnCard = values[self.player.cards[-1].rank]

            else:
                self.stand()

            if self.player.value > 21:
                return -1
                #player lost due to action

        while self.dealer.value <17:
            self.hit(player=False)

        self.dealerFinalVal = self.dealer.value

        # Run different winning scenarios
        if self.dealer.value > 21:
            return 1
            #player won due to action

        elif self.dealer.value > self.player.value:
            return -1
            #player lost due to action

        elif self.dealer.value < self.player.value:
            return 1
            #player won due to action

        else:
            return 0
            #push scenario game ended in a tie

    def getData(self):
        # return np.array([self.isSoft, self.playerValue, self.drawnCard, self.shownCardIsAce, self.shownDealerCard, self.dealerValue, self.dealerFinalVal])

        return np.array([self.isSoft, self.playerValue, self.action, self.shownCardIsAce, self.shownDealerCard])

rounds = 50000 #number of round to simulate

# this plays a single game to determine how many features the game outputs. if we modify the code to add new features,
# we will not have to modify this code
testGame = Game()
testGame.start()
numFeatures = len(testGame.getData())

X = np.zeros((rounds, numFeatures))
y = np.zeros((rounds, 1))

for r in range(rounds):
    game = Game()
    game.start() #deals two cards to all players
    #TODO store players initial totals
    #TODO player action
    action = None
    if r < rounds/2:
        #play with a hit
        action = True
    else:
        #play with a stand
        action = False

    outcome = game.playGame(action)

    X[r] = game.getData()
    y[r]= outcome

#print(X)
X = np.append(X, y, axis=1)
np.save("X.npy", X)

lose = []
for i in y:
    if i == -1:
        lose.append(1)
    else:
        lose.append(0)
y = np.array(lose)

np.save("y.npy", y)


# to load:

# X = np.load("X.npy")
# y = np.load("y.npy")


# ===============

#print(X)
#print(y)

#print("outcome, isSoft, pVal, pDrawnCard, isAce, shownCard, dStartValue, dFinalVal")
#print(np.concatenate((y,X), axis = 1))

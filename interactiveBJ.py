import random

#FIXME: remove global variables.
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
    def __init__(self):
        self.deck = []  # start with an empty list#
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
    
    def addCard(self, card):
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
    
        
def hit(deck,hand):
    hand.addCard(deck.deal())
    hand.adjustForAce()
    
def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's'")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        
        break
    
#GAME
while True:
    playing = True 
    # Print an opening statement
    print("Welcome to MachineEarners's Blackjack Simulator.")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.addCard(deck.deal())
    player.addCard(deck.deal())
    
    dealer = Hand()
    dealer.addCard(deck.deal())
    dealer.addCard(deck.deal())
    
    # Show cards (but keep one dealer card hidden)
    gui = Visualizer(player, dealer)
    gui.displayPartial()
    
    while playing:  # recall this variable from our hit_or_stand function
        x = input("Would you like to Hit or Stand? Enter 'h' or 's'")
        
        if x[0].lower() == 'h':
            hit(deck, player)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        
        # Show cards (but keep one dealer card hidden)
        gui.displayPartial()
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value >21:
            print("Player busts!")
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
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
        
    # Ask to play again
    new_game = input("would you like to play again? Enter 'y' or 'n'")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing! ')

        break
import random

class Blackjack:
	def __init__(self, nDecks):

		self.deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]
		self.deck = [x for x in self.deck for _ in range(nDecks * 4)]
		random.shuffle(self.deck)

		self.dealersHand = []
		self.playersHand = []
		


	def dealerPlays(self):

		# In progress. Right now dealers draws cards until their total exceeds 16 (standard dealerstrategy)
		# BUT aces are counted as 1, instead of as 1 OR 11

		self.dealersHand.append(self.drawCard())
		self.dealersHand.append(self.drawCard())

		print("Dealer's first two cards: {}".format(self.dealersHand))

		while(sum(self.dealersHand) <= 16):
			self.dealersHand.append(self.drawCard())
			print("Dealer's current hand: {}".format(self.dealersHand))

		print("Dealer final score: {}".format(sum(self.dealersHand)))

	def printDeck(self):
		print(self.deck)

	def printDealerHand(self):
		print(self.dealersHand)

	def dealerScore(self):
		acc = 0
		nAces = 0

		for card in dealersHand:
			acc += card

			if(card == 1):
				nAces += 1



	def drawCard(self):
		return self.deck.pop()




a = Blackjack(1)

a.dealerPlays()

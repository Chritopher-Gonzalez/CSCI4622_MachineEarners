# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:15:20 2022

@author: Christopher
"""
from abstractBJ import Game
import numpy as np

rounds = 100000 #number of round to simulate

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
#X = np.append(X, y, axis=1)
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

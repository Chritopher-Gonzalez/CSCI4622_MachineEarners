# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:15:20 2022

@author: Christopher
"""
from abstractCountingBJ import Game
import numpy as np

rounds = 100000 #number of round to simulate

# this plays a single game to determine how many features the game outputs. if we modify the code to add new features,
# we will not have to modify this code
testGame = Game(removeSubset=True)
testGame.start()
numFeatures = len(testGame.getData())

X = np.zeros((rounds, numFeatures))
y = np.zeros((rounds, 1))

for r in range(rounds):
    game = Game(removeSubset=True)
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

    if outcome  == -1:
        y[r]= 1
    else:
        y[r]= 0

np.save("X.npy", X)

correct = []
for i, val in enumerate(y):
    if val == 1:
        if X[i, 0] == 1:
            correct.append(0)
        else:
            correct.append(1)
    else:
        if X[i, 0] == 1:
            correct.append(1)
        else:
            correct.append(0)

np.save("y.npy", correct)


# to load:

# X = np.load("X.npy")
# y = np.load("y.npy")

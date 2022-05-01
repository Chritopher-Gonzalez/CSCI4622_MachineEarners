from abstractCountingBJ import Game
import numpy as np
import keras
import sklearn.metrics as metrics
import random

"""
reconstructed_model = keras.models.load_model("model")

def model_decision(input_array):
    input_array = input_array.reshape(1,-1)
    predict_correct = reconstructed_model.predict(input_array)
    if predict_correct >= 0.52:
        return 1
    else:
        return 0
"""
rounds = 100 #number of round to simulate

# this plays a single game to determine how many features the game outputs. if we modify the code to add new features,
# we will not have to modify this code
testGame = Game()
testGame.start()
numFeatures = len(testGame.getData())

X = np.zeros((rounds, numFeatures))
y = np.zeros((rounds, 1))
prediction = []

for r in range(rounds):
    game = Game()
    game.start() #deals two cards to all players

    action = random.randint(0, 1)
    #action = model_decision(game.getData())
    prediction.append(action)

    outcome = game.playGame(action)

    X[r] = game.getData()
    y[r]= outcome

unique, counts = np.unique(y, return_counts=True)
print(np.asarray((unique, counts)).T)

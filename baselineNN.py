import sklearn.metrics as metrics
from keras.models import Sequential
import numpy as np
from keras.layers import Dense, LSTM, Flatten, Dropout, InputLayer

results = []
for i in range(50):
	exec(open("simulatorBJ.py").read())

	train_X = np.load("X.npy")
	train_y = np.load("y.npy").reshape(-1,1)
	#TODO: Load Data
	#train_X = None
	#train_y = np.array(model_df['correct_action']).reshape(-1,1)

	# Set up a neural net with 5 layers
	model = Sequential()
	model.add(InputLayer(input_shape=(train_X.shape[1],)))
	model.add(Dense(16))
	model.add(Dense(128))
	model.add(Dense(32))
	model.add(Dense(8))
	model.add(Dense(1, activation='sigmoid'))
	model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=["accuracy"])
	model.fit(train_X, train_y, epochs=20, batch_size=256, verbose=1)
	model.save("model")

	prediction = np.rint(model.predict(train_X))
	print((prediction))
	actuals = train_y[:,-1]

	print(metrics.accuracy_score(actuals, prediction))
	results.append(metrics.accuracy_score(actuals, prediction))

print(results)

print("mean: ")
print(np.mean(results))

print("standard dev:")
print(np.std(results))

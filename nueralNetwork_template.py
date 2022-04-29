import sklearn.metrics as metrics
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten, Dropout

#TODO: Load Data
train_X = None
train_y = np.array(model_df['correct_action']).reshape(-1,1)

# Set up a neural net with 5 layers
model = Sequential()
model.add(Dense(16))
model.add(Dense(128))
model.add(Dense(32))
model.add(Dense(8))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd')
model.fit(train_X, train_Y, epochs=20, batch_size=256, verbose=1)

prediction = model.predict(train_X)
actuals = train_Y[:,-1]

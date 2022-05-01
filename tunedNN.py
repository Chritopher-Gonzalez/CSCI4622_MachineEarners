import sklearn.metrics as metrics
import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten, Dropout, InputLayer
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


train_X = np.load("X.npy")
train_y = np.load("y.npy").reshape(-1,1)
#TODO: Load Data
#train_X = None
#train_y = np.array(model_df['correct_action']).reshape(-1,1)

# Set up a neural net with 5 layers
model = Sequential()
model.add(Dense(16, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    loss='binary_crossentropy',
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics=["accuracy"]
)

checkpoint_callbk = tf.keras.callbacks.ModelCheckpoint(
    "best_model", # name of file to save the best model to
    monitor="accuracy", # prefix val to specify that we want the model with best macroF1 on the validation data
    verbose=1, # prints out when the model achieve a better epoch
    mode="max", # the monitored metric should be maximized
    save_freq="epoch", # clear
    save_best_only=True, # of course, if not, every time a new best is achieved will be savedf differently
    save_weights_only=True # this means that we don't have to save the architecture, if you change the architecture, you'll loose the old weights
)

early = tf.keras.callbacks.EarlyStopping(
    monitor='accuracy',
    min_delta=0,
    patience=20,
    verbose=1,
    mode='max'
)
#model.fit(train_X, train_y, epochs=20, batch_size=256, verbose=1, callbacks=[checkpoint_callbk, early])


history = model.fit(train_X, train_y, epochs=20, batch_size=256, verbose=1, callbacks=[checkpoint_callbk, early])
model.save("model")
# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()

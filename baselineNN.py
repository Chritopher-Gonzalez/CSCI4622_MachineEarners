import sklearn.metrics as metrics
import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten, Dropout, InputLayer
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


exec(open("simulatorBJ.py").read())

#train_X = np.load("X.npy")
save_X  = np.load("X.npy")
train_y = np.load("y.npy").reshape(-1,1)
#TODO: Load Data
#train_X = None
#train_y = np.array(model_df['correct_action']).reshape(-1,1)

h = []
legend_labels = []

for i in range(5):

    if(i == 0):
        train_X = save_X[:, [0,1,4]] # initial cards
        legend_labels.append('Shown Cards')
    
    if(i == 1):
        train_X = save_X[:, [0,1,2,4]] # initial cards + isSoft
        legend_labels.append('Shown Cards + isSoft')

    if(i == 2):
        train_X = save_X[:, [0,1,3,4]] # initial cards + shownCardIsAce
        legend_labels.append('Shown Cards + isAce')

    if(i == 3):
        train_X = save_X[:, [0,1,2,3,4]] # initial cards + isSoft + shownCardIsAce  
        legend_labels.append('Shown Cards + isSoft + isAce')

    if(i == 4):
        train_X = save_X # includes everything      
        legend_labels.append('All data, including counting')

    # Set up a neural net with 5 layers
    model = Sequential()
    model.add(Dense(16))
    model.add(Dense(128))
    model.add(Dense(32))
    model.add(Dense(8))
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
#model.save("model")

    history = model.fit(train_X, train_y, epochs=20, batch_size=256, verbose=1, callbacks=[checkpoint_callbk, early])
    h.append(history)

# list all data in history
print(history.history.keys())
# summarize history for accuracy
print(type(history.history['accuracy']))

for i in range(5):
    plt.plot(h[i].history['accuracy'])

plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(legend_labels, loc='lower right')
plt.show()


import os
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

print 'Reading training, validation and test data.....'
username = 'beautifuldestinations'
path = './' + username

npzfile = np.load(username + '_train.npz')
X_train = npzfile['arr_0']
Y_train = npzfile['arr_1']

npzfile = np.load(username + '_validation.npz')
X_validation = npzfile['arr_0']
Y_validation = npzfile['arr_1']

npzfile = np.load(username + '_test.npz')
X_test = npzfile['arr_0']
Y_test = npzfile['arr_1']

print(len(Y_train))
print(len(Y_validation))
print(len(Y_test))

""" Note that not all images in train, validation and test set have the same dimensions. 
For example, running the following snippet:

for x in X_validation:
    print x.shape
    
results in varied shapes: (929, 750), (1349, 1080), (...)
"""

# ## Test correct data
# plt.imshow(X_train[0], cmap = 'gray')
# plt.show()

print 'Done reading data.'

print 'Building Model'
batch_size = 128
epochs = 200

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape = (1, None, None)))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (4, 4), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (4, 4)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (5, 5), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (5, 5)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('relu'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(X_train, Y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=(X_validation, Y_validation),
            shuffle=True)
            
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])



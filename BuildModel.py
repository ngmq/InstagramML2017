import os
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras.backend as K

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

minX = 0.0
minY = 0.0
maxX = 0.0
maxY = 0.0

minX = min(X_train)
minX = min(minX, min(X_validation))
minX = min(minX, min(X_test))

maxX = max(X_train)
maxX = max(maxX, max(X_validation))
maxX = max(maxX, max(X_test))

minY = min(Y_train)
minY = min(minY, min(Y_validation))
minY = min(minY, min(Y_test))

maxY = max(Y_train)
maxY = max(maxY, max(Y_validation))
maxY = max(maxY, max(Y_test))

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

print 'Building Model...'

""" Custom accuracy measurement for regression
"""
threshold = 0.105
def calc_point(y_true, y_pred):
    diff = K.abs(y_true - y_pred)
    maxdiff = y_true * threshold    
    return K.sum(K.less_equal(diff, maxdiff))
    
batch_size = 64
epochs = 200
imgsz = 640, 640, 3

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape = (640, 640, 3)))
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
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('relu'))

print 'Compiling model...'
model.compile(loss='mean_squared_error',
              optimizer='rmsprop',
              metrics=[calc_point])

              
print 'Fitting model...'
# model.fit(X_train, Y_train,
            # batch_size=batch_size,
            # epochs=epochs,
            # validation_data=(X_validation, Y_validation),
            # shuffle=True)
            
print 'Evaluating model...'

score = model.evaluate(X_test, Y_test, batch_size = batch_size, verbose=0)
print('Test loss:', score[0])
print('Test accuracy (points):', score[1])
model.save(username + '.h5')


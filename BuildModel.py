import os
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Activation, Flatten
# from keras.layers import Conv2D, MaxPooling2D
# import keras.backend as K
# from keras import optimizers

print 'Reading training, validation and test data.....'
username = 'kissinfashion'
path = './' + username

""" 
beautifuldestinations
kissinfashion
instagood
etdieucrea
josecabaco
"""

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

minX = np.min(X_train)
minX = min(minX, np.min(X_validation))
minX = min(minX, np.min(X_test))

maxX = np.max(X_train)
maxX = max(maxX, np.max(X_validation))
maxX = max(maxX, np.max(X_test))

minY = np.min(Y_train)
minY = min(minY, np.min(Y_validation))
minY = min(minY, np.min(Y_test))

maxY = np.max(Y_train)
maxY = max(maxY, np.max(Y_validation))
maxY = max(maxY, np.max(Y_test))

X_train = (0.0 + X_train - minX) / (0.0 + maxX - minX)
X_validation = (0.0 + X_validation - minX) / (0.0 + maxX - minX)
X_test = (0.0 + X_test - minX) / (0.0 + maxX - minX)

Y_train = (0.0 + Y_train - minY) / (0.0 + maxY - minY)
Y_validation = (0.0 + Y_validation - minY) / (0.0 + maxY - minY)
Y_test = (0.0 + Y_test - minY) / (0.0 + maxY - minY)

print minY
print maxY

""" Note that not all images in train, validation and test set have the same dimensions. 
For example, running the following snippet:

for x in X_validation:
    print x.shape
    
results in varied shapes: (929, 750), (1349, 1080), (...)
"""

# ## Test correct data
# plt.imshow(X_train[0])
# plt.show()

print 'Done reading data.'

# print 'Building Model...'

""" Custom accuracy measurement for regression
"""
# threshold = 0.095
# def calc_point(y_true, y_pred):
    # diff = K.abs(y_true - y_pred)
    # maxdiff = y_true
    # maxdiff = maxdiff * threshold
    # return K.mean(K.less_equal(diff, maxdiff))
    
# batch_size = 16
# epochs = 50
# imgsz = 128, 128, 3
# FC_max_weight = maxY / 256.0
# FC_min_weight = minY / 256.0

# model = Sequential()
# model.add(Conv2D(32, (3, 3), input_shape = (128, 128, 3)))
# model.add(Activation('relu'))
# model.add(Conv2D(32, (3, 3)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

# model.add(Conv2D(64, (4, 4), padding='same'))
# model.add(Activation('relu'))
# model.add(Conv2D(64, (4, 4)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

# model.add(Conv2D(64, (5, 5), padding='same'))
# model.add(Activation('relu'))
# model.add(Conv2D(64, (5, 5)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

# model.add(Flatten())

# model.add(Dense(256))
# model.add(Activation('sigmoid'))
# model.add(Dropout(0.5))

# ScaleInit = keras.initializers.RandomUniform(minval=FC_min_weight, maxval=FC_max_weight, seed=None)
# model.add(Dense(1, kernel_initializer = ScaleInit))
# model.add(Activation('linear'))

# print 'Compiling model...'

# sgd = optimizers.SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='mean_squared_error',
              # optimizer=sgd,
              # metrics=[calc_point])

              
# print 'Fitting model...'
# model.fit(X_train, Y_train,
           # batch_size=batch_size,
           # epochs=epochs,
           # shuffle=True)
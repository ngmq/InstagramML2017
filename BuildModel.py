import os
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
import keras.backend as K
from keras import optimizers

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

npzfile = np.load('json_data_' + username + '.npz')
X = npzfile['arr_0']
Y = npzfile['arr_1']

N = len(Y)
train_size = int(N * 90 / 100)
X_train = X[:train_size]
Y_train = Y[:train_size]
X_test = X[train_size:]
Y_test = Y[train_size:]

print(len(Y_train))
print(len(Y_test))

minX = np.min(X, 0)
minY = np.min(Y)
maxX = np.max(X, 0)
maxY = np.max(Y)

X_train = (0.0 + X_train - minX) / (0.0 + maxX - minX)
X_test = (0.0 + X_test - minX) / (0.0 + maxX - minX)

Y_train = (0.0 + Y_train - minY) / (0.0 + maxY - minY)
Y_test = (0.0 + Y_test - minY) / (0.0 + maxY - minY)

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
threshold = 0.095
def calc_point(y_true, y_pred):
    Y_true = y_true * (maxY - minY) + minY
    Y_pred = y_pred * (maxY - minY) + minY
    diff = K.abs(Y_true - Y_pred)
    maxdiff = Y_true * threshold
    return K.mean(K.less_equal(diff, maxdiff))
    
def calc_loss(y_true, y_pred):
    Y_true = y_true * (maxY - minY) + minY
    Y_pred = y_pred * (maxY - minY) + minY
    diff = K.abs(Y_true - Y_pred)
    maxdiff = Y_true * threshold
    mask = K.less_equal(diff, maxdiff)
    
    diffy = K.abs(y_true - y_pred) ** 2
    import tensorflow as tf
    return K.mean(tf.boolean_mask(diffy, mask))
    
batch_size = 16
epochs = 30
ndimension = len(X[0])

model = Sequential()
model.add(Dense(30, input_shape = (ndimension, )))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(Dense(20))
model.add(Activation('tanh'))
model.add(Dropout(0.25))
model.add(Dense(1))
model.add(Activation('sigmoid'))

print 'Compiling model...'

sgd = optimizers.SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss=calc_loss, optimizer=sgd, metrics=[calc_point])

              
print 'Fitting model...'
# model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs)

print 'Testing model...'
score = model.evaluate(X_test, Y_test, batch_size = batch_size, verbose=0)
print('Test loss:', score[0])
print('Test accuracy (points):', score[1])
model.save(username + '.h5')
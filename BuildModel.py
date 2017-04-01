import os
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

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

plt.imshow(X_train[0], cmap = 'gray')
plt.show()


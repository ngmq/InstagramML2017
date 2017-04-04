import os
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

username = 'kissinfashion'
path = './' + username

""" 
beautifuldestinations
kissinfashion
instagood
etdieucrea
josecabaco
"""

files = os.listdir(path)

X = list()
Y = list()

# imgsz = (640, 640)

minY = 50000.0
maxY = 0.0

for f in files:
    """ f is a string with format [index]-[code]-[likes].jpg
    """
    nlike = int(f.split('-')[-1].split('.')[0])
    nlike = int(nlike) # estimate that 70% of likes of an image comes within first 24 hours
    Y.append(nlike)
    maxY = max(maxY, nlike)
    minY = min(minY, nlike)
    # print nlike
    # img = misc.imread(path + '/' + f)
    # print img.shape
    # img = misc.imresize(img, (128, 128, 3))
    # X.append(img)
    
print minY, maxY
plt.hist(Y, bins='auto')
plt.title("Histogram with 'auto' bins")
plt.show()

""" Keep 90% of data for training, 5% for validation and 5% for testing
"""
# N = len(files)
# train_size = int(N * 90 / 100)
# X_train = X[:train_size]
# Y_train = Y[:train_size]

# test_size = int(N * 5 / 100)
# X_validation = X[train_size:train_size+test_size]
# Y_validation = Y[train_size:train_size+test_size]

# X_test = X[train_size+test_size:]
# Y_test = Y[train_size+test_size:]
    
# np.savez(username + '_train', X_train, Y_train) 
# np.savez(username + '_validation', X_validation, Y_validation) 
# np.savez(username + '_test', X_test, Y_test) 

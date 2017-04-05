import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import pickle
from sklearn.externals import joblib

# threshold = 0.095
username = 'josecabaco'
npzfile = np.load('json_data_' + username + '.npz')
X = npzfile['arr_0']
Y = npzfile['arr_1']
print X.shape
print Y.shape

N = len(Y)
X_train = X
Y_train = Y

# X_test = X[train_size:]
# Y_test = Y[train_size:]

model = KNeighborsRegressor(n_neighbors=len(Y_train), weights = 'distance', algorithm='auto')
model.fit(X_train, Y_train)
joblib.dump(model, 'KNN_' + username + '.pkl') 

# Y_test = Y_test * 0.7
k = X[7]
Y_pred = model.predict(k)
Y_pred = int(Y_pred[0])
print Y_pred
# Y_pred = np.round(Y_pred)
# diff = np.abs(Y_test - Y_pred)
# maxdiff = Y_test * threshold
# result = diff < maxdiff
# print Y_pred
# print Y_test
# print result
# print diff
# print maxdiff

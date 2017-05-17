import os
import numpy as np

import pickle

from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from sklearn.ensemble import ExtraTreesRegressor

with open('imgs01.bin', 'rb') as f:
    X = pickle.load(f)
    
with open('imgs01Likes.bin', 'rb') as f:
    y = pickle.load(f)
    
with open('et.bin', 'rb') as f:
    et = pickle.load(f)
    
print 'Len X = ', len(X)
print 'Len y = ', len(y)

# et_params = dict(
    # n_estimators=200,
    # criterion='mse',
    # max_depth=40,
    # min_samples_split=6,
    # min_samples_leaf=6,
    # max_features=128, 
    # bootstrap=True, 
    # n_jobs=-1,
    # random_state=1
# )

# et = ExtraTreesRegressor(**et_params)
# et.fit(X, y)

# with open('et.bin', 'wb') as f:
    # pickle.dump(et, f)
    
print "Score on training set = ", et.score(X, y)

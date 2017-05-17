import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input
import keras.backend as K

import pickle
import os
from glob import glob
from tqdm import tqdm

vgg16 = VGG16(weights='imagenet', include_top=True, pooling='max')
featureExtractor = K.function(vgg16.inputs, [vgg16.output])

imgs01 = glob("./post-images-01/*.jpg")

pca = PCA(n_components = 256)
X = list()

for img_path in tqdm(imgs01):
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        features  = featureExtractor([x])
    
        # print "haha"
        # print "image_path = ", img_path
        img_name = os.path.basename(img_path)
        # print "img_name = ", img_name # this is the id
        # print "type features = ", type(features)
        # print len(features) # len = 1
        # print "type feature[0] = ", type(features[0])
        # print "shape = ", features[0].shape
        
        X.append(features[0][0])
    except Exception as e:
        print('exception!!', str(e))
        print("Continue to next picture")
        
  
print "hehe"
# print X  
X = np.array(X)
print X.shape
Z = pca.fit_transform(X)

with open("pca.bin", "wb") as f:
    pickle.dump(pca, f)
    
print "pca saved."
    
with open("first1000pic.bin", "wb") as f:
    pickle.dump(Z, f)
    
print "Z saved."

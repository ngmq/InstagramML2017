import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from keras.preprocessing import image
import pickle
import os
from glob import glob
from tqdm import tqdm
import json

dY = dict()
all_json = glob("./post-data-useful/*.json")
for json_path in tqdm(all_json):
    try:
        f = open(json_path)
        data = json.load(f)
        f.close()
        
        dY[data['id']] = data['likes']        
    except Exception as e:
        print('exception when read json', str(e))
        print('continue to next json file')

imgs01 = glob("./post-images-01/*.jpg")

Y = list()

count = 0
for img_path in tqdm(imgs01):
    try:
        img = image.load_img(img_path, target_size=(224, 224))
    
        # print "haha"
        # print "image_path = ", img_path
        img_name = os.path.basename(img_path)
        img_file = os.path.splitext(img_name)[0]
        
        if( img_file in dY ):
            Y.append(dY[img_file])
        else:
            print("bigger exception here@@@", img_path)
            print("count = ", count)
            Y.append(0)
    except Exception as e:
        print('exception!!', str(e))
        print("Continue to next picture")
        continue
        
  
print "hehe"
Y = np.array(Y)
print len(Y)

with open("Likes.bin", "wb") as f:
    pickle.dump(Y, f)
    
print "Likes saved."

import json
import ijson
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sst
from sets import Set


def get_enum_value(likelihood):
    if likelihood == 'VERY_UNLIKELY':
        return 1
    if likelihood == 'UNLIKELY':
        return 2
    if likelihood == 'POSSIBLE':
        return 3
    if likelihood == 'LIKELY':
        return 4
    if likelihood == 'VERY_LIKELY':
        return 5
    return 0

print 'Reading json file...'
f = open('dataset.json')
data = json.load(f)
f.close()

print 'Read json OK.'
username = data[0].get("username")
kissinfashion = data[0].get("posts")

print 'Getting likes...'
# likes = [p.get('instagram').get('likes').get('count') for p in kissinfashion]
# hasFace = {'0': [], '1': []}
# for p in kissinfashion:
    # like = p.get('instagram').get('likes').get('count')
    # if p.get('annotations').get('faceAnnotations') is None:
        # hasFace.get('0').append(like)
    # else:
        # hasFace.get('1').append(like)
        
# print sst.ttest_ind(hasFace.get('0'), hasFace.get('1'))

# Ttest_indResult(statistic=3.1289134685704121, pvalue=0.0018050893450610637) <= significant difference.
    
# plt.figure(1)
# plt.hist(hasFace.get('1'), bins='auto')
# plt.show()

""" Now build a dictionary from label Annotations
"""

all_label = {}
cnt = 0
for p in kissinfashion:
    like = p.get('instagram').get('likes').get('count')
    labels = p.get('annotations').get('labelAnnotations')
    if labels is not None:
        for label in labels:
            if all_label.get(label.get('description')) is None:
                all_label[label.get('description')] = cnt
                cnt += 1
    
nlabel = len(all_label)
print nlabel
print all_label

X = list()
Y = list()

for p in kissinfashion:
    L = list()
    """ Face features """
    faceAnnotations = p.get('annotations').get('faceAnnotations')
    if faceAnnotations is not None:
        """ roll, pan, tilt """
        faceAnnotations = faceAnnotations[0]
        L.append(faceAnnotations.get('rollAngle', 0))
        L.append(faceAnnotations.get('panAngle', 0))
        L.append(faceAnnotations.get('tiltAngle', 0))
        """ joy, sorrow, anger, surprise, underExposed, blurred, headwear """
        L.append(get_enum_value(faceAnnotations.get('joyLikelihood', "")))
        L.append(get_enum_value(faceAnnotations.get('sorrowLikelihood', "")))
        L.append(get_enum_value(faceAnnotations.get('angerLikelihood', "")))
        L.append(get_enum_value(faceAnnotations.get('surpriseLikelihood', "")))
        L.append(get_enum_value(faceAnnotations.get('underExposedLikelihood', "")))
        L.append(get_enum_value(faceAnnotations.get('blurredLikelihood', "")))
        L.append(get_enum_value(faceAnnotations.get('headwearLikelihood', "")))
    else:
        L.extend([0] * 10)
    
    """ Label features """
    words = [0] * nlabel
    labels = p.get('annotations').get('labelAnnotations')
    
    if labels is not None:
        for i, label in enumerate(labels):
            words[all_label[label.get('description')]] = 1
            
    L.extend(words)
    
    """ Image Properties Features """
    colors = p.get('annotations').get('imagePropertiesAnnotation').get('dominantColors').get('colors')
    # if len(colors) < 7:
        # print 'new len: ', len(colors)
    for dcolor in colors[0:7]:
        r, g, b = dcolor.get('color').get('red', 0), dcolor.get('color').get('green', 0), dcolor.get('color').get('blue', 0)
        fraction = dcolor['pixelFraction']
        rgb = (r*65536)+(g*256)+b
        rgb = rgb * fraction
        L.append(rgb)
    
    """ Done """
    X.append(L)
    like = p.get('instagram').get('likes').get('count')
    Y.append(like)
    
    
ndimension = 10 + nlabel + 7
print 'ndimension = ', ndimension
np.savez('json_data' + '_' + username, X, Y)
    
    
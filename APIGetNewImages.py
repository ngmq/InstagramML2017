import json
import urllib
import requests
from requests.auth import HTTPBasicAuth
import time
from sklearn.externals import joblib

_user = 'manhquan233@gmail.com'
_pass = 'VmJsb83qQBwyuk0PaiyxDrCUgzMZOlrQ'

# r = requests.get('http://challenges.instagram.unpossib.ly/api/live', auth=HTTPBasicAuth(_user, _pass))
# print r.status_code # 200
# print "==========================\n"
# print r.json()

post_uri = "http://challenges.instagram.unpossib.ly/api/submissions"

f = open('dataset.json')
data = json.load(f)
f.close()

all_label = [{}, {}, {}, {}, {}]
nlabel = [0] * 5

for did in range(0, 5):    
    username = data[did].get("username")
    all_posts = data[did].get("posts")
    
    cnt = 0
    for p in all_posts:
        like = p.get('instagram').get('likes').get('count')
        labels = p.get('annotations').get('labelAnnotations')
        if labels is not None:
            for label in labels:
                if all_label[did].get(label.get('description')) is None:
                    all_label[did][label.get('description')] = cnt
                    cnt += 1
                    
                    
    nlabel[did] = len(all_label[did])
    print did, nlabel[did]
    
print nlabel

all_acc = ['kissinfashion', 'instagood', 'beautifuldestinations', 'etdieucrea', 'josecabaco']
ncolors = [7, 7, 6, 6, 2]
predicted_post = {}
username = ""
data = ""

print "Loading models...."
models = []
for i, s in enumerate(all_acc):
    model = joblib.load('KNN_' + s + '.pkl')
    models.append(model)

def get_idx(username):
    for i, s in enumerate(all_acc):
        if username == s:
            return i
            
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

print get_idx('kissinfashion')            
print get_idx('instagood')
print get_idx('beautifuldestinations')
print get_idx('etdieucrea')
print get_idx('josecabaco')

print "All models loaded. Now running..."
while True:
    time.sleep(6)
    print 'Requesting...'
    new_codes = list()
    r = requests.get('http://challenges.instagram.unpossib.ly/api/live', auth=HTTPBasicAuth(_user, _pass))
    data = r.json()
    if r.status_code != 200 or data.get('success') != True:
        continue
    print 'Request OK. Processing...'
    data = data.get('accounts')
    for dict in data:
        username = dict.get('username')
        idx = get_idx(username)
        posts = dict.get('posts')
        
        print username, len(posts)
        for p in posts:
            pid = p.get('id')
            if predicted_post.get(pid) is not None:
                continue
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
            words = [0] * nlabel[idx]
            labels = p.get('annotations').get('labelAnnotations')
    
            if labels is not None:
                for i, label in enumerate(labels):
                    words[all_label[idx][label.get('description')]] = 1
            
            L.extend(words)
    
            """ Image Properties Features """
            colors = p.get('annotations').get('imagePropertiesAnnotation').get('dominantColors').get('colors')
            for dcolor in colors[0:ncolors[idx]]:
                r, g, b = dcolor.get('color').get('red', 0), dcolor.get('color').get('green', 0), dcolor.get('color').get('blue', 0)
                fraction = dcolor.get('pixelFraction', 0)
                rgb = (r*65536)+(g*256)+b
                rgb = rgb * fraction
                L.append(rgb)
    
            predict = models[idx].predict(L)
            predict = int(predict[0])
            predicted_post[pid] = predict
            response = requests.post(post_uri, json={"post" : pid, "likes" : predict}, auth = HTTPBasicAuth(_user, _pass))
            print response.status_code
            print response.reason
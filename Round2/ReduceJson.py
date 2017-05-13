import os
import json

all_files = os.listdir('./post-data')
for file in all_files:
    f = open('./post-data/' + file)
    data = json.load(f)
    
    useful_data = dict()
    useful_data['id'] = data['id']
    useful_data['created_time'] = data['created_time']
    useful_data['updated_time'] = data['updated_time']
    useful_data['likes'] = data['likes']['count']
    f.close()
    
    f = open('./post-data-useful/' + file, 'w')
    json.dump(useful_data, f)
    f.close()
    
print "Dumping useful data finished."

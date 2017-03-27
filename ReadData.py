import json
import ijson

f = open('dataset.json')
data = json.load(f)
f.close()

print type(data)
print len(data)
print type(data[0])
print len(data[0])
print type(data[1])
print len(data[1])
print type(data[2])
print len(data[2])
print type(data[3])
print len(data[3])
print type(data[4])
print len(data[4])
print "============================="
print data[0].keys()
print data[1].keys()
print data[2].keys()
print data[3].keys()
print data[4].keys()
import json
import ijson

f = open('dataset.json')
data = json.load(f)
f.close()

# print type(data)
# print len(data)
# print type(data[0])
# print len(data[0])
# print type(data[1])
# print len(data[1])
# print type(data[2])
# print len(data[2])
# print type(data[3])
# print len(data[3])
# print type(data[4])
# print len(data[4])
# print "============================="
# print data[0].keys()
# print data[1].keys()
# print data[2].keys()
# print data[3].keys()
# print data[4].keys()
# print "============================="
# print type(data[0].get("username"))
# print data[0].get("username")
# print data[1].get("username")
# print data[2].get("username")
# print data[3].get("username")
# print data[4].get("username")
# print "============================="
# print data[0].get("id")
# print data[1].get("id")
# print data[2].get("id")
# print data[3].get("id")
# print data[4].get("id")
# print "============================="
# print type(data[0].get("posts")) # type = list
# p0 = data[0].get("posts")
# print len(p0)
# print type(p0[0])
# print p0[0].keys()
# print "============================="
# print p0[0].get('updated')
# print "============================="
# print p0[0].get('instagram').keys()
# print "============================="
# print p0[0].get('annotations').keys()
# print "============================="
p1 = data[1].get('posts')
print p1[0].get('instagram').get('code')
print p1[0].get('instagram').get('likes').get('count')
import json
import ijson
import time

# f = open('dataset.json')
# data = json.load(f)
# f.close()

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
# for post in p0:
    # if post.get('instagram').get('likes').get('count') > 20000:
        # print post.get('instagram').get('code')
        # break;
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
# p1 = data[1].get('posts')
# print p1[0].get('instagram').get('code')
# print p1[0].get('instagram').get('likes').get('count')
# print p1[0].get('annotations')


# for i in range(0, 5):
    # username = data[i].get('username')
    # posts = data[i].get('posts')
    # print len(posts)
    # for i, p in enumerate(posts):
        # is_video = p.get('instagram').get('is_video')
        # post_like = p.get('instagram').get('likes').get('count')
        # if is_video:
            # print '******'
            
import urllib
import requests
from requests.auth import HTTPBasicAuth

post_uri = "http://challenges.instagram.unpossib.ly/api/submissions"
_user = 'manhquan233@gmail.com'
_pass = 'VmJsb83qQBwyuk0PaiyxDrCUgzMZOlrQ'
response = requests.post(post_uri, json={"post" : "TESTABC12345", "likes" : 128}, auth = HTTPBasicAuth(_user, _pass))
print response.status_code
print response.reason
print response.json()

# all_acc = ['kissinfashion', 'instagood', 'beautifuldestinations', 'etdieucrea', 'josecabaco']
# def get_idx(username):
    # for i, s in enumerate(all_acc):
        # if username == s:
            # return i

# while True:
    # time.sleep(6)
    # print 'Requesting...'
    # new_codes = list()
    # r = requests.get('http://challenges.instagram.unpossib.ly/api/live', auth=HTTPBasicAuth(_user, _pass))
    # data = r.json()
    # if r.status_code != 200 or data.get('success') != True:
        # continue
    # print 'Request OK. Processing...'
    # data = data.get('accounts')
    # for dict in data:
        # username = dict.get('username')
        # idx = get_idx(username)
        # posts = dict.get('posts')
        
        # print username, len(posts)
        
        # response = requests.post(post_uri, data={"post" : "1483235252197708444", "likes" : 128}, auth = HTTPBasicAuth(_user, _pass))
        # print response.status_code
        # print response.reason
        # print response.json()
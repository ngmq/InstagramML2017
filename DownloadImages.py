import json
import urllib

f = open('dataset.json')
data = json.load(f)
f.close()

_user = 'manhquan233@gmail.com'
_pass = 'VmJsb83qQBwyuk0PaiyxDrCUgzMZOlrQ'

# urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "abc/file1.jpg")

print 'Start Downloading...'
for i in range(0, 5):
    username = data[i].get('username')
    posts = data[i].get('posts')
    
    print 'Downloading to ' + username + '....'
    for i, p in enumerate(posts):
        is_video = p.get('instagram').get('is_video')
        sname = '{:04d}'.format(i)
        post_code = p.get('instagram').get('code')
        post_like = p.get('instagram').get('likes').get('count')
        sname = sname + '-' + post_code + '-' + str(post_like) + '.jpg'
        img_url = p.get('instagram').get('display_src')
        urllib.urlretrieve(img_url, username + '/' + sname)
        
print 'DONE'
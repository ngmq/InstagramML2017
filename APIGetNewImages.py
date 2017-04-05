import json
import urllib
import requests
from requests.auth import HTTPBasicAuth
import time

_user = 'manhquan233@gmail.com'
_pass = 'VmJsb83qQBwyuk0PaiyxDrCUgzMZOlrQ'

# r = requests.get('http://challenges.instagram.unpossib.ly/api/live', auth=HTTPBasicAuth(_user, _pass))
# print r.status_code # 200
# print "==========================\n"
# print r.json()

predicted_codes = list()
username = ""
data = ""

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
    
    

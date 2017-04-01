import json
import urllib
import requests
from requests.auth import HTTPBasicAuth

_user = 'manhquan233@gmail.com'
_pass = 'VmJsb83qQBwyuk0PaiyxDrCUgzMZOlrQ'

r = requests.get('http://challenges.instagram.unpossib.ly/api/live', auth=HTTPBasicAuth(_user, _pass))

print r.status_code # 200
print "==========================\n"
print r.json()


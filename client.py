
import requests
from escherauth import EscherRequestsAuth

url = 'http://httpbin.org/get?foo=bin&abc=cba'
response = requests.get(url, auth=EscherRequestsAuth("xxx", {}, {'api_key': 'test', 'api_secret': 'xxx'}))

print response.status_code
print response.text

import json

import requests

# URL = "http://192.168.50.22:8081"
URL = "http://10.202.180.24:8080";

payload = {"user": "api-user", "password": "S0me-Passw0rd"}
headers = {'Content-type': 'application/json'}
response = requests.post("%s/login" % URL, data=json.dumps(payload), headers=headers)

print response.status_code
print response.text

token = response.text

enable = "false"

response = requests.post("%s/apiResource/%s/%s" % (URL, enable, token), headers=headers)

print response.status_code
print response.text

response = requests.post("%s/logout/%s" % (URL, token), headers=headers)
print response.status_code

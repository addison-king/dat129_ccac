"""
Brandyn Gilbert
    Wed Feb 26 20:47:37 2020
    Python 2 - DAT-129 - Spring 2020
    Homework #####
    TITLE OF HOMEWORK
"""
#PLAN

import requests
import json


header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

data = '{\n "apikey": "f538d2864846dd50a311ad8542b40f7d",\
          \n  "userkey": "XCXVRW13LTK0XFJY",\
          \n  "username": "falconfoe"\n}'

response = requests.post('https://api.thetvdb.com/login',
                          headers=header, data=data)
r_text = response.text
# print(r_text)
# print(type(r_text))
# input()

rj_text = json.loads(r_text)
# print(rj_text)
# print(type(rj_text))
# print(rj_text['token'])
# input()

token = rj_text['token']
token_auth = 'Bearer '+ token
auth = {'Authorization': token_auth}

headers = {
    'Accept': 'application/json',
    'Authorization': token_auth,
}

r = requests.get('https://api.thetvdb.com/series/73244', headers=headers)
# office = requests.get('https://api.thetvdb.com/episodes/110413', headers=headers)
text = r.text
j_text = json.loads(text)

print(j_text)
print(type(j_text))

out_file = open("test.json", "w")
json.dump(j_text, out_file, indent=1)


print(office.text)
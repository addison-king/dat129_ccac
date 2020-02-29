"""
Brandyn Gilbert
    Wed Feb 26 20:47:37 2020
    Python 2 - DAT-129 - Spring 2020
    Homework #####
    TITLE OF HOMEWORK
"""
#PLAN

import requests



headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

data = '{\n "apikey": "f538d2864846dd50a311ad8542b40f7d",\
         \n  "userkey": "XCXVRW13LTK0XFJY",\
         \n  "username": "falconfoe"\n}'

response = requests.post('https://api.thetvdb.com/login',
                          headers=headers, data=data)

# response = requests.post('https://api.thetvdb.com/episodes/73244',
#                          headers=headers, data=data)

print(response.content)



# headers = {
#     'Accept': 'application/json',
# }

# response = requests.get('https://api.thetvdb.com/episodes/73244', headers=headers)
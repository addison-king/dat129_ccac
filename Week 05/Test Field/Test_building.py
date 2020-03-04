"""
Brandyn Gilbert
    Sat Feb 29 13:39:20 2020
    Python 2 - DAT-129 - Spring 2020
    Homework #####
    TITLE OF HOMEWORK
"""
#PLAN
###########################
# 500 queries
# 95 seconds
# 5.263 queries / second
# 10,000 queries == 31m 35s
###########################
# 1000 queries
# 180 seconds
# 5.556 queries / second
# 10,000 queries == 30m
###########################


import requests
import json


def main():
    auth_headers = _get_token()
    _get_series(auth_headers)


def _get_token():
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
    rj_text = json.loads(r_text)
    token = rj_text['token']
    token_auth = 'Bearer '+ token

    auth_headers = {
    'Accept': 'application/json',
    'Authorization': token_auth,
    }

    return auth_headers


def _get_series(headers):
    series = 71000
    max_count = 0
    ended = 0
    running = 0
    errors = 0
    thinking = "."
    jstorage = []
    pp = 0
    while series < 72000:
        max_count += 1
        print(series)

        # thinking = thinking + "."

        url = 'https://api.thetvdb.com/series/'+ str(series)
        # print(url)
        # input()
        r = requests.get(url, headers=headers)
        series += 1
        text = r.text
        j_text = json.loads(text)
        jstorage.append(j_text)
        # print("=================================")
        # print(j_text)
        # print(type(j_text))
        # print("=================================")
        # print(jstorage)
        # print("=================================")
        # print(jstorage[pp])
        # pp += 1
        # print("=================================")
        # input()
        if 'Error' not in j_text:
            for i in j_text:
                if j_text[i]['status'] == 'Ended':
                    ended += 1
                else:
                    running += 1
        else:
            errors += 1




    print(ended, "of", max_count, "shows are no longer airing.")
    print(running, 'of', max_count, 'shows are still airing.')
    print(errors, 'of', max_count, 'are non-valid tv series numbers.')
    out_file = open("test.json", "a")
    json.dump(jstorage, out_file, indent=3)
    # json.dump(j_text, out_file, indent=3)
if __name__ == "__main__":
    main()

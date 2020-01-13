import requests
import json

USER = 'polesurka'
PASS = 'P@ssw0rd'

HOST = 'http://grafin-uranus.rd.ptsecurity.ru'
API_VER = ':7024/api/v1'

API_PATH = HOST + API_VER

def loginapi():
    url = 'http://grafin-uranus.rd.ptsecurity.ru:7024/api/v1/account/login'
   # url = API_PATH + '/account/login'
#    headers = {'Content-Type': 'application/json'}
    data = {"login" : "polesurka",
 "password" : "P@ssw0rd"}
    r = requests.post(url, json=data)
    #print(r)
    #print(r.content)

    if r.status_code != 200:
        print('Ответ сервера: ', r)
        raise Exception('Не удалось получить токен')

    #token = r.content
    #return token
    token = json.loads(r)
    print(token)
    return token.get('token')


#print(loginapi())


def get_inn():

    url = 'http://grafin-uranus.rd.ptsecurity.ru:7024/api/v1/antifraud/feeds/hashPassport/download'
    #r = requests.get(url, token=loginapi())
    headers = {'Authorization': 'Bearer ' + loginapi()}
    r = requests.get(url, headers=headers)
    print(r.content)

    if r.status_code != 200:
        print('Ответ сервера: ', r.text)
        raise Exception('Не удалось получить токен')

    return r.json()

print(get_inn())


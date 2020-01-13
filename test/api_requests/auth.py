import requests
import json

USER = 'polesurka'
PASS = 'P@ssw0rd'

HOST = 'http://grafin-uranus.rd.ptsecurity.ru'
API_VER = ':7024/api/v1'

API_PATH = HOST + API_VER

def login(login=USER, password=PASS):

    url = API_PATH + '/account/login'
#    headers = {'Content-Type': 'application/json'}
    params = {'login': login, 'password': password}
    r = requests.post(url, params=params)
#   print(r.text)
    print(r)

    if r.status_code != 200:
        print('Ответ сервера: ', r)
        raise Exception('Не удалось получить токен')

    token = json.loads(r)
#    print(r.status_code)
#    if r.status_code != 200:
 #       print('Ответ сервера: ', r.text)
  #      raise Exception('Не удалось получить токен')

#    token = json.loads(r.text)

    return token.get('token')


def get_inn(token):

    url = API_PATH + 'НАЙТИ урл фида'
    r = requests.get(url, token=token)

    if r.status_code != 200:
        print('Ответ сервера: ', r.text)
        raise Exception('Не удалось получить токен')

    return r.json()
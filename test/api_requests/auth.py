import requests
import json

USER = 'polesurka'
PASS = 'P@ssw0rd'

HOST = 'http://grafin-uranus.rd.ptsecurity.ru'
API_VER = ':7024/api/v1'

API_PATH = HOST + API_VER

#Логин. Получение токена

def loginapi():
    url = 'http://grafin-uranus.rd.ptsecurity.ru:7024/api/v1/account/login'
   # url = API_PATH + '/account/login'
    data = {"login" : "polesurka",
 "password" : "P@ssw0rd"}
    r = requests.post(url, json=data)
    #print(r)
    #print(r.content)

    if r.status_code != 200:
        print('Ответ сервера: ', r)
        raise Exception('Не удалось получить токен')

    token = r.text
    #print(token)
    return token

token = loginapi()

#Получение ИНН

def get_inn():

    url = 'http://grafin-uranus.rd.ptsecurity.ru:7024/api/v1/antifraud/feeds/inn/download'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + str(token)}
    r = requests.get(url, headers=headers)
    #print(headers)
    #print(r.content)

    #resp = r.json()
    resp = r.text
    return resp

resp = get_inn()
#resp1 = list(resp)
#print(type(resp))

get_inn()

#Проверка, есть ли интересующий ИНН в GET запросе

testapicheck = "772083338172"

def check(x):

    #через сплит и in, делим строку и ищем в ней содержание искомого инн
    resp1 = resp.split(',')
    #resp1 = resp.find(x)
    #return resp1
    #print(resp1)
    resp2 = list(resp1)
    print(type(resp2))
    #return resp2
    for i in x:
        if testapicheck in i:
            print("yes", testapicheck, i)
            break
    if testapicheck not in i:
        print('no data')

    return
print(check(testapicheck))
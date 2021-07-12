from os import times
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

user = "1095287"
pw = "h110622"

#start the session
session = requests.session()
response = session.get(urljoin)

url_login= "https://navi.mars.kanazawa-it.ac.jp/portal/student"

bs = BeautifulSoup(response.text, 'html.parser')

# Loggin
login_info = {
    "uid":user,
    "pw":pw,
    "_csrf":"f28e34c1-6ad6-462c-b518-86cf4c23d298",
}


#tokenの取得
_csrf = bs.find(attrs={'name':'_csrf'}).get('value')


#取得したtokenをpostするパラメーターに追加

login_info['_csrf'] = _csrf

login_info = session.post(url_login, data=login_info)
times.sleep(2)
print(login_info.text)

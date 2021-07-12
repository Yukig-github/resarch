import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

user = "1095287"
pw = "h110622"

target = "https://navi.mars.kanazawa-it.ac.jp/portal/student"

#start the session
session = requests.session()
response = session.get(target)
soup = BeautifulSoup(response.content, 'html.parser')
token = soup.find('input',{'name':'_csrf'}).get('value')

# loggin
login_in = {
    "uid":user,
    "pw":pw,
    "StudentLoginBtn": token,
    "password" : ""
}

#launch
response = session.post(target ,data=login_in)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)




import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

user = "JS-TESTER"
pw = "ipCU12ySxI"

#start the session
session = requests.session()

#login
login_info ={
    "username_mmlbbs6" : user,
    "password_mmlbbs6" : pw,
    "back" : "index.php",
    "mml_id" : "0"
}

url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"
res = session.post(url_login, data = login_info)
res.raise_for_status() # pick up some error

#mypage
soup = BeautifulSoup(res.text, "html.parser")
a = soup.select_one(".islogin a")
if a is None:
    print("It dosen't work")
    quit()

#相対URLを絶対URLに変換
url_mypage = urljoin(url_login, a.attrs["href"])
print("mypage = ", url_mypage)

#acess to my page
res = session.get(url_mypage)
res.raise_for_status()

#show favorite titles
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select("#favlist li > a")
for a in links:
    href = a.attrs["href"]
    title = a.get_text()
    print("-", title, ">", href)






import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Setting the user name and password
USER = "1095287"
PASS = "h110622"

# Start a settion
session = requests.session()

# Loggin
login_info = {
    "uid":USER,
    "pw":PASS,
    "_csrf":"f28e34c1-6ad6-462c-b518-86cf4c23d298",
    "password":"0"
}

# Action
url_login = "http://portal/student/inKITP0000001Login"
res = session.post(url_login, data=login_info)
res.raise_for_status() # check any error

print(res.text)

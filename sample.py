import requests
from bs4 import BeautifulSoup

load_url="https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)

for ele in soup.find_all("li"):
    print(ele.text)


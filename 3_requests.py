import requests
from bs4 import BeautifulSoup

res = requests.get("http://google.com")
res.raise_for_status()

with open("mygoogle.html", "w+", encoding="utf8") as f:
    f.write(res.text)

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=747269&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup)
webtoons = soup.find_all("td", class_="title")
ratings = soup.find_all("div", class_="rating_type")

for webtoon in webtoons:
    title = webtoon.text
    url = "https://comic.naver.com" + webtoon.a['href']

total_rate = 0
for rating in ratings:
    rate = rating.strong.text
    total_rate += float(rate)
    print(rate)
print(total_rate / len(ratings))
print(ratings)

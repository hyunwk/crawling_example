import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# print(res.text)
soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title.text)

# print(soup.a)
# print(soup.a.attrs)
# print(soup.a['href'])
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# print(soup.find("a", class_="Nbtn_upload"))
# # print(soup.find("a", href="/mypage/myActivity"))
# rank1 = soup.find("li", class_="rank01")
# print(rank1.a)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank1.a.text)
# print(rank2.a.text)
# print(rank3.a.text)
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.text)
# print(rank1.find_next_sibling("li"))
# print(rank2.parent)
webtoon = soup.find("a", text="반드시 해피엔딩-27화")
print(webtoon)

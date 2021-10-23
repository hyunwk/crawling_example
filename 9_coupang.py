import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", class_=re.compile("^search-product"))
for item in items:
    name = item.find("div", class_="name").text

    # 애플 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다>")
        continue
    price = item.find("strong", class_="price-value").text
    rate = item.find("em", class_="rating")
    if rate:
        rate = float(rate.text)
    else:
        print("<평점 없는 상품 제외>")
        continue
    rate_total_count = item.find("span", class_="rating-total-count")
    rate_total_count = int(rate_total_count.text[1:-1])
    if rate >= 4.5 and rate_total_count >= 50:
        print(
            f"name : {name}\nprice : {price}\nrate : {rate}\nrate_total_count : {rate_total_count}\n\n")

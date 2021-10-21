# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
from bs4 import BeautifulSoup

html_file = requests.get('https://askdjango.github.io/lv1/').text
soup = BeautifulSoup(html_file, "lxml")


# %%
seasons = soup.find_all('ul')
for season in seasons:
    vods = season.find_all('li')
    for vod in vods:
        extract_from_vod(vod)


# %%
def extract_from_vod(vod):
    title = vod.find('a').text
    link = vod.a['href']
    print(title, link)


# %%


# %%

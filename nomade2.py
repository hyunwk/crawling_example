# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
from bs4 import BeautifulSoup

html_file = requests.get('https://askdjango.github.io/lv2/').text
soup = BeautifulSoup(html_file, "lxml")


# %%
vods = soup.select('li[class=course]')
for vod in vods:
    print(vod.text, end='')
    print(vod.a['href'])
# %%


# %%


# %%

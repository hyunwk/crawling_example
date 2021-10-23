# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
import json
from bs4 import BeautifulSoup

json_url = ('https://askdjango.github.io/lv2/data.json')
json_string = requests.get(json_url).text

data_list = json.loads(json_string)
for data in data_list.values():
    for item in data:
        print(item['name'], item['url'])

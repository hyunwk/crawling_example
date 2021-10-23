import re
import requests
import json
url = 'https://askdjango.github.io/lv3/'
html = requests.get(url).text

# result = re.search(r'var s1_courses = (.+?);', html, re.S)
# print(result.group(1))
strs = re.findall(r'var s._courses = (.+?);', html, re.S)
for item in strs:
    result = re.search(r'"name": "(.+?)", "url": "(.+?)"', item, re.S)
    print(result.group(1), result.group(2))

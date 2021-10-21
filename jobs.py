# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import time
from typing import *
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


def extract_from_job(idx, job, unfamiliar_skill):
    date = job.find('span', class_='sim-posted').span.text  # .text.strip()
    skill = job.find('span', class_='srp-skills').text.strip()
    if 'few' in date and unfamiliar_skill not in skill:
        comp_name = job.find('h3', class_='joblist-comp-name').text.strip()
        more_info = job.header.h2.a['href']
        print(f' idx : {idx} ')
        print(f' Company Name : {comp_name}')
        print(f' Date : {date}')
        print(f' more_info : {more_info}')
        print()
# %%


def find_job():
    print('Put some skill that you are not familliar with')
    unfamiliar_skill = input('>')
    print(f'Fitering out {unfamiliar_skill}')

    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for idx, job in enumerate(jobs):
        extract_from_job(idx, job, unfamiliar_skill)

# %%
# rawJob


@dataclass
class Job:
    name: str
    skill: List[str]


# %%
if __name__ == '__main__':
    currentPath = os.getcwd()
    print(currentPath)
    while True:
        find_job()
        time_wait = 10
        print(f'Waiting {time_wait} minute')
        time.sleep(10 * time_wait)


# %%

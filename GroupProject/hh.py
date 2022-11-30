from os import name
import requests
import fake_useragent
from bs4 import BeautifulSoup
import time
import json

text = "python"
ua = fake_useragent.UserAgent()
items = 100
url = f"https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text={text}&items_on_page={items}"


def get_vacancy(html):
    name_vacancy = html.find('a').text
    link = html.find('a')['href']
    company = html.find(
        'div', {'class': 'vacancy-serp-item__meta-info-company'}).text
    city = html.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text

    return {'name': name_vacancy, 'company': company, 'location': city, 'link': link}


def get_max_page():

    data = requests.get(url, headers={"user-agent": ua.random})

    soup = BeautifulSoup(data.text, 'html.parser')

    paginator = soup.find_all(
        "span", {"class": "pager-item-not-in-short-range"})
    pages = []

    for page in paginator:
        pages.append(int(page.find("a").text))
    return pages[-1]


def get_hh_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Парсинг страницы {page+1}')
        result = requests.get(f'{url}&page={page}', headers={
                              "user-agent": ua.random})
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'serp-item'})
        for result in results:
            job = get_vacancy(result)
            jobs.append(job)
    return jobs

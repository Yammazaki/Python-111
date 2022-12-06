import requests
import fake_useragent
from bs4 import BeautifulSoup

# Создание переменных для их дальнейшего использования
text = "python"
ua = fake_useragent.UserAgent()
items = 100
url = f"https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text={text}&items_on_page={items}"

# Создание функции, в которой мы реализуем запись в словарь спарсенных значений одной вакансии:
# Наименование вакансии, компания, которая предлагает данную вакансию, город, в котором
# коспания размещена, а так же ссылку на данную вакансию на HH


def get_vacancy(html):
    name_vacancy = html.find('a').text
    name_vacancy = name_vacancy.partition(',')[0]
    link = html.find('a')['href']
    company = html.find(
        'div', {'class': 'vacancy-serp-item__meta-info-company'}).text
    company = ' '.join(company.partition(',')[0].split())
    city = html.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
    city = city.partition(',')[0]
    cash = html.find('span', {'data-qa': "vacancy-serp__vacancy-compensation"})
    if (cash == None):
        cash = 'Не указана'
    else:
        cash = ' '.join((cash.text).split())
    return {'name': name_vacancy, 'company': company, 'cash': cash, 'location': city, 'link': link}

# Поиск максимальной страницы, на которой мы проводим парсинг


def get_max_page():

    data = requests.get(url, headers={"user-agent": ua.random})

    soup = BeautifulSoup(data.text, 'html.parser')

    paginator = soup.find_all(
        "span", {"class": "pager-item-not-in-short-range"})
    pages = []

    for page in paginator:
        pages.append(int(page.find("a").text))
    return pages[-1]

# Функция записи каждой вакансии в общий список jobs, с которым вдальнейшем мы можем работать


def get_hh_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Парсинг страницы HeadHunter: {page+1}')
        result = requests.get(f'{url}&page={page}', headers={
                              "user-agent": ua.random})
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'serp-item'})
        for result in results:
            job = get_vacancy(result)
            jobs.append(job)
    return jobs

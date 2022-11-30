import time
import json
import csv

def save_to_csv(jobs):
    with open('vacancy.csv', 'w', encoding = 'UTF-8') as file:
        file.writelines(f'Должность,Компания,Адрес,Ссылка \n') 
        for job in jobs:
            vacancy = (list(job.values()))
            file.writelines(f'{vacancy}\n')

    with open('vacancy.csv', 'r', encoding = 'UTF-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    with open('vacancy.json', 'w', encoding = 'UTF-8') as file:
        json.dump(rows, file)
            

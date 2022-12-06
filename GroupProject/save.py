from datetime import datetime
import os
import glob
import csv
from xlsxwriter.workbook import Workbook
import json
import csv
import sqlite3

# Функция, котрая переводит наш список в файлы формата:
# 1. *.CSV формат
# 2. *.TXT формат
# 3. *.JSON формат
# 4. *.XLS  формат
# 5. в базу данных SQLite
# для дальнейшего их использвания


def save_to_csv(jobs):
    with open('vacancy.csv', 'w', encoding='UTF-8') as file:
        file.writelines(f'Должность,Компания,Доход,Адрес,Ссылка \n')
        for job in jobs:
            vacancy = (list(job.values()))
            file.writelines(f'{vacancy}\n')

    with open('vacancy.txt', 'w', encoding='UTF-8') as file:
        file.writelines(f'Должность,Компания,Доход,Адрес,Ссылка \n')
        for job in jobs:
            vacancy = (list(job.values()))
            file.writelines(f'{vacancy}\n')

    with open('vacancy.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    with open('vacancy.json', 'w', encoding='UTF-8') as file:
        json.dump(rows, file)

    for csvfile in glob.glob(os.path.join('.', 'vacancy.csv')):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()

    


# db = sqlite3.connect('database.db')
# with open('vacancy.json', encoding='utf-8-sig') as json_file:
#  json_data = json.loads(json_file.read())

# # Aim of this block is to get the list of the columns in the JSON file.
#  columns = []
#  column = []
#  for data in json_data:
#     column = list(data.keys())
#     for col in column:
#         if col not in columns:
#             columns.append(col)

# # Here we get values of the columns in the JSON file in the right order.
#  value = []
#  values = []
#  for data in json_data:
#     for i in columns:
#         value.append(str(dict(data).get(i)))
#         values.append(list(value))
#         value.clear()

# # Time to generate the create and insert queries and apply it to the sqlite3 database
#         create_query = """ CREATE TABLE IF NOT EXISTS vacancy(name_vacancy TEXT,company TEXT,cash TEXT,coordinats TEXT,link TEXT) """
#         insert_query = "insert into vacacy({0})values(?{1})".format(",".join(columns), ",?" * (len(columns)-1))
#  print("insert has started at " + str(datetime.now()))
#  c=db.cursor()
#  c.execute(create_query)
#  c.executemany(insert_query, values)
#  values.clear()
#  db.commit()
#  c.close()
#  print("insert has completed at " + str(datetime.now()))

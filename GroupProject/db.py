import sqlite3

def data_base(jobs):
    with sqlite3.connect('DataBase/database.db') as db:
        cursor=db.cursor()
        cursor.execute("DROP TABLE vacancy") 
        cursor.execute(""" CREATE TABLE IF NOT EXISTS vacancy(name_vacancy TEXT,company TEXT,cash TEXT,coordinats TEXT,link TEXT) """)
        for job in jobs:
            vacancyes = []
            vacancyes.append(list(job.values())) 
            for i in vacancyes:
                vacancy = i
            cursor.execute("""INSERT INTO vacancy VALUES (?, ?, ?, ?, ?);""", (vacancy[0], vacancy[1], vacancy[2], vacancy[3], vacancy[4]))
    cursor=db.cursor()
    db.commit()
    cursor.close()
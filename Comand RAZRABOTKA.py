import sqlite3

conn = sqlite3.connect('база_данных.db') #подключение к базе данных
cur = conn.cursor() #создание курсора
cur.execute('''
        CREATE TABLE IF NOT EXISTS users 
        (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL)
        ''') #создание таблицы

conn.commit()

cur.execute("INSERT INTO users (name, age) VALUES (?, ?)",("Алексей", 22))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)",("Джус", 35))

conn.commit() #сохранение изменений

cur.execute('SELECT * FROM users') #получение данных
rows = cur.fetchall() #получение данных
print(rows) #вывод
for row in rows:  #перебор строк
    print(row) #

conn.close() #закрытие


import sqlite3 
conn=sqlite3.connect('1.practice_site_3.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,

    SELECT * FROM users WHERE id=1
    users.query.get(1)


''')

conn.commit()
conn.close()
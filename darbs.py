
import sqlite3

# New DB + Connect
connection=sqlite3.connect('darbs.db')
cursor=connection.cursor()

# Create a table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS lietotaji(
                id INTEGER PRIMARY KEY,
                vards TEXT NOT NULL,
                uzvards TEXT NOT NULL,
                epasts TEXT NOT NULL UNIQUE
               )
               ''')



connection.commit()
connection.close()
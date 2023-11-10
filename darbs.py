
import sqlite3

# New DB + Connect
connection=sqlite3.connect('darbs.db')
cursor=connection.cursor()

# Create a table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS lietotaji(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
               )
               ''')

# Create 2nd table with relation 
cursor.execute('''
               CREATE TABLE IF NOT EXISTS pasutijumi(
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                product_name TEXT NOT NULL,
                ammount INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES lietotaji(id)
               )
               ''')

# Insert data into the users table
cursor.execute("INSERT INTO lietotaji (name, surname, email) VALUES (?,?,?)",('Edmunds','Berzons','edmundsberzons@roblox.com'))
cursor.execute("INSERT INTO lietotaji (name, surname, email) VALUES (?,?,?)",('Degmunds','Berzons','Degmundsberzons@riot.com'))

#Insert data into the purchase table
cursor.execute("INSERT INTO pasutijumi (user_id, product_name, ammount) VALUES (?,?,?)",(1,'RTX 3080',2))
cursor.execute("INSERT INTO pasutijumi (user_id, product_name, ammount) VALUES (?,?,?)",(2,'MOUSE',1))

connection.commit()
connection.close()
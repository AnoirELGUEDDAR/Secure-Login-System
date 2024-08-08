import sqlite3
import hashlib

# Connect to SQLite database
conn = sqlite3.connect('userdata.db')
cur = conn.cursor()

# Create table
cur.execute('''
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Add a sample user (username: user1, password: pass1234)
username1 = 'anoir69'
password1 = hashlib.sha256('anoir0'.encode()).hexdigest()
username2,password2="passin",hashlib.sha256('passin2021'.encode()).hexdigest()
username3,password3="hello",hashlib.sha256('world19'.encode()).hexdigest()
username4,password4="mwa",hashlib.sha256('password2013'.encode()).hexdigest()

cur.execute('INSERT INTO userdata (username, password) VALUES (?, ?)', (username1, password1))
cur.execute('INSERT INTO userdata (username, password) VALUES (?, ?)', (username2, password2))
cur.execute('INSERT INTO userdata (username, password) VALUES (?, ?)', (username3, password3))
cur.execute('INSERT INTO userdata (username, password) VALUES (?, ?)', (username4, password4))

# Commit and close
conn.commit()
conn.close()

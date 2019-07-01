import sqlite3

e_user_name_v = 'admin'
e_pas_v = 'admin'

conn = sqlite3.connect("soumil.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXIST shah (username TEXT,password TEXT) """)

cursor.execute("INSERT INTO shah (username,password) VALUES ('admin','admin')  ")

conn.commit()
cursor.close()
conn.close()
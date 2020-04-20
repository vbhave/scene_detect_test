# importing the sqlite3 module which would be required to create a Sqlite3 
# database
import sqlite3
conn = sqlite3.connect('output/test.db')

#if test.db previously exists, removing all records from it and starting anew
try:
	conn.execute('''DROP TABLE IF EXISTS SCENE_DETECTION;''')
	conn.commit()
except sqlite3.OperationalError:
	pass

# creating the scene_detection table
conn.execute('''CREATE TABLE SCENE_DETECTION		
		(NAME TEXT PRIMARY KEY NOT NULL,
		ENVIRONMENT TEXT NOT NULL,
		CATEGORIES TEXT NOT NULL,
		ATTRIBUTES TEXT NOT NULL);''')

# executing the transaction and in the end closing it
conn.commit()
conn.close()	
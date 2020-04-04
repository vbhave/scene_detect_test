import sqlite3
conn = sqlite3.connect('output/test.db')

#(ID INT PRIMARY KEY NOT NULL,
try:
	conn.execute('''DROP TABLE IF EXISTS SCENE_DETECTION;''')
	conn.commit()
except sqlite3.OperationalError:
	pass

conn.execute('''CREATE TABLE SCENE_DETECTION		
		(NAME TEXT PRIMARY KEY NOT NULL,
		ENVIRONMENT TEXT NOT NULL,
		CATEGORIES TEXT NOT NULL,
		ATTRIBUTES TEXT NOT NULL);''')

conn.commit()
conn.close()	

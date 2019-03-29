import sqlite3


con=sqlite3.connect("books_db.sqlite3")
cur = con.cursor()

try:
	cur.execute("""CREATE TABLE books(id INTEGER PRIMARY KEY, name TEXT, rating INTEGER)""")
except sqlite3.OperationalError:
	print("Table already exists")
cur.execute("""INSERT INTO books VALUES(1,"Eleven Minutes",7)""")
cur.execute("""INSERT INTO books VALUES(2,"The Kite Runner",9)""")
cur.execute("""INSERT INTO books VALUES(3,"The Great Gatsby",8)""")

con.commit()

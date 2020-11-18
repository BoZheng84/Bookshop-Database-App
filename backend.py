import sqlite3

def connect():
    conn = sqlite3.connect("books.db")  # let's call books.db database.
    cur = conn.cursor()  # we establish an connection to the database.
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")  # need to execute an SQL statement.
    conn.commit()
    conn.close()

# Creating an insert function (Add Entry)
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")  
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,  ?, ?, ?, ?)", (title, author, year, isbn))  # NULL means python will automatically create the id.
    conn.commit()
    conn.close()

# Creating View All function, so this will fetch all the rows of the table.
def view():
    conn = sqlite3.connect("books.db")  
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    # conn.commit()  # because this would be select statement so will not perform any changes to the database, so we don't use commit method.
    rows = cur.fetchall()
    conn.close()
    return rows

# Creating a search function
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")  
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# Creating a delete function
def delete(id):
    conn = sqlite3.connect("books.db")  
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))  
    conn.commit()
    conn.close()

# Creating a update function
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")  
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))  
    conn.commit()
    conn.close()
 



connect()
# insert("The Sun", "John Smith", 1918, 913123132)
# delete(3)
# update(2, "The moon", "John Smooth", 1917, 99999)
# print(view())
# print(search(author="John Smith"))
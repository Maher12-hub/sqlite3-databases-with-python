import sqlite3
mydb=sqlite3.connect('customer.db')
mycursor=mydb.cursor()
'''
mycursor.execute("""CREATE TABLE customers(
    first_name text,
    last_name text,
    email text)""")
'''
#mycursor.execute("INSERT INTO customers VALUES('maher','rehman','maheribne12@gmail.com')")
#mycursor.execute("DELETE FROM customers where first_name='maher'")
##customer_list=[('mehanaz','sunny','mehanazctg@gmail.com'),('rahi','rahman','rahibinte@gmail.com')]
##sql="INSERT INTO customers VALUES(?, ?, ?)"
#mycursor.executemany(sql,customer_list)
#mycursor.execute("UPDATE customers SET first_name='Rahi' WHERE rowid=3")
#mycursor.execute("DELETE FROM customers WHERE rowid=3")
#mycursor.execute("INSERT INTO customers VALUES('bappu','tahmim','tahmim_bappu@gmail.com')")
#mycursor.execute("INSERT INTO customers VALUES('neloy','rahman','neloyrahman@gmail.com')")
mydb.commit()
#mycursor.execute("SELECT rowid, * FROM customers")
#mycursor.execute("SELECT * FROM customers WHERE last_name='sunny'")
#mycursor.execute("SELECT rowid,* FROM customers WHERE  last_name LIKE '%ah%' OR rowid=1 ")
mycursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")
myresult=mycursor.fetchall()
for result in myresult:
    print(result)
#mydb.close()
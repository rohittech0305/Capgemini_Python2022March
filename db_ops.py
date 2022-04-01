import sqlite3

dbh=sqlite3.connect('mydatabase')
c=dbh.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS employee ( ename TEXT, exp TEXT, tech TEXT)")

def insert_records():
    c.execute("INSERT INTO employee VALUES('Vijay',15,'Python')")
    c.execute("INSERT INTO employee VALUES('Ajit',20,'Python')")
    dbh.commit()
    c.close()
    dbh.close()

def update_records():
    c.execute("UPDATE employee SET tech='AIML' WHERE ename='Levin'")
    dbh.commit()
    c.close()
    dbh.close()

def delete_records():
    c.execute("DELETE FROM employee WHERE tech != 'Python' ")
    dbh.commit()
    c.close()
    dbh.close()

def fetch_records():
    c.execute("SELECT * FROM employee")
    #fetchone, fetchmany, fetchall
    #print(c.fetchone())
    #print(c.fetchmany(1))
    for row in c.fetchall():
        if row[1]=='20':
            print(row[0].upper() + " ---> "+ str(row[1])+" ---> "+ row[-1].upper())
#create_table()
#insert_records()
#update_records()
#delete_records()
fetch_records()
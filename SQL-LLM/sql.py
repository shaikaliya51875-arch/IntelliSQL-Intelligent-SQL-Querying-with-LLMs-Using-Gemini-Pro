import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
CREATE TABLE Students(name VARCHAR(30), class VARCHAR(10), marks INT, company VARCHAR(30));

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''cursor.execute ("insert into Students values('Sijo', 'Btech', 75, JSW')''') 
cursor.execute('''cursor.execute("insert into Students values('lijo', 'MTech', 69, 'TCS")''') 
cursor.execute('''cursor.execute("insert into Students values('Rijo', 'BSc, 79, 'WIPRO")''') 
cursor.execute('''cursor.execute("insert into Students values('Sibin', 'SC, 89, 'INFOSYS")''') 
cursor.execute('''cursor.execute("insert into Students values('Dilsha', 'MCom', 99, 'Cyient')''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
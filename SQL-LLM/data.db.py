import sqlite3

## Connectt to SQlite
conn=sqlite3.connect("datt.db")

# Create a cursor object to insert record,create table

cursor=conn.cursor()

## create the table
table_info="""CREATE TABLE Students(name VARCHAR(30), class VARCHAR(10), marks INT, company VARCHAR(30));"""
cursor.execute(table)

## Insert Some more records

cursor.execute('''insert into Students values('Sijo', 'Btech', 75, JSW')''') 
cursor.execute('''insert into Students values('lijo', 'MTech', 69, 'TCS")''') 
cursor.execute('''insert into Students values('Rijo', 'BSc, 79, 'WIPRO")''') 
cursor.execute('''insert into Students values('Sibin', 'SC, 89, 'INFOSYS")''') 
cursor.execute('''insert into Students values('Dilsha', 'MCom', 99, 'Cyient')''')

## Disspaly ALl the records

print("Data Inserted in the table:")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
conn.commit()
conn.close()

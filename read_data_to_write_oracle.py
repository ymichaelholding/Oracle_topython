import cx_Oracle
import csv
import os
import pandas

conn = cx_Oracle.connect('hr/hr@Xe')
print(conn)
ver = conn.version.split(".")
print(ver)
#The cursor() method opens a cursor for statements to use.
cur = conn.cursor()
res=[]
#The execute() method parses and executes the statement.
res= cur.execute('select *  FROM EMPLOYEES')
headers=[]
for i in res.description:
    headers.append(i[0])
print(headers)
# Open a file for writing, and create a csv.writer instance:
with open("DATA.csv", "w") as f:
    fcsv = csv.writer(f)
    # Write header row, then write the rest of the data:
    fcsv.writerow(headers)
    record=[]
    for record in res:
            fcsv.writerow(record)



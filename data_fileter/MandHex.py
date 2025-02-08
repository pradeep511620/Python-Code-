import csv
import re
import pymysql
from fractions import Fraction
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="filter"
)
mycursor = mydb.cursor()

filename = "/home/Desktop/pradeep/filter/file.csv"
with open(filename, 'r', encoding="utf-8") as f:
    df = csv.reader(f)

#     for row in df:
#         sql = "INSERT INTO DATA(MPN ,L3,datatype,superAtt,type,ATTRIBUTE,raw_value,e,polarity1,value1,unit1,polarity2,value2,unit2,value_pairing) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s)"
#         val = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
#         mycursor.execute(sql, val)
#     print("done")
# mydb.commit()


sql1 = "SELECT * from DATA"
mycursor.execute(sql1)
myresult = mycursor.fetchall()
# print(myresult)
#
for d in myresult:

    id = d[0]
    f = d[10]
    t = d[7]

    if 'M' in f and "Me" not in f and ' ' not in f and "Ma" not in f and "AS" not in f:
        e = f.split("M")
        value1 = e[0]+e[1]
        p = "M"
        val = (p, value1, id)
        sql = "UPDATE DATA SET polarity1=%s ,value1=%s WHERE id=%s"
        mycursor.execute(sql, val)
mydb.commit()




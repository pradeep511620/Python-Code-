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

filename = "/home/tajender/filter/file.csv"
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

    id=d[0]
    f = d[10]
    t = d[7]

    if 'ga' in f and '/' in f:
        a = f.split('rp_')[1]
        b = a.strip('ga')
        c = "rp_"
        if ' ' not in b:
            d = str(round(float(Fraction(b)), 3))
            e = c + d
            val = (e, id)
            print(e)
            sql = "UPDATE DATA SET value1=%s WHERE id=%s"
            mycursor.execute(sql, val)
        elif ' ' in b:
            i = b.split(' ')[0]
            i1 = b.split(' ')[1]
            d1 = round(float(Fraction(i1)), 3)
            d2 = str(float(i) + d1)
            print(d2)
            e = c + d2
            print(e)
            val = (e, id)
            sql = "UPDATE DATA SET value1=%s WHERE id=%s"
            mycursor.execute(sql, val)
mydb.commit()


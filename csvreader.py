import csv
import re
import pymysql
from fractions import Fraction

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="data_filter"
)
mycursor = mydb.cursor()

filename = "/home/pradeep/Downloads/csv/allfiles.csv"
with open(filename, 'r', encoding="utf-8") as f:
    data = csv.reader(f)
    # for x in data:
    #     print(x)

    # for row in data:
    #     x = "INSERT INTO DATA(MPN, L3, DataType, SuperAtt, Type, ATTRIBUTE, raw_value, e, polarity1, value1, unit1, polarity2, value2, unit2, value_pairing) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)"
    #     val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
    #     mycursor.execute(x, val)
    #     print("execute")
    #     mydb.commit()

sql1 = "SELECT * from DATA"
mycursor.execute(sql1)
myresult = mycursor.fetchall()
# print(myresult)

for d in myresult:
    id = d[0]
    f = d[10]  # value1
    x = d[7]  # row_value ("")
    # print(f)
    if f == "":
        val = (x, id)
        sql = "UPDATE DATA SET value1=%s WHERE id=%s"
        mycursor.execute(sql, val)

    if '/' in f and ',' not in f and '-' not in f and '(' not in f and 'to' not in f and '"' in f:
        a = f.split('rp_')[1]
        b = a.strip('"')
        c = "rp_"
        if ' ' not in b:
            d = str(round(float(Fraction(b)), 3))
            e = c+d
            val = (e, id)
            print(val)
            sql = "UPDATE DATA SET value1=%s WHERE id=%s"
            mycursor.execute(sql, val)
    #
    #     elif ' ' in b:
    #         i = b.split(' ')[0]
    #         i1 = b.split(' ')[1]
    #         d1 = round(float(Fraction(i1)), 3)
    #         d2 = str(float(i) + d1)
    #         print(d2)
    #         e = c + d2
    #         val = (e, id)
    #         sql = "UPDATE DATA SET value1=%s WHERE id=%s"
    #         mycursor.execute(sql, val)

    if '"' in x:
        e = "inch"
        val = (e, id)
        # print(val)
        sql = "UPDATE DATA SET unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # mydb.commit()

    elif " ' " in x:
        g = "Feet"
        val = (g, id)
        sql = "UPDATE DATA SET unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # mydb.commit()
    elif 'mm' in x:
        e = "mm"
        val = (e, id)
        # print(val)
        sql = "UPDATE DATA SET unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # mydb.commit()

    elif 'ga' in x:
        e = "ga"
        val = (e, id)
        sql = "UPDATE DATA SET unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # mydb.commit()


#     if 'psi' in f:
#         e=f.split(" ")
#         val = (e[0],e[1], id)
#         sql = "UPDATE DATA SET value1=%s,unit1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#     if f == '':
#         id = str(d[0])
#         val = T
#         v = (val, id,)
#         sql = "UPDATE DATA SET value1=%s WHERE id=%s"
#         mycursor.execute(sql, v)
#
#
# mydb.commit()

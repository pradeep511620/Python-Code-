import csv
import pymysql

from fractions import Fraction

obj1 = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="lms"
)
print("Database Connection ")
mycursor = obj1.cursor()

filename = "/home/pradeep/Downloads/csv/Weld_Nuts.csv"
with open(filename, 'r', encoding='utf-8') as f:
    data = csv.reader(f)
    # for x in data:
    #     print(x)

    # for row in data:
    #     sql = "INSERT INTO Weld_Nuts (MPN, L3, DataType, SuperAtt, Type, ATTRIBUTE, VALUE, PreP, value1, unit1, PostP, value2, unit2, key_value) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #     val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
    #     mycursor.execute(sql, val)
    # print("Insert Into Data")
    # obj1.commit()

# Importing module
import csv
import glob
import pymysql

obj1 = pymysql.connect(
    host="localhost",
    user="root",
    port=3307,
    password="",
    database="lms"
)
print("Database Connection ")
mycursor = obj1.cursor()

filename = glob.glob(r'/home/pradeep/Downloads/Nov-uk/*')  # Read main folder Read file name
print(len(filename))
# print(filename)
for files in filename:
    # print(files)
    result = glob.glob(files + '/*')  # Read sub folder and csv files
    for f in result:
        # print(f)
        if "excluded_log" not in f:
            print(f)
            with open(f, 'r', encoding='utf-8') as ff:
                data = csv.reader(ff)
                for row in data:  # print all data and read files
                    sql = "INSERT INTO data_import (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                        row[11],
                        row[12], row[13], row[14])
                    mycursor.execute(sql, val)
print("Insert Into Data")
obj1.commit()
#                 for row in data:
#                     A = row[0], B = row[1], C = row[2], D = row[3], E = row[4], F = row[5], G = row[6], H = row[7], I = row[8], J = row[9], K = row[10]
#                     L = row[11], M = row[12], N = row[13], O = row[14], print(O)
#                     print()

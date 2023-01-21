import csv
import mysql.connector

obj1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="data_filter")
print("created connection")
# print(obj1.connection_id)
mycursor = obj1.cursor()  # open a cursor

"""
# create a new database
mycursor.execute("CREATE DATABASE student")  
print("created database")
"""

"""
# to check databases in database
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
"""

"""
# Create a Table in data_filter database
mycursor.execute("CREATE TABLE data (id INT AUTO_INCREMENT PRIMARY KEY,"
                 " MPN VARCHAR(40),"
                 " L3 VARCHAR(30),"
                 " HEADING VARChar (35),"
                 " SUBHEADING VARCHAR(35),"
                 " ATTRIBUTE VARCHAR(55)"
                 " VALUE VARCHAR(55)"
                 " VALUE1 VARCHAR(55)")
print("create table")
"""

with open(r'/home/pradeep/Downloads/csv/rough4.csv', 'r') as datas:
    data = csv.reader(datas)
    # for row in data:
    #     x = "INSERT INTO data(id, MPN ,L3,HEADING,SUBHEADING,ATTRIBUTE,value) VALUES (%s,%s, %s,%s,%s, %s,%s)"
    #     val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    #     mycursor.execute(x, val)
    # print("execute command")
    # obj1.commit()
    # print(row)

fatch_data = "SELECT * from data"
mycursor.execute(fatch_data)
result = mycursor.fetchall()
b2 = []
# print(result)

for row in result:
    id = (row[0])
    res = [int(x) for x in str(id)]
    print(res)
    ATTRIBUTE = row[5]
    VALUE1 = row[7]
    b2.append(row[5])
#     # print(b2)
    l = [1]
    if 'Diameter' == ATTRIBUTE:
        l.pop()
        l.append(b2)
        val = (l, id)
        sql = "UPDATE DATA SET VALUE1=%s WHERE id=%s"
        mycursor.execute(sql, val)


# print(ATTRIBUTE)
#         if ATTRIBUTE == 'Diameter':
#             x = int(id)-1
#             b.append(x)
#             # print(b)
#             y = row
#             b2.append(y)
#     # print(b)
#     # print(b2)
#     for ids in b:
#         # print(type(ids))
#         # print(ids)
#         for ids1 in b2:
#             # print(type(ids1))
#             if ids == int(ids1[0]):
#                 id = ids[0]
#                 print(id)
#                 print(len("ok"))

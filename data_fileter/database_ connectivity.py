import mysql.connector
obj1 = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="students")
print("created connection")
# print(obj.connection_id)
mycursor = obj1.cursor()  # open a cursor
# """mycursor.execute("CREATE DATABASE student")  # create a new database
# print("created database")"""
# to check databases in database
# """mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)"""

# crate a table in database
# mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY,"
#                  " First_Name VARCHAR(40),"
#                  " Last_Name VARCHAR(30),"
#                  " Email_Id VARChar (35),"
#                  " City VARCHAR(35),"
#                  " Address VARCHAR(55)")
# # print("create table")






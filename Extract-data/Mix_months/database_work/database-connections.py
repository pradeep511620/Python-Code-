import csv
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1', database='data_tab', user='root', password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
# cursor.execute("CREATE TABLE data (`url` VARCHAR(450), `entity_id` VARCHAR(450) , `value` VARCHAR(500), `image_url` VARCHAR(500))")
# print('table Created here successfully ')

cursor.execute("select * from sheet limit 2")
myresult = cursor.fetchall()
# print(myresult)
for row in myresult:
    url = row[0]
    entity_id = row[1]
    value = row[2]
    image_url = row[3]
    print(url)

    # l3_Name =

# path = "D:/LOG-ANALYZER/SG-AU/SG-AU-DEC-LOG/"
# path = "/home/pradeep/Downloads/au/"
# dirs = os.listdir(path)
# for dir1 in dirs:
#     if os.path.isdir(path + dir1):
#         # print('newFolder')
#         filepath = path + dir1 + '/'
#         files = os.listdir(filepath)
#         for files1 in files:
#             # print("New File")
#             if ".html" not in files1:
#                 if "sg_au_all_" in files1:
#                     print(files1)

from bs4 import BeautifulSoup
import mysql.connector
import requests
from mysql.connector import Error

# try:
mydb = mysql.connector.connect(host='development-uk.c5tedj3txtxy.eu-west-1.rds.amazonaws.com',
                               database='PRADEEP-SCRAPING-DATA', user='raptoradmin', password='Raptorpwa2020')
#     connection = mysql.connector.connect(host='development-uk.c5tedj3txtxy.eu-west-1.rds.amazonaws.com',
#                                          database='PRADEEP-SCRAPING-DATA', user='raptoradmin', password='Raptorpwa2020')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)
#
# except Error as e:
#     print("Error while connecting to MySQL", e)
mycursor = mydb.cursor()

# sql = "SELECT * from dba_324_static"
sql = "SELECT * from dba_324_dynamic "
mycursor.execute(sql)
result = mycursor.fetchall()
# print(result)
for row in result:
    id = str(row[0])
    url = row[1]
    title = row[3]
    meta = row[4].replace('\n', '')
    desc = row[5]

    print('url...', url)

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    title_des = soup.find("title").string.replace(' | Raptor Supplies Worldwide', '')
    print('d', title)
    print('p', title_des)

    meta_des = soup.find("meta", attrs={"name": "description"}).get("content").replace(' | Worldwide Delivery', '')
    print('d', meta)
    print('p', meta_des)

    description = soup.find('div', class_="lets-talk").find('p')
    description_d = str(description)
    description_data = description_d[3:-4].replace('amp;', '').replace('/', '')
    print('d', desc)
    print('p', description_data)

#     if desc == description_data and meta == meta_des and title == title_des:
#         print('same')
#         # update = "UPDATE dba_324_static SET meta_updated = 'same', description_updated = 'same' WHERE id  = '" + id + "'"
#         # print(update)
#         # mycursor.execute(update)
#         # print(mycursor.rowcount, 'row update')
#     else:
#         print('different data')
#
# mydb.commit()

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
sql = "SELECT * from dba_324_dynamic"
mycursor.execute(sql)
result = mycursor.fetchall()
# print(result)
for row in result:
    id = str(row[0])
    url = row[1]
    meta = row[2].replace('\n', '')
    desc = row[4]

    print('url...', url)
    metas = meta
    print('Meta...database', metas)

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    meta_des = soup.find("meta", attrs={"name": "description"}).get("content").strip().replace(' | Worldwide Delivery', '')
    print('Meta...webpage', meta_des)

    description = soup.find('section', class_="about-brand").find('p')
    description_d = str(description)
    description_data = description_d[3:-4].replace('amp;', '')
    print('d', desc)
    print('p', description_data)

    if desc == description_data and metas == meta_des:
        print('same')
        update = "UPDATE dba_324_static SET meta_updated = 'same', description_updated = 'same' WHERE id  = '" + id + "'"
        print(update)
        mycursor.execute(update)
        print(mycursor.rowcount, 'row update')
    else:
        print('different data')

# mydb.commit()

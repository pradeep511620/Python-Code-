import csv
import re
from datetime import datetime
import os
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='logs',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

path = "D:/dec-com/"
dirs = os.listdir(path)
count = 0
for dir1 in dirs:
    if os.path.isdir(path + dir1):
        print('newFolder')
        filepath = path + dir1 + '/'
        files = os.listdir(filepath)
        for files1 in files:
            print("New File")
            print(files1)
            if ".html" not in files1:
                if os.path.isfile(filepath + files1):
                    with open(filepath + files1, 'r') as f:
                        reader = csv.reader(f)
                        for rows1 in reader:
                            if len(rows1) == 2:
                                row = rows1[0] + rows1[1]
                            else:
                                row = rows1[0] + '"'
                            rows = re.findall(r'[^"\s]\S*|".+?"', row)
                            if len(rows) != 15:
                                for x in range(len(rows), 15):
                                    rows.append('-')
                            date_row = rows[3].replace('[', '')
                            date_object = datetime.strptime(date_row, "%d/%b/%Y:%H:%M:%S").strftime("%d%b%Y")
                            rows[4] = rows[4].replace(']', '')
                            if ".php" in rows[5]:
                                continue
                            elif ".png" in rows[5]:
                                continue
                            elif "/pub/" in rows[5]:
                                continue
                            elif "/customer/" in rows[5]:
                                continue
                            elif ".css" in rows[5]:
                                continue
                            elif ".html" in rows[5]:
                                continue
                            elif ".js" in rows[5]:
                                continue
                            elif ".css" in rows[5]:
                                continue
                            sql = "INSERT INTO log_com (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p) VALUES (%s,%s,%s,%s,%s,%s,%s,%s," \
                                  "%s,%s,%s,%s,%s,%s,%s,%s) "
                            val = (
                                rows[0].replace('"', ''), rows[1].replace('"', ''), rows[2].replace('"', ''),
                                date_object,
                                rows[
                                    4].replace('"', ''), rows[5].replace('"', ''), rows[6].replace('"', ''),
                                rows[7].replace('"', ''), rows[
                                    8].replace('"', ''), rows[9].replace('"', ''), rows[10].replace('"', ''),
                                rows[11].replace('"', ''), rows[
                                    12].replace('"', ''), rows[13].replace('"', ''), rows[14].replace('"', ''),
                                date_row)
                            cursor.execute(sql, val)
                    print("Record inserted")
                    connection.commit()

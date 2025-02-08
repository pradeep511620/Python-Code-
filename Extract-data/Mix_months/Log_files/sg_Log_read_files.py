import csv
import re
from datetime import datetime
import os
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1', database='lms', user='root', password='', port=3307)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
#   path = "D:/LOG-ANALYZER/SG-AU/SG-AU-DEC-LOG/"

path = "/home/pradeep/Downloads/sg/ssg/"
dirs = os.listdir(path)
count = 0
for dir1 in dirs:
    if os.path.isdir(path + dir1):
        # print('newFolder')
        filepath = path + dir1 + '/'
        files = os.listdir(filepath)
        for files1 in files:
            # print("New File")
            if ".html" not in files1:
                if "sg_au_all_" in files1:
                    # if ".html" not in files1 and "sg_au_ads_" not in files1 and "sg_au_bing_" not in files1 and "sg_au_exclude_" not in files1 and "sg_au_gclid_" not in files1 and "sg_au_googlebot_" not in files1:
                    print(files1)
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
                                date_row = rows[6].replace('[', '')
                                date_object = datetime.strptime(date_row, "%d/%b/%Y:%H:%M:%S").strftime("%d%b%Y")
                                rows[7] = rows[7].replace(']', '')
                                rows[8] = rows[8].replace('GET ', '')
                                rows[8] = rows[8].replace(' HTTP/2.0', '')
                                rows[8] = rows[8].replace(' HTTP/1.1', '')
                                if ".php" in rows[8]:
                                    continue
                                elif ".png" in rows[8]:
                                    continue
                                elif "/pub/" in rows[8]:
                                    continue
                                elif "/customer/" in rows[8]:
                                    continue
                                elif ".css" in rows[8]:
                                    continue
                                elif ".html" in rows[8]:
                                    continue
                                elif ".js" in rows[8]:
                                    continue
                                elif ".css" in rows[8]:
                                    continue
                                sql = "INSERT INTO sg_custom (`domain`,`ip`,`date`,`url`,`url_status`,`date_time`) VALUES (%s,%s,%s,%s,%s,%s) "
                                val = (rows[0].replace('"', ''), rows[1].replace('"', ''), date_object,
                                       rows[8].replace('"', ''), rows[9].replace('"', ''), date_row)
                                # sql = "INSERT INTO sg (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p) VALUES (%s,%s,%s,%s,%s,%s," \
                                #      "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                """val = (
                                    rows[0].replace('"', ''), rows[1].replace('"', ''), rows[2].replace('"', ''),
                                    rows[3].replace('"', ''),
                                    rows[4].replace('"', ''), rows[5].replace('"', ''), date_object,
                                    rows[7].replace('"', ''), rows[
                                        8].replace('"', ''), rows[9].replace('"', ''), rows[10].replace('"', ''),
                                    rows[11].replace('"', ''), rows[
                                        12].replace('"', ''), rows[13].replace('"', ''), rows[14].replace('"', ''),
                                    date_row)"""
                                # print(sql)
                                # print(val)
                                if (cursor.execute(sql, val)):
                                    print(sql)
                                    print(val)
                    print("Record inserted")
                    connection.commit()

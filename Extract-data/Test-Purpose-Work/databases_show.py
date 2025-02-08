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
# with open(r"C:\Users\lenovo\Downloads\tiny_im_url.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # print(csv_reader)
#     # for data in csv_reader:
#         # print(data)
sql_select_Query = "select * from sheet limit 5"
data = connection.cursor()
cursor.execute(sql_select_Query)
# get all records
records = cursor.fetchall()
for row in records:
    url = row[0]
    print(url)


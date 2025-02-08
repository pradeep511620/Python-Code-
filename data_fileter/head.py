import csv

import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="filter"
)
mycursor = mydb.cursor()

filename = r'/home/pradeep/Downloads/csv/file.csv'
with open(filename, 'r', encoding="utf-8") as f:
    df = csv.reader(f)

    # for row in df:
    #     sql = "INSERT INTO Diameter(MPN ,L3,HEADING,SUBHEADING,ATTRIBUTE,value) VALUES (%s, %s,%s, %s,%s, %s)"
    #     val = (row[0],row[1],row[2],row[3],row[4],row[5])
    #     mycursor.execute(sql, val)
    # print("done")
    # mydb.commit()

sql1 = "SELECT * from Diameter"
mycursor.execute(sql1)
myresult = mycursor.fetchall()
d1 = 0
f = []
for d in myresult:
    id = str(d[0])
    mpn = d[1]
    attr = d[5]
    value = d[6]
    # print(id,value)
    f.append(d)

l = []
print(l)
for j in f:
    # print(j[5])
    for k in l:
        # if j[5]=='rp_Diameter ':
        #     id = j[0]
        #     T = k[5]
        #     val = (T, id)
        #     sql = "UPDATE Diameter SET U=%s WHERE id=%s"
        #     mycursor.execute(sql, val)

        if j[5] == 'rp_Length ' or j[5] == 'rp_Thickness ':
            print("done")
            id = j[0]
            T = k[7]
            val = (T, id)
            sql = "UPDATE Diameter SET U=%s WHERE id=%s"
            mycursor.execute(sql, val)
    if j[0] != 2:
        l.pop()
    l.append(j)

mydb.commit()

import csv

with open(r'/home/pradeep/Downloads/csv/files.csv', 'r') as datas:
    data = csv.reader(datas)
    for row in data:
        # print(row)
        date_type = row[2]
        print(date_type)
        if date_type == 'Discrete':
             pass





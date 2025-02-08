import csv

with open(r'/home/pradeep/Downloads/csv/rough3.csv', 'r') as datas:
    data = csv.reader(datas)

    l = []
    for row in data:
        id = row[0]
        MPN = row[1]
        ATTRIBUTE = row[5]
        VALUE1 = row[7]
        print(VALUE1)

        if row[5] == 'Diameter':
            row[7] = l[0]
    l.pop()
    l.append(ATTRIBUTE)

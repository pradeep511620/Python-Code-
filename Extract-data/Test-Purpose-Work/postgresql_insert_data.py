# import psycopg2
# from psycopg2 import sql
# import csv
# import json
# conn = psycopg2.connect(
#     dbname="postgres",
#     user="postgres",
#     password="7789",  # Provide the correct password here
#     host="::1",
#     port="5432"
# )
#
# # Create a cursor object
# cur = conn.cursor()
# print('Connection is created')
#
#
# file_path = 'C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Thomson.com/data/thomson-all-data11.csv'

# # Open the CSV file
# with open(file_path, 'r', encoding='latin1') as ff:
#     data = csv.reader(ff)
#     next(data)
#     for row in data:
#         row_data = row[0:22]
#         # print(row_data[-1])
#         sql = ("INSERT INTO scraped_pd_data ("
#                "brand, catlvl1, catlvl2, catlvl3 ,url, title, price_value, usd, unit, "
#                "shipping_weight, breadscrumbs, image_urls, mpn, specification_1, specification_2, datasheets, "
#                "product_description_1, product_description_2, accessories,video_links,miscellaneous,scraped_by,created_)"
#                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#                )
#         # print(sql)
#         val = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5], row_data[6], row_data[7],
#                row_data[8], row_data[9], row_data[10], row_data[11],row_data[12], row_data[13], row_data[14], row_data[15],
#                row_data[16], row_data[17], row_data[18], row_data[19], row_data[20], row_data[21], row_data[22], row_data[23])
#         # mycursor.execute(sql, val)
#         val = tuple(row_data)  # Convert row_data to a tuple
#         cur.execute(sql, val)
#


# Importing required libraries
import csv
import psycopg2

# Parameters to access the database


db_params = {
    'host': 'cleancatalograptorsupplies.cy63lzu6l3sf.ap-south-1.rds.amazonaws.com',
    'database': 'raptor_db',
    'user': 'rp_scraping_team',
    'password': 'RaptorSuppliesScrapTeam#2024',
    'port': '5432'
}

# Your file
csv_file_path = 'C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Sealmaster/data/Sealmaster-all-data - Copy.csv'

# Table name where data need to be inserted
table_name = 'raw_db.scraped_pd_data'

# Creating connection using Db parameters
conn = psycopg2.connect(**db_params)

# Creating a cursor
cur = conn.cursor()

# Opening the file and Inserting the data row by row using insert query
with open(csv_file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    row_counter = 0
    for row_data in reader:
        print(row_data)
        row_counter += 1
        if row_counter >= 6:
            break

        # val = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5], row_data[6], row_data[7], row_data[8], row_data[9], row_data[10], row_data[11], row_data[12], row_data[13], row_data[14], row_data[15],row_data[16], row_data[17], row_data[18], row_data[19], row_data[20], row_data[21],)
        # %s are the number of columns in your file
        insert_query = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        # Execution of the data
        cur.execute(insert_query, row_data)
        # print(insert_query)
    print(row_data)
# # Commiting the changes
# conn.commit()
# # closing the connection
# conn.close()
#
# print('complete it')

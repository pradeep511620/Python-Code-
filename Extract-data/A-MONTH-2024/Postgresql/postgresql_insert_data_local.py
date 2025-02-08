import psycopg2
import csv

file_path = "C:/Users/PK/Downloads/industry_fabory.csv"
table_name_path = 'raw_db.scraped_pd_data'


create_connection = psycopg2.connect(host="127.0.0.1", dbname="postgres", user="postgres", password="7789", port="5432")
# Create a cursor object
create_object = create_connection.cursor()
print('Connection is created')

# create_object.execute("SELECT * FROM raw_db.scraped_pd_data LIMIT 5 ")
# row = create_object.fetchall()
# for rows in row:
#     print(rows)



#
with open(file_path, 'r', newline='', encoding='latin1') as csvfile:
    raw_data = csv.reader(csvfile)
    row_counter = 0
    next(raw_data)
    for row in raw_data:
        # row_counter += 1
        # if row_counter >= 5:
        #     break
        insert_query = (
            "INSERT INTO public.demo (brand, catlvl1, catlvl2, catlvl3, url, title, price_value, unit, "
            "shipping_weight, breadscrumbs, image_urls, mpn, specification_1, specification_2, datasheets, "
            "product_description_1, product_description_2, accessories, video_links, miscellaneous, scraped_by) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        value_data = row
        print(value_data)
        create_object.execute(insert_query, value_data)

create_connection.commit()
create_object.close()
create_connection.close()
print('Data inserted into the table.')

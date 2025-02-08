import psycopg2
import csv

file_path = r"C:\Users\prade\Downloads\taifittings_product_data.csv"
table_name_path = 'raw_db.scraped_pd_data'


class Upload_Data_On_DB:

    def __init__(self):
        self.create_object = None
        self.create_connection = None

    def connection_create_on_db(self):
        self.create_connection = psycopg2.connect(
            host="cleancatalograptorsupplies.cy63lzu6l3sf.ap-south-1.rds.amazonaws.com",
            database="raptor_db", user="rp_scraping_team",
            password="RaptorSuppliesScrapTeam#2024", port="5432")
        # Create a cursor object
        self.create_object = self.create_connection.cursor()
        print('Connection is created')

    def read_csv_from_files(self):
        with open(file_path, 'r', newline='', encoding='latin1') as csvfile:
            raw_data = csv.reader(csvfile)
            next(raw_data)  # Skip header row
            row_counter = 0
            for row in raw_data:
                row_counter += 1
                # if row_counter >= 30:
                #     break
                insert_query = (
                    f"INSERT INTO {table_name_path} (brand, catlvl1, catlvl2, catlvl3, url, title, price_value, unit, "
                    "shipping_weight, breadscrumbs, image_urls, mpn, specification_1, specification_2, datasheets, "
                    "product_description_1, product_description_2, accessories, video_links, miscellaneous, scraped_by) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                )
                value_data = row
                print(value_data)
                self.create_object.execute(insert_query, value_data)

    def commit_code(self):
        self.create_connection.commit()
        self.create_object.close()
        self.create_connection.close()
        print('Data inserted into the table and connection closed.')


def main():
    upload = Upload_Data_On_DB()
    upload.connection_create_on_db()  # calling function of connection
    upload.read_csv_from_files()  # read file or csv
    upload.commit_code()  # commited the code


if __name__ == "__main__":
    main()

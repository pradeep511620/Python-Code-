import pandas as pd
import mysql.connector
import xlrd

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_dat",
    port='3306'
)
cur = mydb.cursor()
cur.execute(
    "SELECT product_url,l3_name,parent_name,item_name,product_title,model_no,brand FROM `domino_clamps_onb_dba_121` ")
myresult = cur.fetchall()

print(myresult)

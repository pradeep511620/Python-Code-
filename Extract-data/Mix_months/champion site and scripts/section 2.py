from typing import TextIO

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

# url = "https://www.championbuilt.com/cht2416st.html"
# url = "https://www.championbuilt.com/cht3056.html"
url = "https://www.championbuilt.com/cts15pc.html"

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

# ========================================= part Number ========================================================
print("*********************************** Part Number: *************************************")
h2 = soup.find("h2", class_="wsite-content-title").text.strip()
h2_d = h2
print("Part N == ", h2_d)
print()
# ========================================= Description =========================================================
print("*********************************** Description : *************************************")
product = soup.find("div", class_="paragraph").text.strip()
product_d = product
print("Description == ", product_d)
print()
#
# # ============================================ Features =========================================================
print("*********************************** Features: *************************************")
f = soup.find("div", class_="tabbed-box-content tab-0")
f_d = f.text.strip()
print("Features == ", f_d)
print()

# ============================================ Specifications ===================================================
print("***********************************  Specifications: *************************************")
s = soup.find("div", class_="tabbed-box-content tab-1").text.strip()
s_d = s
print("Specifications = ", s_d)
print()

# ============================================ Options  =========================================================
print("***********************************  Options: *************************************")
op = soup.find("div", class_="tabbed-box-content tab-2").text.strip()
op_d = op
print("Options == ", op_d)
print()

# ============================================ Images =========================================================
print("*********************************** Images: *************************************")
image = soup.find("img", alt="Picture")
image_d = image
print("image_d", image_d.get('src'))
print()

# ============================================= color =========================================================
print("*********************************** color: *************************************")
# color_d = ""
co = soup.find_all("div", class_="wsite-section-wrap")[2]
for x in co:
    color_d = (x.text.strip().replace("COLORS", ""))
    print("color_d == ", color_d)

# ============================================ color image =========================================================
print("*********************************** color image: *************************************")
image1 = soup.find_all("div", class_="wsite-section-wrap")[2].find_all_next('img')
for x in image1:
    image2 = x.get('src')
    print("image2 == ", image2)

# save_details: TextIO = open("champion_section_2.txt", "a+", encoding="utf-8")
# save_details.write("\n" + url + "\t" + h2_d + "\t" + product_d + "\t" + f_d + "\t" + s_d + "\t" + op_d + "\t" + str(image_d) + "\t" + str(color_d) + "\t" + "".join(image2))
# print("End")
# save_details.close()
# print("\n ***** Record stored into champion_section_2 . *****")
# print()

import time
from typing import TextIO

import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# import time

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# opts = Options()
# opts.headless = False
# driver = webdriver.Chrome()
# driver.maximize_window()


mylst = [
    # 'https://www.panimatic.com/VERTICAL-WATER-CHILLER-50L_677_83_1234.html',
    # 'https://www.panimatic.com/VERTICAL-WATER-CHILLER-90L_677_83_1235.html',
    # 'https://www.panimatic.com/HORIZONTAL-WATER-CHILLER-50L_677_83_1236.html',
    # 'https://www.panimatic.com/HORIZONTAL-WATER-CHILLER-140L_677_83_1237.html',
    # 'https://www.panimatic.com/HORIZONTAL-WATER-CHILLER-360L_677_83_1238.html',
    # 'https://www.panimatic.com/INTERMEDIATE-PROVER-STANDARD-DEPTH_677_71_1239.html',
    # 'https://www.panimatic.com/INTERMEDIATE-PROVER-REDUCED-DEPTH_677_71_1240.html',
    # 'https://www.panimatic.com/INTERMEDIATE-PROVER-STANDARD-DEPTH-WIDE-POCKETS_677_71_1241.html',
    # 'https://www.panimatic.com/INTERMEDIATE-PROVER-REDUCED-DEPTH-WIDE-POCKETS_677_71_1242.html',
    # 'https://www.panimatic.com/MOULDER-F14_677_69_1243.html',
    # 'https://www.panimatic.com/PROOFER-400X600_677_65_1311.html',
    # 'https://www.panimatic.com/PROOFER-600x800_677_65_1312.html',
    # 'https://www.panimatic.com/PROOFER-400x800_677_65_1313.html',
    # 'https://www.panimatic.com/ROLL-IN-PROOFER_677_65_1314.html',
    # 'https://www.panimatic.com/PROOFER-OVEN-SUPPORT-9-LEVELS-E9_677_65_1315.html',
    # 'https://www.panimatic.com/PROOFER-OVEN-SUPPORT-400X600_677_65_1316.html',
    # 'https://www.panimatic.com/PROOFER-OVEN-SUPPORT-600x800_677_65_1318.html',
    # 'https://www.panimatic.com/PROOFER-OVEN-SUPPORT-400x800_677_65_1319.html',
    # 'https://www.panimatic.com/PROOFER-OVEN-SUPPORT-8-LEVELS-E8_677_65_1348.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-OVEN-SUPPORT-600X800_677_60_1262.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-OVEN-SUPPORT-400x800_677_60_1263.html',
    # 'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-FOR-TRAYS_677_60_1270.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-400x800_677_60_1271.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-460x800_677_60_1272.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-600x800_677_60_1273.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-600x900_677_60_1274.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-700-750x800_677_60_1275.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-700-750x900_677_60_1276.html',
    # 'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-FOR-FILETS_677_60_1285.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-USA_677_60_1345.html',
    # 'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-USA_677_60_1346.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-600x800_677_56_1273.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-600x900_677_56_1274.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-700-750x800_677_56_1275.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-700-750x900_677_56_1276.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-820X800_677_56_1277.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-900x800_677_56_1278.html',
    # 'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-FOR-FILETS_677_56_1285.html',
    # 'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-USA_677_56_1346.html',
    # 'https://www.panimatic.com/BENCH-RETARDER-PROOFER-DISMOUNTABLE_677_64_1260.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-OVEN-SUPPORT_677_64_1261.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-P16_677_64_1266.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-P22_677_64_1267.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-P127-ET-P1-24DB_677_64_1268.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-M2C48-ET-M54_677_64_1269.html',
    # 'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-FOR-TRAYS_677_64_1270.html',
    # 'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-FOR-FILETS_677_64_1285.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-USA_677_64_1345.html',
    # 'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-USA_677_64_1346.html',
    # 'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-FOR-TRAYS_677_62_1270.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-M-600X800_677_62_1279.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-MA-765X800_677_62_1280.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-A-935X800_677_62_1281.html',
    # 'https://www.panimatic.com/RETARDER-PROOFER-BA-1050X800_677_62_1282.html',
    'https://www.panimatic.com/RETARDER-PROOFER-B1-1250X800_677_62_1283.html',
    'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-FOR-GRIDS_677_62_1284.html',
    'https://www.panimatic.com/RETARDER-PROOFER-FOR-DOUGH-TRAYS_677_52_1264.html',
    'https://www.panimatic.com/ROLL-IN-RETARDER-PROOFER-FOR-DOUGH-TRAYS_677_52_1265.html',
    'https://www.panimatic.com/PANEL-2008_677_66_1286.html',
    'https://www.panimatic.com/PANEL-2012_677_66_1287.html',
    'https://www.panimatic.com/PANEL-2000-V2_677_66_1288.html',
    'https://www.panimatic.com/BENCH-FRIDGE-DISMOUNTABLE_677_80_1289.html',
    'https://www.panimatic.com/BENCH-FRIDGE-NOT-DISMOUNTABLE_677_80_1290.html',
    'https://www.panimatic.com/REFRIGERATED-CABINET_677_80_1291.html',
    'https://www.panimatic.com/REFRIGERATED-CABINET-400X600-STAINLESS-STEEL_677_80_1294.html',
    'https://www.panimatic.com/REFRIGERATED-CABINET-600X800-STAINLESS-STEEL_677_80_1295.html',
    'https://www.panimatic.com/REFRIGERATED-CABINET-P58_677_80_1296.html',
    'https://www.panimatic.com/WALK-IN-FRIDGE_677_80_1297.html',
    'https://www.panimatic.com/REFRIGERATED-CABINET-FOR-DOUGH-TRAYS_677_78_1292.html',
    'https://www.panimatic.com/ROLL-IN-FRIDGE-FOR-DOUGH-TRAYS_677_78_1293.html',
    'https://www.panimatic.com/CHOCOLATE-BENCH-400X600_677_79_1308.html',
    'https://www.panimatic.com/CHOCOLATE-CABINET-400X600_677_79_1309.html',
    'https://www.panimatic.com/CHOCOLATE-CABINET-600X800_677_79_1310.html',
    'https://www.panimatic.com/BENCH-FREEZER_677_50_1298.html',
    'https://www.panimatic.com/FREEZER-P58_677_50_1299.html',
    'https://www.panimatic.com/FREEZER-C87_677_50_1300.html',
    'https://www.panimatic.com/WALK-IN-FREEZER_677_50_1301.html',
    'https://www.panimatic.com/BENCH-BLAST-FREZZER_677_54_1304.html',
    'https://www.panimatic.com/WALK-IN-BLAST-FREEZER-CS1_677_54_1349.html',
    'https://www.panimatic.com/WALK-IN-BLAST-FREEZER-CS2_677_54_1350.html',
    'https://www.panimatic.com/FREEZER-BLAST-FREEZER-P88_677_58_1302.html',
    'https://www.panimatic.com/FREEZER-BLAST-FREEZER-P67_677_58_1303.html',
    'https://www.panimatic.com/FREEZER-BLAST-FREEZER-P58_677_58_1305.html',
    'https://www.panimatic.com/FREEZER-BLAST-FREEZER-P87-2_677_58_1306.html',
    'https://www.panimatic.com/FREEZER-BLAST-FREEZER-P87-3_677_58_1307.html',
    'https://www.panimatic.com/AUTOMATIC-COUCHE_677_76_1231.html',
    'https://www.panimatic.com/OPTICOUCHE_677_76_1232.html',
    'https://www.panimatic.com/COUCHES-CLEANER_677_76_1233.html',
    'https://www.panimatic.com/AUTOMATIC-COUCHES-CABINET_677_76_1253.html',
    'https://www.panimatic.com/PARISIEN-8-10-OR-20-LEVELS_677_75_1254.html',
    'https://www.panimatic.com/DOUGH-RESTING-CABINET_677_75_1255.html',
    'https://www.panimatic.com/DOUGH-RESTING-CABINET-FOR-TRAYS_677_75_1256.html',
    'https://www.panimatic.com/STAINLESS-STEEL-RACK-FOR-TRAYS-AND-FILETS_677_75_1257.html',
    'https://www.panimatic.com/RACK-FOR-DOUGH-TRAYS_677_75_1258.html',
    'https://www.panimatic.com/TROLLEY-FOR-GRIDS_677_75_1259.html',
    'https://www.panimatic.com/SALT-BENCH_677_77_1338.html',
    'https://www.panimatic.com/WORK-SURFACE_677_77_1339.html',
    'https://www.panimatic.com/CUSTOM-MADE-TABLE_677_77_1340.html',
    'https://www.panimatic.com/STORAGE-MODULES_677_77_1341.html',
    'https://www.panimatic.com/SLIDING-DOORS-UNIT_677_77_1342.html',
    'https://www.panimatic.com/OVEN-LOADING-TABLE_677_77_1343.html',
    'https://www.panimatic.com/WALL-RACK_677_74_1333.html',
    'https://www.panimatic.com/UTENSILS-HOLDER_677_74_1334.html',
    'https://www.panimatic.com/COUCHES-DRYER_677_74_1335.html',
    'https://www.panimatic.com/ELECTRIC-COUCHES-DRYER_677_74_1336.html',
    'https://www.panimatic.com/COUCHES-DRYER-TROLLEY_677_74_1337.html',
    'https://www.panimatic.com/VENTILATED-OVEN-4-LEVELS-F4_677_24_1320.html',
    'https://www.panimatic.com/VENTILATED-OVEN-6-LEVELS-F6_677_24_1321.html',
    'https://www.panimatic.com/VENTILATED-OVEN-9-LEVELS-F9_677_24_1322.html',
    'https://www.panimatic.com/VENTILATED-OVEN-USA_677_24_1347.html',
    'https://www.panimatic.com/VENTILATED-DECK-OVEN-400X600-T461_677_82_1325.html',
    'https://www.panimatic.com/DECK-OVEN-COMPAGNON-600_677_82_1327.html',
    'https://www.panimatic.com/DECK-OVEN-COMPAGNON-1200_677_82_1328.html',
    'https://www.panimatic.com/DECK-OVEN-COMPAGNON-750_677_82_1329.html',
    'https://www.panimatic.com/DECK-OVEN-COMPAGNON-900_677_82_1330.html',
    'https://www.panimatic.com/OPTICOUCHE_677_81_1232.html',
    'https://www.panimatic.com/EXTRACTOR-HOOD_677_81_1323.html',
    'https://www.panimatic.com/OVEN-SUPPORT_677_81_1324.html',
    'https://www.panimatic.com/OVEN-LOADER_677_81_1331.html',
    'https://www.panimatic.com/STEAM-CONDENSER_677_81_1332.html',
    'https://www.panimatic.com/OVEN-LOADING-TABLE_677_81_1343.html',
]


def extract_data(url1):
    l = 0
    # try:
    l = l + 1
    r = requests.get(url1)
    soup = BeautifulSoup(r.content, 'html.parser')
    # driver.get(url)
    time.sleep(3)
    # print(soup)
    technical = ''
    option = ''
    description = ''
    images = ''

    print("Product-urls", l, url1)
    try:
        print("********** Meta-Description : **********")
        meta_description = soup.find("meta", attrs={"name": "description"}).get("content").strip()
        print("Meta_description......", meta_description)
    except:
        meta_description = "Not Found"
        print("Not Found")

    try:
        print('********** Meta-Title : **********')
        meta_title = soup.find('title').string.strip()
        print("Meta_title .....", meta_title)
    except:
        meta_title = "Not Found"
        print("Not Found")

#
    try:
        print('********** Title : **********')
        title = soup.find('h1').text.strip()
        # print('title...', title)
    except:
        title = "Not Found"
        print("Not Found")

    try:
        print('********** Reference : **********')
        ref = soup.find('span', id="idml_reference_detail").text.strip()
        print('Reference...', ref)
    except:
        ref = "Not Found"
        print("Not Found")
#
    try:
        print('********** Images : **********')
        image = soup.find("div", {"class": "eshop-detail-photo"}).find_all('img')
        for imgs in image:
            images = "https://www.panimatic.com" + imgs.get('src')
            print('images...', images)
            save_details: TextIO = open("panimetic.txt", "a+", encoding="utf-8")
            save_details.write("\n" + url1 + "\t" + meta_description + "\t" + meta_title + "\t" + title + "\t" + ref + "\t" + images.strip())
            print("\n ***** Record stored into files. *****")
    except:
        images = "Not Found"
        print("Not Found")

#
    details = soup.find_all('div', {"class": "eshop-detail-description"})
    for js in details:
        data = js.text.strip().split('\n')
        # print(data)
        try:
            description = data[5].strip()
            print('Description...', description)
        except:
            description = "Not Found"
            print("Not Found Description")

        try:
            technical = data[10].strip()
            print('Technical...', technical)
        except:
            technical = "Not Found"
            print("Not Found Technical")

        try:
            option = data[15].strip()
            print('Option...', option)
            save_details: TextIO = open("panimetic.txt", "a+", encoding="utf-8")
            save_details.write("\n" + url1 + "\t" + meta_description + "\t" + meta_title + "\t" + title + "\t" + ref + "\t" + images + "\t" + description + "\t" + technical + "\t" + option.strip())
            print("\n ***** Record stored into files. *****")
        except:
            option = "Not Found"
            print("Not Found Option")
            save_details: TextIO = open("panimetic.txt", "a+", encoding="utf-8")
            save_details.write("\n" + url1 + "\t" + meta_description + "\t" + meta_title + "\t" + title + "\t" + ref + "\t" + images + "\t" + description + "\t" + technical + "\t" + option)
            print("\n ***** Record stored into exception files. *****")


#   here is the function for calling url and extract_data
for url in mylst:
    extract_data(url)
